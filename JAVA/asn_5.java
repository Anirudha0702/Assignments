package JAVA;

import java.util.Scanner;

class MatrixOperations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of rows for matrices A and B:");

        int rowsA = scanner.nextInt();
        System.out.print("Enter the number of columns for matrices A andB: ");

        int colsA = scanner.nextInt();
        int[][] matrixA = inputMatrix("A", rowsA, colsA, scanner);
        int[][] matrixB = inputMatrix("B", rowsA, colsA, scanner);
        int[][] sumMatrix = addMatrices(matrixA, matrixB);
        int[][] productMatrix = multiplyMatrices(matrixA, matrixB);
        System.out.println("Matrix A:");
        printMatrix(matrixA);
        System.out.println("Matrix B:");
        printMatrix(matrixB);
        System.out.println("Sum of Matrix A and B:");
        printMatrix(sumMatrix);
        System.out.println("Product of Matrix A and B:");
        printMatrix(productMatrix);
        scanner.close();
    }

    public static int[][] inputMatrix(String matrixName, int rows, int cols, Scanner scanner) {

        System.out.println("Enter elements for Matrix " + matrixName +

                ":");

        int[][] matrix = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print("Enter element at row " + (i + 1) + ",column " + (j + 1) + ": ");

                matrix[i][j] = scanner.nextInt();
            }
        }
        return matrix;
    }

    public static int[][] addMatrices(int[][] matrixA, int[][] matrixB) {
        int rows = matrixA.length;
        int cols = matrixA[0].length;
        int[][] result = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[i][j] = matrixA[i][j] + matrixB[i][j];
            }
        }
        return result;
    }

    public static int[][] multiplyMatrices(int[][] matrixA, int[][] matrixB) {

        int rowsA = matrixA.length;
        int colsA = matrixA[0].length;
        int colsB = matrixB[0].length;
        int[][] result = new int[rowsA][colsB];
        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                int sum = 0;
                for (int k = 0; k < colsA; k++) {
                    sum += matrixA[i][k] * matrixB[k][j];
                }
                result[i][j] = sum;

            }
        }
        return result;
    }

    public static void printMatrix(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
