// Splitting a sum across workers. Each thread adds its own run of values into a
// variable no other thread can see, and the partial sums are then combined two
// ways: one after another, and as a tree whose rounds add pairs at the same time.
// Then the same split, with doubles.
//
// Java's generics do not cover long and double, so the methods that add come
// twice, once for each.
//
//   java split_sum_java.java      (Java 25: a compact source file, which imports java.base)

final int WORKERS = 8; // a power of two, so every round pairs everyone up
final long[] VALUES = {1, 4, 3, 9, 2, 8, 5, 1, 1, 6, 2, 7, 2, 5, 0, 4, 1, 8, 6, 5, 1, 2, 3, 9};

record Combined(String total, int additions, int rounds) {}

// Run job(0) ... job(n - 1), each on its own thread, and wait for all of them.
void runAll(int n, IntConsumer job) {
    List<Thread> threads = new ArrayList<>();
    for (int i = 0; i < n; i++) {
        int index = i;
        threads.add(Thread.ofPlatform().start(() -> job.accept(index)));
    }
    try {
        for (Thread t : threads) {
            t.join();
        }
    } catch (InterruptedException e) {
        throw new IllegalStateException(e);
    }
}

// Each worker adds its own run, left to right, into its own mySum, and stores
// the result in its own slot of sums.
long[] partialSums(long[] values, int workers) {
    int width = values.length / workers;
    long[] sums = new long[workers];
    runAll(workers, w -> {
        long mySum = values[w * width];
        for (int i = w * width + 1; i < (w + 1) * width; i++) {
            mySum += values[i];
        }
        sums[w] = mySum;
    });
    return sums;
}

double[] partialSums(double[] values, int workers) {
    int width = values.length / workers;
    double[] sums = new double[workers];
    runAll(workers, w -> {
        double mySum = values[w * width];
        for (int i = w * width + 1; i < (w + 1) * width; i++) {
            mySum += values[i];
        }
        sums[w] = mySum;
    });
    return sums;
}

// Each round adds neighbouring pairs, every pair on its own thread, until one
// value is left.
Combined treeCombine(long[] sums, boolean showRounds) {
    long[] level = sums;
    int additions = 0;
    int rounds = 0;
    while (level.length > 1) {
        long[] from = level;
        long[] next = new long[from.length / 2];
        runAll(next.length, i -> next[i] = from[2 * i] + from[2 * i + 1]);
        additions += next.length;
        rounds++;
        level = next;
        if (showRounds) {
            IO.println("tree, round " + rounds + ": " + joined(Arrays.stream(level).boxed()));
        }
    }
    return new Combined(Long.toString(level[0]), additions, rounds);
}

double treeCombine(double[] sums) {
    double[] level = sums;
    while (level.length > 1) {
        double[] from = level;
        double[] next = new double[from.length / 2];
        runAll(next.length, i -> next[i] = from[2 * i] + from[2 * i + 1]);
        level = next;
    }
    return level[0];
}

String joined(Stream<?> xs) {
    return xs.map(String::valueOf).collect(Collectors.joining(" "));
}

void main() {
    IO.println(VALUES.length + " values, " + VALUES.length / WORKERS + " to each of " + WORKERS + " workers");
    long[] partials = partialSums(VALUES, WORKERS);
    IO.println("partial sums: " + joined(Arrays.stream(partials).boxed()));
    long serialTotal = partials[0];
    for (int w = 1; w < partials.length; w++) {
        serialTotal += partials[w];
    }
    int serialAdditions = partials.length - 1;
    IO.println("serial combine: " + serialTotal + ", after " + serialAdditions + " additions in "
            + serialAdditions + " rounds");
    Combined tree = treeCombine(partials, true);
    IO.println("tree combine: " + tree.total() + ", after " + tree.additions() + " additions in "
            + tree.rounds() + " rounds");

    double[] floats = new double[VALUES.length];
    for (int i = 0; i < VALUES.length; i++) {
        floats[i] = VALUES[i] + 0.2;
    }
    IO.println();
    IO.println("the same " + floats.length + " values plus 0.2 each, as double (on paper, 99.8)");
    double loopTotal = 0.0;
    for (double x : floats) {
        loopTotal += x;
    }
    IO.println("one loop over all " + floats.length + ": " + loopTotal);
    double[] floatPartials = partialSums(floats, WORKERS);
    double floatSerial = floatPartials[0];
    for (int w = 1; w < floatPartials.length; w++) {
        floatSerial += floatPartials[w];
    }
    IO.println("partial sums, then serial: " + floatSerial);
    IO.println("partial sums, then tree: " + treeCombine(floatPartials));
    IO.println("DoubleStream.reduce(0.0, Double::sum): " + DoubleStream.of(floats).reduce(0.0, Double::sum));
    IO.println("DoubleStream.sum(): " + DoubleStream.of(floats).sum());
}
