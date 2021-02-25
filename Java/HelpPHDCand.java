import java.util.Scanner;

public class HelpPHDCand {

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String tmp = "";
		final String SKIP = "P=NP";
		final int N = Integer.parseInt(sc.nextLine());
		//int[] results = new int[N];
		
		for(int i = 0;i < N;i++)
		{
			tmp = sc.nextLine();
			
			if(tmp.equals(SKIP))
				System.out.println("skipped");
			
			else
			{
				 System.out.println(Integer.parseInt(tmp.split("+")[0]) + Integer.parseInt(tmp.split("+")[1]));
			}
		}
		
		//for(int i = 0;i < N;i++)
		
		
		sc.close();

	}

}
