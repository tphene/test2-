import java.util.*;
public class parenthesis
{
	public static void main(String args[])
	{
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the parenthesis string to be checked");
		String par = sc.next();
		System.out.println(Check_parenthesis(par));
		
	}
	public static boolean Check_parenthesis(String par)
	{
		Stack<Character> s = new Stack<Character>();
		for(int i=0;i<par.length();i++)
		{
			if(par.charAt(i)=='(')
			{
				s.push(')');
			}
			else if(par.charAt(i)=='[')
			{
				s.push(']');
			}
			else if(par.charAt(i)=='{')
			{
				s.push('}');
			}
			else if(s.isEmpty()||s.pop()!=par.charAt(i))
			{
				return false;
			}
			

		}
		return s.isEmpty();
	}
}