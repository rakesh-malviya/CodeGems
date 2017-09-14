
import java.util.concurrent.Semaphore;


public class Mutex {

	static Semaphore a1done = new Semaphore(0);
	static Semaphore b1done = new Semaphore(0);
	static Semaphore mutex = new Semaphore(1);
	static int mid = 2;
	static int end = 4;
	static class myThread1 extends Thread{
		
		private void a1() throws InterruptedException
		{
			mutex.acquire();
			System.out.println();
			for(int i=0;i<mid;i++)
			{
				System.out.print(" a1 "+i);
			}
			mutex.release();
		}
		
		private void a2() throws InterruptedException
		{
			mutex.acquire();			
			System.out.println();
			for(int i=mid;i<end;i++)
			{
				System.out.print(" a2 "+i);
			}
			mutex.release();			
		}
		
		public void run(){
			
			try {				
				a1();
				
				a1done.release();
				b1done.acquire();
				
				a2();
				
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}			
		}
	}
	
	static class myThread2 extends Thread{		
		
		public void b1() throws InterruptedException
		{
			mutex.acquire();
			System.out.println();
			for(int i=0;i<mid;i++)
			{
				System.out.print(" b1 "+i);
			}
			mutex.release();
		}
		
		public void b2() throws InterruptedException
		{
			mutex.acquire();
			System.out.println();
			for(int i=mid;i<end;i++)
			{
				System.out.print(" b2 "+i);
			}
			mutex.release();
		}
		
		public void run(){
			
			try {
				b1();
				
				b1done.release();
				a1done.acquire();
				
				b2();				
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}			
		}
	}
	
	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub

		Thread t1 = new myThread1();
		t1.start();
		
		Thread t2 = new myThread2();
		t2.start();
		t2.sleep(50);
		t1.sleep(50);
	}

}

