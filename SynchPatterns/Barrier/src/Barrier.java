
import java.util.concurrent.Semaphore;


public class Barrier {

	static int n = 5;
	static Semaphore mutex = new Semaphore(1);
	static Semaphore barrier = new Semaphore(0);
	
	static int noOfthreads = 0;
	
	static class myThread1 extends Thread{
		private String name;
		
		public myThread1(String name) {
			this.name = name;
		}
		
		private void a1()
		{
			System.out.println(name+" a1 done");
		}
		
		private void a2()
		{
			System.out.println(name+" a2 done");
		}
		
		public void run(){
			
			try {
				
				a1();
				
				mutex.acquire();
				noOfthreads++;			
				mutex.release();
				
				if(noOfthreads==n)
					barrier.release();
				
				barrier.acquire();
				barrier.release();
				
				a2();
				noOfthreads--;
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}			
		}
	}
	
	
	
	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub

		for(int i=0;i<n;i++)
		{
			new myThread1("Thread "+(i+1)).start();
		}
	}

}


