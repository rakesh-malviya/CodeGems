import java.util.concurrent.Semaphore;


public class Signaling {

	static Semaphore a1done = new Semaphore(0);
	
	static class myThread1 extends Thread{
		
		private void a1()
		{
			System.out.println();
			for(int i=0;i<10;i++)
			{
				System.out.print(" T1 "+i);
			}			
		}
		public void run(){
			a1();
			a1done.release();			
		}
	}
	
	static class myThread2 extends Thread{		
		
		private void b2()
		{
			System.out.println();
			for(int i=0;i<10;i++)
			{
				System.out.print(" T2 "+i);
			}
		}
		public void run(){

			try {
				a1done.acquire();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			b2();
						
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
