
import java.util.concurrent.Semaphore;
import java.util.concurrent.Semaphore;


public class Rendezvous {

	static Semaphore a1done = new Semaphore(0);
	static Semaphore b1done = new Semaphore(0);
	static int mid = 2;
	static int end = 4;
	static class myThread1 extends Thread{
		
		private void a1()
		{
			System.out.println();
			for(int i=0;i<mid;i++)
			{
				System.out.print(" a1 "+i);
			}
		}
		
		private void a2()
		{
			System.out.println();
			for(int i=mid;i<end;i++)
			{
				System.out.print(" a2 "+i);
			}			
		}
		
		public void run(){
			
			try {
				a1();
				
				a1done.release();				
				b1done.acquire();
				
				a2();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}
	}
	
	static class myThread2 extends Thread{		
		
		public void b1()
		{
			System.out.println();
			for(int i=0;i<mid;i++)
			{
				System.out.print(" b1 "+i);
			}
		}
		
		public void b2()
		{
			System.out.println();
			for(int i=mid;i<end;i++)
			{
				System.out.print(" b2 "+i);
			}
		}
		
		public void run(){			
			
			try {
				
				b1();
				
				b1done.release();
				a1done.acquire();
				
				b1();
				
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
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

