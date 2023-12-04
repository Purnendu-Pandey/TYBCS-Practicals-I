public class setC3
{
	public static void main(String[] args)
	{
			int numberOfTables=15;
			int maxmultiplier=10;
	
			for(int table=1;table<=numberOfTables;table++)
			{
	   		System.out.println("Multiplication table for "+table+":");
	   		for(int multiplier=1;multiplier<=maxmultiplier;multiplier++)
	   		{
	       		int result=table*multiplier;
	       		System.out.println(table+"X"+multiplier+"="+result);
	   		}
	   		System.out.println();
			}    
	}
}
/*
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 1$ javac setC3.java
ty32@pc38:~/TYBCS-32/JAVA/Assignment No 1$ java setC3
Multiplication table for 1:
1X1=1
1X2=2
1X3=3
1X4=4
1X5=5
1X6=6
1X7=7
1X8=8
1X9=9
1X10=10

Multiplication table for 2:
2X1=2
2X2=4
2X3=6
2X4=8
2X5=10
2X6=12
2X7=14
2X8=16
2X9=18
2X10=20

Multiplication table for 3:
3X1=3
3X2=6
3X3=9
3X4=12
3X5=15
3X6=18
3X7=21
3X8=24
3X9=27
3X10=30

Multiplication table for 4:
4X1=4
4X2=8
4X3=12
4X4=16
4X5=20
4X6=24
4X7=28
4X8=32
4X9=36
4X10=40

Multiplication table for 5:
5X1=5
5X2=10
5X3=15
5X4=20
5X5=25
5X6=30
5X7=35
5X8=40
5X9=45
5X10=50

Multiplication table for 6:
6X1=6
6X2=12
6X3=18
6X4=24
6X5=30
6X6=36
6X7=42
6X8=48
6X9=54
6X10=60

Multiplication table for 7:
7X1=7
7X2=14
7X3=21
7X4=28
7X5=35
7X6=42
7X7=49
7X8=56
7X9=63
7X10=70

Multiplication table for 8:
8X1=8
8X2=16
8X3=24
8X4=32
8X5=40
8X6=48
8X7=56
8X8=64
8X9=72
8X10=80

Multiplication table for 9:
9X1=9
9X2=18
9X3=27
9X4=36
9X5=45
9X6=54
9X7=63
9X8=72
9X9=81
9X10=90

Multiplication table for 10:
10X1=10
10X2=20
10X3=30
10X4=40
10X5=50
10X6=60
10X7=70
10X8=80
10X9=90
10X10=100

Multiplication table for 11:
11X1=11
11X2=22
11X3=33
11X4=44
11X5=55
11X6=66
11X7=77
11X8=88
11X9=99
11X10=110

Multiplication table for 12:
12X1=12
12X2=24
12X3=36
12X4=48
12X5=60
12X6=72
12X7=84
12X8=96
12X9=108
12X10=120

Multiplication table for 13:
13X1=13
13X2=26
13X3=39
13X4=52
13X5=65
13X6=78
13X7=91
13X8=104
13X9=117
13X10=130

Multiplication table for 14:
14X1=14
14X2=28
14X3=42
14X4=56
14X5=70
14X6=84
14X7=98
14X8=112
14X9=126
14X10=140

Multiplication table for 15:
15X1=15
15X2=30
15X3=45
15X4=60
15X5=75
15X6=90
15X7=105
15X8=120
15X9=135
15X10=150
*/
