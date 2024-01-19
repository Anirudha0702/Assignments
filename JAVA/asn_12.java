abstract class Employee {
    private String name;
    private int employeeId;
    private double basicSalary;
    public Employee(String name, int employeeId, double basicSalary) {
        this.name = name;
        this.employeeId = employeeId;
        this.basicSalary = basicSalary;
    }
    public abstract double calculateNetSalary();
    public abstract void displayInformation();
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getEmployeeId() {
        return employeeId;
    }
    public void setEmployeeId(int employeeId) {
        this.employeeId = employeeId;
    }
    public double getBasicSalary() {
        return basicSalary;
    }
    public void setBasicSalary(double basicSalary) {
        this.basicSalary = basicSalary;
    }
}
class Manager extends Employee {
    private double bonus;
    public Manager(String name, int employeeId, double basicSalary, double bonus) {
        super(name, employeeId, basicSalary);
        this.bonus = bonus;
    }
    @Override
    public double calculateNetSalary() {
        return getBasicSalary() + bonus;
    }
    @Override
    public void displayInformation() {
        System.out.println("Manager Information:");
        System.out.println("Name: " + getName());
        System.out.println("Employee ID: " + getEmployeeId());
        System.out.println("Basic Salary: $" + getBasicSalary());
        System.out.println("Bonus: $" + bonus);
        System.out.println("Net Salary: $" + calculateNetSalary());
    }
}
class Clerk extends Employee {
    private double overtimeHours;
    public Clerk(String name, int employeeId, double basicSalary, double overtimeHours) {
        super(name, employeeId, basicSalary);
        this.overtimeHours = overtimeHours;
    }
    @Override
    public double calculateNetSalary() {
        return getBasicSalary() + (overtimeHours * 10);
    }
    @Override
    public void displayInformation() {
        System.out.println("Clerk Information:");
        System.out.println("Name: " + getName());
        System.out.println("Employee ID: " + getEmployeeId());
        System.out.println("Basic Salary: $" + getBasicSalary());
        System.out.println("Overtime Hours: " + overtimeHours);
        System.out.println("Net Salary: $" + calculateNetSalary());
    }
}

public class Asn_12 {
    public static void main(String[] args) {
        Manager manager = new Manager("John Manager", 101, 50000, 10000);
        Clerk clerk = new Clerk("Alice Clerk", 201, 30000, 20);
        manager.displayInformation();
        clerk.displayInformation();
    }
}

