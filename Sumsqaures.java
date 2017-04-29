import java.io.*;
import java.util.*;
public class Sumsqaures
{
	public static void main(String args[])
	{
		int a[] = {1,2,3,4,5,6,7,7};
		HashSet hs = new HashSet();
		HashMap hm = new HashMap();
		Arrays.sort(a);
		for(int i=0;i<=Math.sqrt(2*a[a.length-1]);i++)
			hs.add(i*i);

		int count = 0;
		for(int i=0;i<a.length;i++)
		{
			if(!hm.containsKey(a[i]))
			{
				hm.put(a[i],1);
			}
			else
			{
				hm.put(a[i],((int)hm.get(a[i])+1));
			}
		}
		ArrayList<ArrayList<Integer>> alist = new ArrayList<ArrayList<Integer>>();
	}
}
