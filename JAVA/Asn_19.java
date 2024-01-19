public class Asn_19 {
    static int totalThreads=4;
    public static void main(String[] args) {
        Counter counter=new Counter();
        for(int i=0;i<totalThreads;i++){
            Thread t=new Thread(new CustomThread(counter,"Thread--"+i));
            t.start();
        }
    }
}
class Counter{
    private int count=0;
    public synchronized void increment(){
        count++;
        System.out.println(" Count is : "+count+" incremented by "+Thread.currentThread().getName());
    }
}
class CustomThread implements Runnable{
    Counter counter;
    private String threadName;
    public CustomThread(Counter counter,String name){
        this.counter=counter;
        this.threadName=name;
    }
    @Override
    public void run() {
        for(int i=0;i<3;i++){
            counter.increment();
            try {
                Thread.sleep(100);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}

