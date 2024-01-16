package JAVA;
import java.util.Scanner;
public class asn_7 {

	public static void main(String[] args) {
		Scanner getInput=new Scanner(System.in);
        System.out.print("Enter NAme: ");
		String name=getInput.nextLine();
        System.out.print("Enter Address: ");
		String address=getInput.nextLine();
        System.out.print("Enter Program enrolled in: ");
		String program=getInput.nextLine();
        System.out.print("Enter Year of enroll ment: ");
		String year=getInput.nextLine();
        System.out.print("Enter Enrolled school: ");
		String school=getInput.nextLine();
        System.out.print("Enter Program fees: ");
		double fees=getInput.nextDouble();
        System.out.print("Enter Staff pay: ");
		double pay=getInput.nextDouble();
		getInput.close();
		Person person=new Person(name,address);
		person.tostring();
		Student student=new Student(name,address,program,year,fees);
		student.tostring();
		Staff staff=new Staff(name,address,school,pay);
		staff.tostring();

	}

}
class Person{
	String name;
	String address;
	Person(String name,String address){
		this.name=name;
		this.address=address;
	}
	void setPerson(String name,String address){
		this.name=name;
		this.address=address;
	}
	void tostring(){
		System.out.println("Person[name="+name+",address="+address+"]");
	}
}
class Student extends Person{
	String program;
	String year;
	double fees;
	Student(String name, String address,String program,String year,double fees) {
		super(name, address);
		this.program=program;
		this.year=year;
		this.fees=fees;
	}
	void setStudent(String name, String address,String program,String year,double fees){
		super.setPerson(name, address);
		this.program=program;
		this.fees=fees;
		this.year=year;
		
	}
	void tostring(){
		System.out.println("Person[name="+name+",address="+address+",program="+program+",year="+year+",fees="+fees+"]");
	}
	
}
class Staff extends Person{
	String school;
	double pay;
	Staff(String name, String address,String school,double pay){
		super(name, address);
		this.school=school;
		this.pay=pay;
	}
	void setStudent(String name, String address,String school,double pay){
		super.setPerson(name, address);
		this.pay=pay;
		this.school=school;	
	}
	void tostring(){
		System.out.println("Person[name="+name+",address="+address+",School="+school+",Pay="+pay+"]");
	}
	
}

 
