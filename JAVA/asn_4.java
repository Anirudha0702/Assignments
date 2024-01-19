public class Asn_4 {
    public static void main(String[] args) {
        MyPoint point1 = new MyPoint();
        System.out.println("Default Constructor: " + point1);
        MyPoint point2 = new MyPoint(3, 4);
        System.out.println("Overloaded Constructor: " + point2);
        point1.setXY(1, 2);
        System.out.println("setXY Method: " + point1);
        int[] coordinates = point2.getXY();
        System.out.println("getXY Method: (" + coordinates[0] + ", " + coordinates[1] + ")");
        double distance = point1.distance(5, 6);
        System.out.println("Distance Method: " + distance);
    }
}
class MyPoint {
    private int x;
    private int y;
    public MyPoint() {
        this.x = 0;
        this.y = 0;
    }
    public MyPoint(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public void setXY(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public int[] getXY() {
        int[] result = { this.x, this.y };
        return result;
    }
    public double distance(int x, int y) {
        int xDiff = this.x - x;
        int yDiff = this.y - y;
        return Math.sqrt(xDiff * xDiff + yDiff * yDiff);
    }
    @Override
    public String toString() {
        return "(" + this.x + ", " + this.y + ")";
    }
}

