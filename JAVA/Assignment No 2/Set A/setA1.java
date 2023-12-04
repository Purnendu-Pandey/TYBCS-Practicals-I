//Assignment-2 SetA1
class setA1
{
 	int id=0;
 	String name=" ";
 	String dept="  ";
 	double salary=0;
 	
 	setA1(int id,String name,String dept,double salary)
 	{
 	  this.id=id;
  	  this.name=name;
  	  this.dept=dept;
  	  this.salary=salary;
 	}
 	void show()
 	{
  	  System.out.println("Enter Employee id :"+id);
  	  System.out.println("Enter Employee name :"+name);
  	  System.out.println("Enter Employee department :"+dept);
  	  System.out.println("Enter Employee salary :"+salary);
  	  System.out.println();
 	}
	public static void main(String args[])
	{
	   setA1 e1=new setA1(32,"Shobhit","MBA",82000);
	   setA1 e2=new setA1(44,"Sanklap","MCA",85000);
	   e1.show();	   
	   e2.show();
	}
}
/*
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 2$ javac setA1.java
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 2$ java setA1
Enter Employee id :32
Enter Employee name :Shobhit
Enter Employee department :MBA
Enter Employee salary :82000.0

Enter Employee id :44
Enter Employee name :Sanklap
Enter Employee department :MCA
Enter Employee salary :85000.0
*/
