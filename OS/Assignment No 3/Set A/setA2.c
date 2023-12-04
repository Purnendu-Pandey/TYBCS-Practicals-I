#include<stdio.h>
#include<stdlib.h>
void main()
{
     int i,n;
     float avwt=0,avgtat=0;
     printf("Enter no of process : \n");
     scanf("%d",&n);
     int p[n],at[n],bt[n],wt[n],tat[n];
     for (i=0;i<n;i++)
          p[i]=i;
     printf("enter arrival time : \n");
     for (i=0;i<n;i++)
         scanf("%d",&at[i]);
     printf("enter burst time : \n");
     for (i=0;i<n;i++)
         scanf("%d",&bt[i]);
     int temp,j;       
     
     
     for (i=1;i<n;i++)
     {   for (j=i+1;j<n;j++)
        {
          if(bt[i]>bt[j])
          {
             temp=bt[i];
             bt[i]=bt[j];
             bt[j]=temp;
             
             temp=p[i];
             p[i]=p[j];
             p[j]=temp;
             
             temp=at[i];
             at[i]=at[j];
             at[j]=temp;
 
          }
       }  
       } 
       int start[10];
       start[0]=0;
       for(i=1;i<n+1;i++)
       {
          start[i]=start[i-1]+bt[i-1];
          printf("\t %d",start[i]); 
       }   
       for(i=0;i<n;i++)
       {
          wt[i]=start[i]-at[i];         
          avwt+=wt[i];
          tat[i]=wt[i]+bt[i];
          avgtat+=tat[i];
       }
      avwt/=n;
      avgtat/=n;
      printf("\nPro \tAt\tBt\twt\ttat\n");
      for (i=0;i<n;i++)
          printf("\nP%d\t%d\t%d\t%d\t%d\n",p[i],at[i],bt[i],wt[i],tat[i]);
      printf("Avg waiting time : %f\nAvg TurnAround time : %f\n",avwt,avgtat);    
}
/*
ty32@pc38:~/TYBCS-32/OS/Assignment No 3$ cc setA2.c
ty32@pc38:~/TYBCS-32/OS/Assignment No 3$ ./a.out
Enter no of process : 
4
enter arrival time : 
0
1
2
3
enter burst time : 
4
1
2
1
Pro     At      Bt      wt      tat
P0      0       4       0       4
P1      1       1       3       4
P3      3       1       2       3
P2      2       2       4       6
Avg waiting time : 2.250000
Avg TurnAround time : 4.250000
*/


