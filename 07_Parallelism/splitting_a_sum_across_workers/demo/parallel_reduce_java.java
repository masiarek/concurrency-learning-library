// A parallel stream splits the array however its fork-join pool decides; this
// prints the total it reached for the lesson's 24 values plus 0.2 each.
void main() {
    long[] values = {1, 4, 3, 9, 2, 8, 5, 1, 1, 6, 2, 7, 2, 5, 0, 4, 1, 8, 6, 5, 1, 2, 3, 9};
    double[] floats = new double[values.length];
    for (int i = 0; i < values.length; i++) {
        floats[i] = values[i] + 0.2;
    }
    IO.println(DoubleStream.of(floats).parallel().reduce(0.0, Double::sum));
}
