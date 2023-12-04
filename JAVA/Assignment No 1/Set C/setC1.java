//AssignmentNo-1 setC1
import java.util.Scanner;
public class setC1
{
	public static void main(String[] args)
	{
				Scanner scanner=new Scanner(System.in);
				System.out.println("Enter The Number Of Country:");
				int n=scanner.nextInt();
				scanner.nextLine();
	
				String[]names=new String[n];	
				for(int i=0;i<n;i++)
				{
	   				System.out.println("Enter The Number "+(i+1)+":");
	   				names[i]=scanner.nextLine();
				}
				
				for(int i=0;i<n-1;i++)
				{
	   				for(int j=i+1;j<n;j++)
	   				{
	     					if(names[i].compareTo(names[j])<0)
	     					{
	        					String temp=names[i];
	       						names[i]=names[j];
	        					names[j]=temp;
	     					}
	   				}
				}
				System.out.println("Names in descending order:");
        for(int i=0;i<n;i++)
        {
           System.out.println(names[i]);
				}
				scanner.close();
	}
}
/*
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 1$ javac setC1.java
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 1$ java setC1
Enter The Number Of Country:
5
Enter The Number 1:
india
Enter The Number 2:
japan
Enter The Number 3:
france
Enter The Number 4:
nepal
Enter The Number 5:
china
Names in descending order:
nepal
japan
india
france
china
*/
