import java.util.LinkedList;
public class Asn_20 {
    public static void main(String[] args) {
        Resource resource=new Resource(5);
        Producer producer=new Producer(resource);
        Consumer consumer=new Consumer(resource);
        producer.start();
        consumer.start();
    }
}
class Resource{
    private LinkedList<Integer> buffer=new LinkedList<>();
    private int capacity;
    public Resource(int capacity){
        this.capacity=capacity;
    }
    public void consume(){
        synchronized(this){
            while(buffer.size()==0){
                try {
                    wait();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
            int val=buffer.removeFirst();
            System.out.println("Consumed : "+val);
            notify();
        }
    }
    public void produce(){
        synchronized(this){
            while(buffer.size()==this.capacity){
                try {
                    wait();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
            int item = (int) (Math.random() * 100);
            buffer.add(item);
            System.out.println("Produced : " + item);
            notify();
        }
    }
}
class Producer extends Thread{
    private Resource sharedResource;
    public Producer(Resource sharedResource){
        this.sharedResource=sharedResource;
    }
    @Override
    public void run() {
       while (true) {
        try {
            sharedResource.produce();
            Thread.sleep(20);
        } catch (Exception e) {
            e.printStackTrace();
        } 
       }
    }
}
class Consumer extends Thread{
    private Resource sharedResource;
    public Consumer(Resource sharedResource){
        this.sharedResource=sharedResource;
    }
    @Override
    public void run() {
        while (true) {
            try {
                sharedResource.consume();
                Thread.sleep(40);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}