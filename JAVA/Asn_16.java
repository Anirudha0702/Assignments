import java.util.Scanner;
public class Asn_16 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            int[] numbers = {1, 2, 3, 4, 5};
            System.out.print("Enter the index to access from the array: ");
            int index = scanner.nextInt();
            int result = numbers[index];
            System.out.println("Value at index " + index + ": " + result);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("ArrayIndexOutOfBoundsException: Index is out of bounds.");
        }
        try {
            System.out.print("Enter a divisor to perform division: ");
            int divisor = scanner.nextInt();
            int result = 10 / divisor;
            System.out.println("Result of division: " + result);
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException: Cannot divide by zero.");
        }
        scanner.close();
    }
}
