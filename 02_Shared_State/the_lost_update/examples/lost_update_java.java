// The lost update, forced. `total += 1` is three steps -- load, add, store --
// and nothing stops ten threads from all loading the same old total. A
// CyclicBarrier holds every thread between its load and its store, so every
// load happens before any store, on every run.
//
// `total` is an AtomicLong, so each get() and each set() is atomic. The pair is
// not.
//
//   java lost_update_java.java      (Java 25: a compact source file, which imports java.base)

final int HANDLERS = 10;

void main() throws InterruptedException {
    AtomicLong total = new AtomicLong();
    CyclicBarrier allLoaded = new CyclicBarrier(HANDLERS);
    long[] loaded = new long[HANDLERS];

    List<Thread> handlers = new ArrayList<>();
    for (int i = 0; i < HANDLERS; i++) {
        int slot = i;
        handlers.add(Thread.ofPlatform().start(() -> {
            long seen = total.get();  // 1. load
            loaded[slot] = seen;
            awaitAll(allLoaded);      // every handler has loaded
            total.set(seen + 1);      // 2. add, 3. store
        }));
    }
    for (Thread handler : handlers) {
        handler.join();
    }

    IO.println(HANDLERS + " handlers each added 1 to a total that started at 0");
    IO.println("the totals they loaded: " + Arrays.toString(loaded));
    IO.println("the total is " + total.get() + ", not " + HANDLERS);
}

void awaitAll(CyclicBarrier barrier) {
    try {
        barrier.await();
    } catch (InterruptedException | BrokenBarrierException e) {
        throw new IllegalStateException(e);
    }
}
