import java.util.Scanner;
class Sort {
    int[] array = null;
    Sort() {
        Scanner get = new Scanner(System.in);
        System.out.println("Enter the size of array: ");
        int size = get.nextInt();
        array = new int[size];
        System.out.println("Enter the elements of array: ");
        for (int i = 0; i < size; i++) {
            array[i] = get.nextInt();
        }
        get.close();
    }
    void print() {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }
    void BubbleSort() {
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }
    public static void main(String[] args) {
        Sort sort = new Sort();
        System.out.println("Before sorting: ");
        sort.print();
        sort.BubbleSort();
        System.out.println("After sorting: ");
        sort.print();
    }
}

