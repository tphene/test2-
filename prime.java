import java.util.*;
public class prime
{
	static int n =23;
	static boolean not_Prime[] = new boolean[n+1];
	static int count = 0;
	public static void main(String args[])
	{
		//1 is neither prime nor composite
		count_prime();
		for(int i=2;i<=n;i++)
		{
			if(not_Prime[i]==false)
			System.out.println(i);
		}
	}
	public static void count_prime()
	{
		for(int i=2;i<=n;i++)
		{

			if(not_Prime[i]==false)
			{
				count++;
				for(int j=2;i*j<=n;j++)
				{
					not_Prime[i*j]=true;
				}
			}
		}
		return;
	}

}