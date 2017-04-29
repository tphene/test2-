import java.util.*;
public class binarysearch
{	
	static int iteration = 0;
	public static void main(String args[])
	{
		int a[] = {1,2,3,4,5,6,7,8,9,11,11,11,11,14,15,16,17};
		int t = 11;
		int index = binary_search(a,t);
		System.out.println(index);
		System.out.println(iteration);
	}
	public static int binary_search(int a[],int t)
	{
		int high = a.length-1;
		int low = 0;
		while(low <= high)
		{
			iteration++;
			int mid = (high+low)/2;
			if(a[mid]==t) return mid;
			if(a[mid]<t) low = mid+1;
			if(a[mid]>t) high = mid-1;
		}
		return (-1);
	}

}