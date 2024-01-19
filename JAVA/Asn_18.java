import java.util.Scanner;
public class Asn_18 {
    public static void main(String[] args) {
        Scanner get = new Scanner(System.in);
        System.out.println("Enter the size of the array: ");
        int size = get.nextInt();
        get.close();
        try {
            createArray(size);
            System.out.println("Array created successfully.");
        } catch (NegativeSizeException e) {
            System.out.println("NegativeSizeException: " + e.getMessage());
        }
    }
    static void createArray(int size) throws NegativeSizeException {
        if (size < 0) {
            throw new NegativeSizeException("Array size cannot be negative.");
        }
        int[] array = new int[size];
        System.out.println("Array created with size: " + size);
    }
}
class NegativeSizeException extends Exception {
    public NegativeSizeException(String message) {
        super(message);
    }
}

