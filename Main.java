public class Main {
    /**
     * Return the sum of the given numeric array.
     */
    public static double sumOfNumbers(double[] numbers) {
        double sum = 0.0;
        if (numbers == null) return 0.0;
        for (double n : numbers) sum += n;
        return sum;
    }

    /**
     * Return the arithmetic mean of the given numeric array.
     * @throws IllegalArgumentException if numbers is null or empty
     */
    public static double averageOfNumbers(double[] numbers) {
        if (numbers == null || numbers.length == 0) {
            throw new IllegalArgumentException("averageOfNumbers requires a non-empty array");
        }
        return sumOfNumbers(numbers) / numbers.length;
    }

    public static void main(String[] args) {
        double[] nums = {1, 2, 3, 4, 5};
        System.out.println(sumOfNumbers(nums));      // prints 15.0
        System.out.println(averageOfNumbers(nums));  // prints 3.0
    }
}