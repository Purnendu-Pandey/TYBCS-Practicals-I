#include<stdio.h>
struct times
{
	int p,art,but,wtt,tat,rnt;
};
void sortart(struct times a[],int pro)
{
	int i,j;
	struct times temp;
	for(i=0;i<pro;i++)
	{
	   for(j=i+1;j<pro;j++)
	   {
	     if(a[i].art>a[j].art)
	     {
	       temp=a[i];
	       a[i]=a[j];
	       a[j]=temp;
	     }
	   }
	}
	return;
}
int main()
{
	int i,j,pro,time,remain,flag=0,ts;
	struct times a[100];
	float avgwt=0,avgtt=0;
	printf("Round Roubin Scheduling Algorithm \n");
	printf("Enter the number of process :");
	scanf("%d",&pro);
	remain=pro;
	for(i=0;i<pro;i++)
	{
	   printf("Enter arrival time for process:",i+1);
  	   scanf("%d",&a[i].art);

  	   printf("Enter burst time for the process:");
  	   scanf("%d",&a[i].but);
  	   a[i].p=i;
  	   a[i].rnt=a[i].but;
  	}
  	sortart(a,pro);
  	printf("Enter time quantum :");
  	scanf("%d",&ts);
  	printf("\n-----------------------------------------\n");
  	printf("Gantt chart \n");
  	printf("0");
  	   
  	for(time=0,i=0;remain!=0;)
  	{
	   if(a[i].rnt<=ts && a[i].rnt>0)
	   {
	      time=time+a[i].rnt;
	      printf("->[p%d]<-%d",a[i].p,time);
	      a[i].rnt=0;
	      flag=1;
	   }
	   else if(a[i].rnt>0)
	   {
	      a[i].rnt=a[i].rnt-ts;
	      time=time+ts;
	      printf("-->[p%d]<--%d",a[i].p,time);
	   }
	   if(a[i].rnt==0 && flag==1)
	   {
	   	remain--;
	   	a[i].tat=time-a[i].art;
	   	a[i].wtt=time-a[i].art-a[i].but;
	   	avgwt=avgwt+time-a[i].art-a[i].but;
	   	avgtt=avgtt+time-a[i].art;
	   	flag=0;
	   }
	   if(i==pro-1)
	      i=0;
	      else if(a[i+1].art<=time)
	         i++;
	      else
	         i=0;  	   
       }
       printf("\n\n");
       printf("\n-----------------------------------------\n");
       printf("PID \tAT \tBT \tTAT \tWT \n");
       printf("\n-----------------------------------------\n");
       for(i=0;i<pro;i++)
       {
          printf("P%d\t%d\t%d\t%d\t%d\n",a[i].p,a[i].art,a[i].but,a[i].tat,a[i].wtt);
       }
       printf("\n-----------------------------------------\n");
       avgwt=avgwt/pro;
       avgtt=avgtt/pro;
       printf("Average Waiting Time :%2f\n",avgtt);
       printf("Average Turnaround Time :%2f\n",avgwt); 
}
/*
ty32@pc38:~/TYBCS-32/OS/Assignment No 3$ cc setC2.c
ty32@pc38:~/TYBCS-32/OS/Assignment No 3$ ./a.out
Round Roubin Scheduling Algorithm 
Enter the number of process :5
Enter arrival time for process:1
Enter burst time for the process:5
Enter arrival time for process:2
Enter burst time for the process:6
Enter arrival time for process:0
Enter burst time for the process:4
Enter arrival time for process:5
Enter burst time for the process:9
Enter arrival time for process:6
Enter burst time for the process:3
Enter time quantum :2

**********************************************
Gantt chart 
0-->[p2]<--2-->[p0]<--4-->[p1]<--6-->[p3]<--8-->[p4]<--10->[p2]<-12-->[p0]<--14-->[p1]<--16-->[p3]<--18->[p4]<-19->[p0]<-20->[p1]<-22-->[p3]<--24-->[p3]<--26->[p3]<-27

***************************************
PID      AT      BT      TAT     WT

***************************************
P2      0       4       12      8
P0      1       5       19      14
P1      2       6       20      14
P3      5       9       22      13
P4      6       3       13      10

***************************************
Average Waiting Time :17.200001
Average Turnaround Time :11.800000
*/
  	   
		
