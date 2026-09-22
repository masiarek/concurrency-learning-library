#!/usr/bin/env bash
# Not run by CI. AddressSanitizer against the C program in
# examples/lend_local_dangling_c_sh.sh, whose dangling pointer the plain compile
# does not mention. The report carries addresses, thread ids and a pid, and the
# two runtimes do not agree on the exit status, so this belongs in a
# "Real runs" fence and not in a key. Each run sleeps a second.
#
#   bash demo/use_after_return.sh          on this machine
#
# The Linux column was taken with the same script inside `docker run --rm
# --ulimit fsize=104857600 -v "$PWD:/w" -w /w gcc:14`.
set -u

runs=${1:-10}
dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT

here=$(cd "$(dirname "$0")" && pwd)
# One copy of the program: the heredoc inside the example driver.
awk "/<<'C'\$/{flag=1;next} /^C\$/{flag=0} flag" "$here/../examples/lend_local_dangling_c_sh.sh" >"$dir/dangling.c"

"${CC:-cc}" -std=c17 -Wall -Wextra -pedantic -pthread -fsanitize=address -g -O1 \
    "$dir/dangling.c" -o "$dir/dangling" || exit 1

reported=0
statuses=""
for _ in $(seq 1 "$runs"); do
    # A run that aborts makes the shell announce the signal; keep that off the report.
    ( (cd "$dir" && ASAN_OPTIONS=detect_stack_use_after_return=1 ./dangling >stdout.txt 2>stderr.txt) ) 2>/dev/null
    status=$?
    grep -q 'AddressSanitizer: stack-use-after-' "$dir/stderr.txt" && reported=$((reported + 1))
    case " $statuses " in
        *" $status "*) ;;
        *) statuses="$statuses $status" ;;
    esac
done

"${CC:-cc}" --version | head -n 1
echo "$reported of $runs runs reported an AddressSanitizer stack error, of which the first was:"
grep -m 1 -o 'AddressSanitizer: stack-use-after-[a-z]*' "$dir/stderr.txt" | sed 's/^/  ERROR: /'
grep -m 1 -oE '(READ|WRITE) of size [0-9]+ at 0x[0-9a-f]+ thread T[0-9]+' "$dir/stderr.txt" | sed 's/0x[0-9a-f]*/0x…/; s/^/  /'
grep -m 1 -o 'is located in stack of thread T[0-9]*.*' "$dir/stderr.txt" | sed 's/^/  /'
grep -m 1 -o "'left' (line [0-9]*).*" "$dir/stderr.txt" | sed 's/^/    /'
grep -m 1 -o 'SUMMARY: AddressSanitizer: .*' "$dir/stderr.txt" | sed 's#/[^ ]*/dangling\.c#dangling.c#; s/^/  /'
echo "exit statuses seen:$statuses"
echo "what the program printed: $(cat "$dir/stdout.txt")"
