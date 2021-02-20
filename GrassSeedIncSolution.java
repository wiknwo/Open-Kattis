import java.util.Scanner;

public class GrassSeedIncSolution 
{
	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub

		//I/O
		Scanner sc = new Scanner(System.in);
		
		//Variables to solve problem
		double costOfSeed = sc.nextDouble(), width = 0.0, length = 0.0, totalCost = 0.0;
		int numLawns = sc.nextInt();
		
		for(int i = 1;i <= numLawns;i++)
		{
			width = sc.nextDouble();
			length = sc.nextDouble();
			totalCost += width * length;
		}			
		
		totalCost *= costOfSeed; 
		sc.close();

		System.out.println(totalCost);
	}

}
