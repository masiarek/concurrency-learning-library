// Getting a result back. In Java, Thread.join() returns void. A Future from an
// ExecutorService carries the value back, and get() wraps a thrown exception in
// an ExecutionException.
//
//   java result_back_java.java      (Java 25: a compact source file, which imports java.base)

void main() throws Exception {
    long[] box = new long[1];
    Thread thread = Thread.ofPlatform().start(() -> box[0] = sumTo100());
    thread.join();
    IO.println("after join(), the array the lambda captured holds " + box[0]);

    try (ExecutorService pool = Executors.newVirtualThreadPerTaskExecutor()) {
        Callable<Long> sum = this::sumTo100;
        Future<Long> future = pool.submit(sum);
        IO.println("Future.get() returned " + future.get());

        Callable<Long> noTotalToday = () -> {
            throw new IllegalStateException("no total today");
        };
        Future<Long> failing = pool.submit(noTotalToday);
        try {
            failing.get();
        } catch (ExecutionException e) {
            IO.println("Future.get() threw ExecutionException, caused by " + e.getCause());
        }
    }
}

long sumTo100() {
    long total = 0;
    for (int i = 1; i <= 100; i++) {
        total += i;
    }
    return total;
}
