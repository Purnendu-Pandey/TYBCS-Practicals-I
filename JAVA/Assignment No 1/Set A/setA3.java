import java.util.*;
class setA3
{
	static void cylinder()
	{
	    float r,h;
	    Scanner sc=new Scanner(System.in);
	    System.out.println("Enter radius of cylinder :");
	    r=sc.nextFloat();
	    System.out.println("Enter height of cylinder :");
	    h=sc.nextFloat();
	    System.out.println("Volume of cylinder =:"+3.142*r*r*h);
	}
	static void fact()
	{
	    int n,fact=1;
	    Scanner sc=new Scanner(System.in);
	    System.out.println("Enter the number :");
	    n=sc.nextInt();
	    for(int i=1;i<=n;i++)
	    {
	       fact=fact*i;
	    }
	    System.out.println("Factorial of "+n+" is :"+fact);
	}
	static void armstrong()
	{
	    int n,sum=0,num;
	    Scanner sc=new Scanner(System.in);
	    System.out.println("Enter the number :");
	    n=sc.nextInt();
	    int no=n;
	    while(n!=0)
	    {
	       num=n%10;
	       sum=sum+(num*num*num);
	       n=n/10;
	    }
	    if(sum==no)
	    {
	       System.out.println("Number"+ no +"is armstrong number");
	    }
	    else 
	       System.out.println("Number"+ no +"is not armstrong number");
	    }
	    
	public static void main(String a[])
	{
	    int ch=0;
	    Scanner sc=new Scanner(System.in);
	    while(ch<=3)
	    {
	    System.out.println("1.Volume of cylinder:");
	    System.out.println("2.Factorial of Number:");
	    System.out.println("3.Number is Armstrong or not:");
	    System.out.println("4.Exit:");
	    
	 System.out.println("Enter Your Choice:");
	 ch=sc.nextInt();
	 
	 switch(ch)
	 {
	    case 1:cylinder();
	           break;
	    case 2:fact();
	           break;
	    case 3:armstrong();
	           break;
	 }
       }
    }
}

/*
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 1$ javac setA3.java
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 1$ java setA3	       
1.Volume of cylinder:
2.Factorial of Number:
3.Number is Armstrong or not:
4.Exit:
Enter Your Choice:  1
Enter radius of cylinder : 7
Enter height of cylinder : 4
Volume of cylinder =:615.832

1.Volume of cylinder:
2.Factorial of Number:
3.Number is Armstrong or not:
4.Exit:
Enter Your Choice: 2
Enter the number :4
Factorial of 4 is :24

1.Volume of cylinder:
2.Factorial of Number:
3.Number is Armstrong or not:
4.Exit:
Enter Your Choice: 3
Enter the number :150
Number 150 is not armstrong number

1.Volume of cylinder:
2.Factorial of Number:
3.Number is Armstrong or not:
4.Exit:
Enter Your Choice: 3
Enter the number : 153
Number 153 is armstrong number

1.Volume of cylinder:
2.Factorial of Number:
3.Number is Armstrong or not:
4.Exit:
Enter Your Choice: 4
*/	    
	        
