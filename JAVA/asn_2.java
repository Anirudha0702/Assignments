package JAVA;

import java.util.Scanner;

class ComplexNumber {
    double real, imaginary;

    void getdata(Scanner get) {
        System.out.println("Enter real part: ");
        this.real = get.nextDouble();
        System.out.println("Enter imaginary part: ");
        this.imaginary = get.nextDouble();
    }

    void showdata() {
        System.out.println("Complex number: " + this.real + " + " +

                this.imaginary + "i");
    }

    static ComplexNumber add(ComplexNumber c1, ComplexNumber c2) {
        ComplexNumber c3 = new ComplexNumber();
        c3.real = c1.real + c2.real;
        c3.imaginary = c1.imaginary + c2.imaginary;
        return c3;
    }

    static ComplexNumber multiply(ComplexNumber c1, ComplexNumber c2) {
        ComplexNumber c3 = new ComplexNumber();
        c3.real = c1.real * c2.real - c1.imaginary * c2.imaginary;
        c3.imaginary = c1.real * c2.imaginary + c1.imaginary * c2.real;
        return c3;
    }

    public static void main(String[] args) {
        ComplexNumber c1 = new ComplexNumber();
        ComplexNumber c2 = new ComplexNumber();
        ComplexNumber c3 = new ComplexNumber();
        ComplexNumber c4 = new ComplexNumber();
        Scanner get = new Scanner(System.in);
        c1.getdata(get);
        c2.getdata(get);
        get.close();

        c3 = add(c1, c2);
        c4 = multiply(c1, c2);
        c1.showdata();
        c2.showdata();
        c3.showdata();
        c4.showdata();
    }
}
