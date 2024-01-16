package JAVA;

import java.util.Scanner;

class Fibonacci {
    public static void main(String[] args) {
        Scanner get = new Scanner(System.in);
        System.out.println("Enter the limit: ");
        int n = get.nextInt();
        get.close();
        int a = 0, b = 1, c = 0;
        System.out.println("Fibonacci series upto " + n + " is: ");
        System.out.print(a + " " + b + " ");
        while (c <= n) {
            c = a + b;
            if (c <= n)
                System.out.print(c + " ");
            a = b;
            b = c;
        }
    }
}