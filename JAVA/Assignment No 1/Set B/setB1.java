import java.text.SimpleDateFormat;
import java.util.Date;
class setB1
{
	public static void main(String[] args)
	{
	    Date currentDate=new Date();
	    SimpleDateFormat s1=new SimpleDateFormat("dd/mm/yyyy");
	    System.out.println("Current date is "+s1.format(currentDate));
	    
	    SimpleDateFormat s2=new SimpleDateFormat("mm/dd/yyyy");
	    System.out.println("Current date is "+s2.format(currentDate));
	    
	    SimpleDateFormat s3=new SimpleDateFormat("EEEEEE MMMM dd yyyy");
	    System.out.println("Current date is "+s3.format(currentDate));
	    
	    SimpleDateFormat s4=new SimpleDateFormat("E MMMM dd HH:mm:ss z yyyy");
	    System.out.println("Current date and time is "+s4.format(currentDate));
	    
	    SimpleDateFormat s5=new SimpleDateFormat("dd/mm/yyyy HH:mm:ss a Z");
	    System.out.println("Current date and time is "+s5.format(currentDate));
	    
	    SimpleDateFormat s6=new SimpleDateFormat("HH:mm:ss");
	    System.out.println("Current time is "+s6.format(currentDate));
	    
	    SimpleDateFormat s7=new SimpleDateFormat("w");
	    System.out.println("Current week of year is "+s7.format(currentDate));
	    
	    SimpleDateFormat s8=new SimpleDateFormat("W");
	    System.out.println("Current week of month is "+s8.format(currentDate));
	    
	    SimpleDateFormat s9=new SimpleDateFormat("D");
	    System.out.println("Current day of the year is "+s9.format(currentDate));
    }
}

/*
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 1$ javac setB1.java
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 1$ java setB1
Current date is- 18/08/2023
Current date is- 08/18/2023
Current date is- Friday August 18 2023
Current date and time is- Fri August 18 15:08:48 IST 2023
Current date and time is- 18/08/2023 15:08:48 pm +0530
Current time is- 15:08:48
Current week of year is- 33
Current week of month is- 3
Current daye of the year is- 230
*/

