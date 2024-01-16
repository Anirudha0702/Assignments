package JAVA;
public class asn_8 {

	public static void main(String[] args) {
		Cylinder cylndr=new Cylinder(2,3);
		cylndr.getVolume();

	}

}
class Square{
	double side;
	Square(double side){
		this.side=side;
	}
	void getVolume(){
		
	}
}
class Cylinder extends Square{
	double height;
	Cylinder(double radius,double height){
		super(radius);
		this.height=height;
		
	}
	void getVolume(){
		System.out.println("Volume=" +(3.14*this.side*this.side*height));
	}
}


