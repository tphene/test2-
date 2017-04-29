import java.util.*;
public class excelcolumn
{
	public static void main(String args[])
	{
	Scanner sc = new Scanner(System.in);
	String input = "AZ";
	int result = convert_to_number(input);
	System.out.println(result);	
	}
	public static int convert_to_number(String input)
	{
		int result = 0;
		int power = 0;
		for(int i=input.length()-1;i>=0;i--)
		{
			int digit = (int)input.charAt(i)-64;
			result += digit*Math.pow(26,power++);
		}
		return result;
	}

}