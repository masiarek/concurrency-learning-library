#!/usr/bin/env bash
# Not run by CI. ThreadSanitizer against the C program in
# examples/same_value_c_sh.sh, whose data race the plain compile does not
# mention. The report's addresses, pids, thread ids and the width it says was
# written are all the machine's, and the exit status differs between libtsan
# and Apple's runtime, so this belongs in a "Real runs" fence and not in a key.
#
#   bash demo/thread_sanitizer.sh          on this machine
#
# The Linux column was taken with the same script inside `docker run --rm
# --ulimit fsize=104857600 -v "$PWD:/w" -w /w gcc:14`.
set -u

runs=${1:-20}
dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT

here=$(cd "$(dirname "$0")" && pwd)
# One copy of the program: the heredoc inside the example driver.
awk "/<<'C'\$/{flag=1;next} /^C\$/{flag=0} flag" "$here/../examples/same_value_c_sh.sh" >"$dir/same_value.c"

"${CC:-cc}" -std=c17 -Wall -Wextra -pedantic -pthread -fsanitize=thread -g -O1 \
    "$dir/same_value.c" -o "$dir/same_value" || exit 1

reported=0
statuses=""
for _ in $(seq 1 "$runs"); do
    # A run that aborts makes the shell announce the signal; keep that off the report.
    ( (cd "$dir" && ./same_value >stdout.txt 2>stderr.txt) ) 2>/dev/null
    status=$?
    grep -q 'WARNING: ThreadSanitizer: data race' "$dir/stderr.txt" && reported=$((reported + 1))
    case " $statuses " in
        *" $status "*) ;;
        *) statuses="$statuses $status" ;;
    esac
done

"${CC:-cc}" --version | head -n 1
echo "$reported of $runs runs reported: WARNING: ThreadSanitizer: data race"
echo "exit statuses seen:$statuses"
grep -m 1 -o 'Write of size [0-9]*' "$dir/stderr.txt"
echo "what the program printed: $(cat "$dir/stdout.txt")"
