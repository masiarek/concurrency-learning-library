// Four platform threads, a million additions each, to a plain long field with
// nothing guarding it. Prints how many additions were lost.

final int THREADS = 4;
final int EACH = 1_000_000;

long total = 0;

void main() throws InterruptedException {
    List<Thread> threads = new ArrayList<>();
    for (int i = 0; i < THREADS; i++) {
        threads.add(Thread.ofPlatform().start(() -> {
            for (int j = 0; j < EACH; j++) {
                total += 1;
            }
        }));
    }
    for (Thread t : threads) {
        t.join();
    }
    IO.println((long) THREADS * EACH - total);
}
