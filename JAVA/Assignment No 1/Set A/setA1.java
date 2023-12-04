//Set-A1 from the above sample
public class setA1
{
	int num;
	public setA1()
	{
	   num=0;
	}
	public setA1(int name)
	{
	   this.num=num;
	}
	public static void main(String[]args)
	{
	   setA1 m1=new setA1();
	   if(args.length>0)
	   {
	      int n=Integer.parseInt(args[0]);
	      setA1 m2 = new setA1(n);
	      System.out.println(m1.num);
	      System.out.println(m2,num);
           }
	   else
	      System.out.println("Insufficient arguments");
	}
}
