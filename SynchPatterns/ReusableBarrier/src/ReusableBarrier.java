
import java.util.concurrent.Semaphore;


public class ReusableBarrier {

	static int n = 3;
	static Semaphore mutex = new Semaphore(1);
	static Semaphore barrier = new Semaphore(0);
	static Semaphore barrier2 = new Semaphore(0);
	
	static int noOfthreads = 0;
	
	static class myThread1 extends Thread{
		private int tid;
		
		public myThread1(int tid) {
			this.tid = tid;
		}
		
		public void run(){
			
			try {
				
				//Another solution
				for(int i=0;i<6;i++)
				{					
					
					mutex.acquire();
						noOfthreads++;
						//System.out.println("Thread:"+tid+" done:"+i);//+ " no#:"+noOfthreads);
						System.out.print(" "+i);
						if(noOfthreads==n)
						{					
							barrier.release(n);					
						}
					mutex.release();
					
					barrier.acquire();
					
					mutex.acquire();
						noOfthreads--;	
						if(noOfthreads==0)
						{
							barrier2.release(n);
						}
					mutex.release();				
				
					barrier2.acquire();					
				}
				
				/* Another Solution
				for(int i=0;i<5;i++)
				{
					System.out.println("Thread:"+tid+" done:"+i);
					
					mutex.acquire();
						noOfthreads++;
						if(noOfthreads==n)
						{
							barrier2.acquire();
							barrier.release();						
						}
					mutex.release();
					
					barrier.acquire();
					barrier.release();
					
					mutex.acquire();
						noOfthreads--;
						if(noOfthreads==0)
						{
							barrier.acquire();
							barrier2.release();
						}
					mutex.release();
					
					barrier2.acquire();
					barrier2.release();
					
				}
				 */
				
				/*
				 * Not solution
				for(int i=0;i<5;i++)
				{
					System.out.println("Thread:"+tid+" done:"+i);
					
					mutex.acquire();
						noOfthreads++;						
					mutex.release();
					
					if(noOfthreads==n)
					{					
						barrier.release();						
					}
					
					barrier.acquire();
					barrier.release();
					
					mutex.acquire();
						noOfthreads--;						
					mutex.release();
					
					if(noOfthreads==0)
					{
						barrier.acquire();						
					}	
				}
				*/
				
				
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
			new myThread1(i+1).start();
		}
	}

}
