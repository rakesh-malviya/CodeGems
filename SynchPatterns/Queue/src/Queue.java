
import java.util.Random;
import java.util.concurrent.Semaphore;


public class Queue {

	static Semaphore leaderSema = new Semaphore(0);
	static Semaphore followerSema = new Semaphore(0);
	static Semaphore rendezvous = new Semaphore(0);
	static Semaphore mutex = new Semaphore(1);
	
	static int leaderCnt = 0;
	static int followerCnt = 0;
	
	static class Leader extends Thread{
		
		private int id;
		
		public Leader(int id) {
			this.id = id;
		}
		
		public void dance()
		{
			System.out.printf("Leader id:%d dancing\n",id);
		}
		
		public void run(){
			
			try {
				mutex.acquire();
				
				if(followerCnt > 0)
				{
					followerCnt--;
					followerSema.release();
				}
				else
				{
					leaderCnt++;
					mutex.release();
					leaderSema.acquire();
				}
				
				dance();
				rendezvous.acquire();
				mutex.release();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}
	}

	static class Follower extends Thread{
		
		private int id;
		
		public Follower(int id) {
			this.id = id;
		}
		
		public void dance()
		{			
			System.out.printf("Follower id:%d dancing\n",id);
		}
		
		public void run(){
			
			try {
				mutex.acquire();
				if(leaderCnt > 0)
				{
					leaderCnt--;
					leaderSema.release();
				}
				else
				{
					followerCnt++;
					mutex.release();
					followerSema.acquire();
				}
				
				dance();
				rendezvous.release();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}
	}

	
	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub
		int count =10;
		Random r = new Random();
		
		while(count>0)
		{			
			if(r.nextInt()%2==0)
			{
				new Leader(count).start();
			}
			else
			{
				new Follower(count).start();
			}
			count--;
		}
	}

}

