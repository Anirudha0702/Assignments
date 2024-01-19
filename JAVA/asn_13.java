class VehicleEngine implements Engine {
    private int speed;
    private int gear;
    public VehicleEngine() {
        speed = 0;
        gear = 1;
    }
    @Override
    public void speedUp(int value) {
        if (value > 0) {
            speed += value;
            System.out.println("Speeding up. New speed: " + speed);
        } else {
            System.out.println("Invalid speed value. Speed must be greater than 0.");
        }
    }
    @Override
    public void changeGear(int value) {
        if (value >= 1 && value <= 6) {
            gear = value;
            System.out.println("Changing gear to: " + gear);
        } else {
            System.out.println("Invalid gear value. Gear must be between 1 and 6.");
        }
    }
    public void displayStatus() {
        System.out.println("Current Speed: " + speed + ", Current Gear: " + gear);
    }
    public static void main(String[] args) {
        VehicleEngine carEngine = new VehicleEngine();

        carEngine.speedUp(20);
        carEngine.changeGear(2);
        carEngine.speedUp(30);
        carEngine.displayStatus();
    }
}
interface Engine {
    void speedUp(int value);
    void changeGear(int value);
}