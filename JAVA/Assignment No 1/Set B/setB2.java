//Assignment-1 Set B2
import java.util.Scanner;
class MyNumber
{
	private int no;
  	MyNumber()
   	{
   	   no=0;
        }
        MyNumber(int no)
        {
          this.no=no;
        }
	void negative()
	{
          if(no<0)
          System.out.println(+no+ "is Negative");
  	}
	void Positive()
	{
          if(no>0)
          System.out.println(+no+ "Number is Positive");
   	}
	void Zero()
	{
  	  if(no==0)
  	  System.out.println(+no+ "Number is Zero");
   	}
 	void Odd()
 	{
  	  if(no%2!=0)
  	  System.out.println(+no+ "Number is Odd");
 	}
	void Even()
	{
 	   if(no%2==0)
 	   System.out.println(+no+ "Number is Even");
  	}
 
 	public static void main(String [] args) 
 	{
   		System.out.println("Enter the number ");
   		Scanner s=new Scanner(System.in);
   		int no=s.nextInt();
   		MyNumber m=new MyNumber(no);
  		m.Positive(); 
  		m.negative(); 		
  		m.Even();   		
  		m.Odd();
   		m.Zero();
   		
 }
}

/*
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 1$ gedit MyNumber.java
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 1$ javac MyNumber.java
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 1$ java MyNumber
Enter the number : 55
55 Number is Positive
55 Number is Odd

Enter the number : -2
-2 is Negative
-2 Number is Even

Enter the number : 0
0 Number is Even
0 Number is Zero

*/
