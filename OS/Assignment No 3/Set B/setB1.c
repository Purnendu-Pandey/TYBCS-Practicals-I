#include<stdio.h>
#include<stdlib.h>
void main()
{
     int i,n,j;
     printf("\n Enter number of processes : ");
     scanf("%d",&n);
     int at[n],bt[n],rt[n],ct,small,remain=0,time,temp;
     float avwt=0,avatat=0;  
     for (i=0;i<n;i++)
     { 
         printf("\n Enter arival time for process  %d:  ",i+1);
         scanf("%d",&at[i]);    
     }        
     for (i=0;i<n;i++)
     {
         printf("\n\n Enter burst time for processs %d: ",i+1);
         scanf("%d",&bt[i]);
         rt[i]=bt[i];
         
     }     
     printf("\n pro\tat\tbt\twt\ttat ");
     for (time=0;remain != n;time++)
     {
          for (i=0;i<n;i++)
          {
              if(at[i] <= time && rt[i])
                 small=i;
          }
          rt[small]--;
          if(rt[small]==0)
          {
            remain++;
            ct=time+1;
            printf("\n P%d\t%d\t%d\t%d\t%d ",small+1,at[small],bt[small],ct-bt[small]-at[small],ct-at[small]);
            avatat=avatat+ ct-at[small];
            avwt=avwt+ct-bt[small]-at[small];         
          }       
      }
      avwt/=n;
      avatat/=n;
      printf("\n Average waiting time : %f ",avwt);
      printf("\n Average turn around  time : %f \n",avatat);         
}
     
/*
ty32@pc38:~/TYBCS-32/OS/Assignment No 3$ cc setB1.c
ty32@pc38:~/TYBCS-32/OS/Assignment No 3$ ./a.out
Enter number of processes : 3
Enter arival time for process 1: 2
Enter arival time for process 2: 4
Enter arival time for process 3: 4
Enter burst time for processs 1: 4
Enter burst time for processs 2: 5
Enter burst time for processs 3: 1

pro    at      bt      wt      tat
P3     4       1       0       1
P2     4       5       1       6
P1     2       4       6       10
Average waiting time : 2.333333
Average turn around  time : 5.666667
*/