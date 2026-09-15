// Who waits when main returns? In Java, the JVM does: it will not exit while a
// thread that is not a daemon is still running. A virtual thread is always a daemon.
//
//   java who_waits_java.java      (Java 25: a compact source file, no class declaration)

void main() {
    Thread platform = Thread.ofPlatform().start(() -> work("platform thread:", 1));
    Thread virtual = Thread.ofVirtual().start(() -> work("virtual thread: ", 3));

    IO.println("platform thread is a daemon: " + platform.isDaemon());
    IO.println("virtual thread is a daemon:  " + virtual.isDaemon());
    IO.println("main:             returning");
}

void work(String label, int seconds) {
    try {
        Thread.sleep(seconds * 1000L);
    } catch (InterruptedException e) {
        return;
    }
    IO.println(label + "  finished");
}
