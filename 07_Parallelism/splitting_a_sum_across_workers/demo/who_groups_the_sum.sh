#!/usr/bin/env bash
# Two library calls that choose the grouping of a float sum for you, run where
# their choice shows. CI cannot hold either result as an answer key, because the
# answer depends on the machine.
#
#   1. std::reduce, built against libc++ (this Mac's c++) and against libstdc++
#      (GCC in the Docker image gcc:14).
#   2. Java's parallel DoubleStream.reduce(0.0, Double::sum), with the common
#      fork-join pool set to different sizes.
#
#   bash demo/who_groups_the_sum.sh          # from the lesson folder; needs Docker
set -eu
cd "$(dirname "$0")"
dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT

echo "the 24 values plus 0.2 each; one loop gives 99.80000000000004"
echo
echo "std::reduce(floats.begin(), floats.end(), 0.0):"
c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic reduce_cpp.cpp -o "$dir/reduce_cpp"
printf '  %-38s %s\n' "$(c++ --version | head -1 | cut -d'(' -f1)with libc++" "$("$dir/reduce_cpp")"
docker run --rm --ulimit fsize=104857600 -v "$PWD:/src:ro" gcc:14 bash -c \
    'c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic /src/reduce_cpp.cpp -o /tmp/reduce_cpp &&
     printf "  %-38s %s\n" "GCC $(c++ -dumpfullversion) with libstdc++" "$(/tmp/reduce_cpp)"'

echo
echo "DoubleStream.of(floats).parallel().reduce(0.0, Double::sum), $(java --version | head -1 | cut -d' ' -f1-2):"
for size in 1 2 3 4 8; do
    printf '  common pool parallelism %-14s %s\n' "$size" \
        "$(java -Djava.util.concurrent.ForkJoinPool.common.parallelism="$size" parallel_reduce_java.java)"
done
