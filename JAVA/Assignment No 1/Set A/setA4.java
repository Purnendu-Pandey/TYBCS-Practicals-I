import java.util.Scanner;
public class setA4
{
	public static void main(String[] args)
	{
	    Scanner sc=new Scanner(System.in);
	    System.out.println("Enter The size of elements :");
	    int n=sc.nextInt();
	    int[] array=new int[n];
	    System.out.println("Enter the array element:");
	    for(int i=0;i<n;i++)
	    {
	        array[i]=sc.nextInt();
	    
	    }	   
	    System.out.println("reverse order is :");
	    for(int i=n-1;i>=0;i--)
	    {
	    System.out.println(array[i]);
	    }
	    sc.close();
	}
}
/*
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 1$ javac setA4.java
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 1$ java setA4
Enter The size of elements :
5
Enter the array element:
4
9
5
1
3
reverse order is :
3
1
5
9
4
*/
