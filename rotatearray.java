import java.io.*;
public class rotatearray
{
	public static void main(String args[])
	{
		int a[] = {3,1,2};
		int element = find_first(a);
		System.out.println(element);
	}
	public static int find_first(int nums[])
	{
		if (nums == null || nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
		int high = nums.length-1;
		int low = 0;
		while(low<high)
		{
			int mid = (high + low) /2;
			if(mid>0 && nums[mid]<nums[mid-1])
			{
				return nums[mid];
			}
			if(nums[mid]>=nums[low] && nums[mid]>nums[high])
			{
				low = mid+1;
			}
			else
			{
				high = mid-1;
			}

		}
		return nums[low];
	}
}