package JAVA;
class ComplexStack  {
    private ComplexNumber[] stackArray;
    private int top;
    private int maxSize;
    
    public ComplexStack(int size) {
        maxSize = size;
        stackArray = new ComplexNumber[maxSize];
        top = -1;
    }
    public void push(ComplexNumber num) {
        if (top < maxSize - 1) {
            stackArray[++top] = num;
            System.out.println("Pushed: " + num);
        } else {
            System.out.println("Stack overflow. Cannot push " + num);
        }
    }

    public ComplexNumber pop() {
        if (top >= 0) {
            ComplexNumber popped = stackArray[top--];
            return popped;
        } else {
            System.out.println("Stack underflow. Cannot pop.");
            return null;
        }
    }
    
    public void display() {
        if (top >= 0) {
            System.out.print("Stack: ");
            for (int i = 0; i <= top; i++) {
                System.out.print(stackArray[i] + " ");
            }
            System.out.println();
        } else {
            System.out.println("Stack is empty.");
        }
    }
    public static void main(String[] args) {
        ComplexStack stack = new ComplexStack(5);

        stack.push(new ComplexNumber(2.5, 3.0));
        stack.push(new ComplexNumber(1.0, -2.0));
        stack.display();

        System.out.println("Popped: " + stack.pop().toString());
        stack.display();
    }
}

    class ComplexNumber {
        double real;
        double imaginary;
    
        public ComplexNumber(double real, double imaginary) {
            this.real = real;
            this.imaginary = imaginary;
        }
    
        @Override
        public String toString() {
            return real + " + " + imaginary + "i";
        }
    }