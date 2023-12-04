#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
void main()
{
     int pid,r;
     pid=fork();
     for (int i=1;;i++)
     {
        if (pid==0)
        {
           r=nice(-20);
           printf("Child gets higher CPU priority %d \n",r);
           sleep(4);
           
        }
        else
        {
           r=nice(19);
           printf("Parent gets higher CPU priority %d \n",r);
           sleep(4);
        }
     }
}
/*
ty32@pc38:~/TYBCS-32/OS/Assignment No 1$ cc setA2.c
ty32@pc38:~/TYBCS-32/OS/Assignment No 1$ ./a.out
Parent gets higher CPU priority 19 
Child gets higher CPU priority -1 
Parent gets higher CPU priority 19 
Child gets higher CPU priority -1 
Child gets higher CPU priority -1 
Parent gets higher CPU priority 19 
Child gets higher CPU priority -1 
Parent gets higher CPU priority 19 

and the process will contine....
*/

