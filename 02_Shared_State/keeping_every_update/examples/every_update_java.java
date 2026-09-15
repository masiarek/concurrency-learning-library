// Keeping every update, three ways. Eight handlers each add the numbers 1 to
// 10,000 to one total: inside a synchronized block, with an AtomicLong, and by
// handing every addition to a single-thread executor, the one thread that owns
// the total.
//
//   java every_update_java.java      (Java 25: a compact source file, which imports java.base)

final int HANDLERS = 8;
final long LAST = 10_000;

final Object lock = new Object();
long lockedTotal = 0;
long ownedTotal = 0; // touched only by the owner thread, and read after it has finished

void runHandlers(Runnable handler) throws InterruptedException {
    List<Thread> threads = new ArrayList<>();
    for (int i = 0; i < HANDLERS; i++) {
        threads.add(Thread.ofPlatform().start(handler));
    }
    for (Thread t : threads) {
        t.join();
    }
}

long withSynchronized() throws InterruptedException {
    runHandlers(() -> {
        for (long n = 1; n <= LAST; n++) {
            synchronized (lock) {
                lockedTotal += n; // load, add and store, all while holding the lock
            }
        }
    });
    return lockedTotal;
}

long withAnAtomicAdd() throws InterruptedException {
    AtomicLong total = new AtomicLong();
    runHandlers(() -> {
        for (long n = 1; n <= LAST; n++) {
            total.addAndGet(n); // one indivisible operation
        }
    });
    return total.get();
}

long withOneOwner() throws InterruptedException {
    try (ExecutorService owner = Executors.newSingleThreadExecutor()) {
        runHandlers(() -> {
            for (long n = 1; n <= LAST; n++) {
                long number = n;
                owner.execute(() -> ownedTotal += number); // queued, run one at a time
            }
        });
    } // close() waits until the owner has run every queued addition
    return ownedTotal;
}

void main() throws InterruptedException {
    IO.println(HANDLERS + " handlers each add 1 to " + LAST + "; the total should be "
            + HANDLERS * LAST * (LAST + 1) / 2);
    IO.println("with synchronized:    " + withSynchronized());
    IO.println("with AtomicLong:      " + withAnAtomicAdd());
    IO.println("with one owner:       " + withOneOwner());
}
