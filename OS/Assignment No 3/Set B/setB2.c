#include<stdio.h>
#include<stdlib.h>
#define max 10
typedef struct process
{ 
    int pid,cpu_bt,pri,tat,wt,at;
}process;
void swap (process *a,process *b)
{
    process temp = * a;
    *a = *b ;
    *b = temp;
} 
void sort(process pro[],int n)
{ 
    for (int i=0;i<n-1;i++)
    {
        for (int j=0;j<n-i-1;j++)
        {
            if (pro[j].pri > pro[j+1].pri)
                swap(&pro[j],&pro[j+1]);
        }
    }
}  
void calculate_tat(process pro[],int n)
{
    int total_wt = 0,ttat=0;
    for (int i=0;i<n;i++)
    {
        pro[i].tat=pro[i].wt+pro[i].cpu_bt;
        total_wt+=pro[i].wt;
        ttat+=pro[i].tat;
    }
    double avwt = (double)total_wt/n;
    printf("\nAverage Waiting Time : %2f\n",avwt);
    printf("\nAverage TurnAroundTime : %2f\n",ttat);
}   
void calculate_wt(process pro[],int n)
{
    pro[0].wt=0;
    for (int i=1;i<n;i++)
        pro[i].wt=pro[i-1].wt+pro[i-1].cpu_bt;
}
void main()
{
    int n;
    process pro[max];
     
    printf("\n Enter The No of Processes :");
    scanf("%d",&n);
    for (int i=0;i<n;i++)
        pro[i].pid=i+1;
    printf("\n Enter priority of process :");
        for (int i=0;i<n;i++)
            scanf("%d",&pro[i].pri);
      
    printf("enter arrival time of process :");
        for (int i=0;i<n;i++)
            scanf("%d",&pro[i].at);
    printf("enter burst time of process : ");
        for (int i=0;i<n;i++)
            scanf("%d",&pro[i].cpu_bt);
      
    sort(pro,n);
    calculate_wt(pro,n);
    calculate_tat(pro,n);
    printf("\n------GANTT CHART------\n");
    for (int i=0;i<n;i++) 
    {
        printf("P--->%d\t",pro[i].pid);
    }
    printf("\n");
      
    printf("\nPro\tAT\tBT\tPrio\tTAT\t WT\n");
    printf("------------------------------------------------");
    for (int i=0;i<n;i++)
        printf("\nP[%d]\t %d\t %d\t %d\t %d\t %d\n",i+1,pro[i].at,pro[i].cpu_bt,pro[i].pri,pro[i].tat,pro[i].wt);
        printf("----------------------------------------------");  
}

/*
ty32@pc38:~/TYBCS-32/OS/Assignment No 3$ cc setB2.c
ty32@pc38:~/TYBCS-32/OS/Assignment No 3$ ./a.out
Enter The No of Processes :
5
enter priority of process :
3
2
4
1
6
enter arrival time of process :
0
1
2
3
4
enter burst time of process :
7
6
3
5
4

Average Waiting Time : 11.000000
Average Turnaround Time : 11.000000

------GANTT CHART------
P--->4  P--->2  P--->1  P--->3  P--->5

Pro     AT      BT      Prio    TAT      WT
--------------------------------------------
P[1]     3       5       1       5       0
P[2]     1       6       2       11      5
P[3]     0       7       3       18      11
P[4]     2       3       4       21      18
P[5]     4       4       6       25      21
-------------------------------------------
*/