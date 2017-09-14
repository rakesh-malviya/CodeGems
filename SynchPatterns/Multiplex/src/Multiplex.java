
import java.util.concurrent.Semaphore;


public class Multiplex {

	static int n = 5;
	static Semaphore multiplex = new Semaphore(n);
	
	static int noOfthreads = 0;
	
	static class myThread1 extends Thread{
		private String name;
		
		public myThread1(String name) {
			this.name = name;
		}
		
		private void criticalSection() throws InterruptedException
		{
			noOfthreads++;
			System.out.println(name + " enter, No of threads: "+noOfthreads);
			Thread.sleep(1000);
			System.out.println(name + " exit,  No of threads: "+noOfthreads);
			noOfthreads--;
		}
		
		public void run(){
			
			try {				
				
				multiplex.acquire();
				
				criticalSection();
				
				multiplex.release();
				
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}			
		}
	}
	
	
	
	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub

		for(int i = 0;i<20;i++)
		{
			new myThread1("Thread "+(i+1)).start();
		}
	}

}


