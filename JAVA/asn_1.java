import java.util.Scanner;
class Timestamp {
    int hour, minute, second;
    Timestamp() {
        hour = 0;
        minute = 0;
        second = 0;
    }
    Timestamp(int hour, int minute, int second) {
        this.hour = hour;
        this.minute = minute;
        this.second = second;
    }
    public Timestamp add(Timestamp t1, Timestamp t2) {
        int newHour = t1.hour + t2.hour;
        int newMinute = t1.minute + t2.minute;
        int newSecond = t1.second + t2.second;
        if (newSecond >= 60) {
            newSecond -= 60;
            newMinute++;
        }
        if (newMinute >= 60) {
            newMinute -= 60;
            newHour++;
        }
        return new Timestamp(newHour, newMinute, newSecond);
    }
    String print() {
        return hour + ":" + minute + ":" + second;
    }
    public static void main(String[] args) {
        Scanner get = new Scanner(System.in);
        System.out.println("Enter hour: ");
        int hour = get.nextInt();
        System.out.println("Enter minute: ");
        int minute = get.nextInt();
        System.out.println("Enter second: ");
        int second = get.nextInt();
        get.close();
        Timestamp t1 = new Timestamp(hour, minute, second);
        Timestamp t2 = new Timestamp(hour, minute, second);
        Timestamp t3 = new Timestamp();
        t3 = t3.add(t1, t2);
        System.out.println("Time 1: " + t1.print());
        System.out.println("Time 2: " + t2.print());
        System.out.println("Time 3: " + t3.print());
    }
}