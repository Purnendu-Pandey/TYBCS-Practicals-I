#include<stdio.h>
#include<sys/types.h>
void ChildProcess();
void ParentProcess();
int main()
{
	 pid_t pid;
	 pid=fork();
	 if (pid==0)
	    ChildProcess(pid);
	 else
	    if (pid>0)
	    ParentProcess(pid);
	 else
	    printf("unsuccessful");  
}
	 void ChildProcess(int pid)
	 { 
	    printf("\n Child");
	    printf("\n My ID : %d",getpid());
	    printf("\n My Parent Id :%d",getppid());
	 }
	 void ParentProcess(int pid)
	 {
	    printf("\n Parent ");
	    printf("\n My ID : %d",getpid());
	    printf("\n My Parent Id : %d\n",getppid());
	 }

/*
ty32@pc38:~/TYBCS-32/OS/Assignment No 1$ cc setA1.c
ty32@pc38:~/TYBCS-32/OS/Assignment No-1$ ./a.out

Parent 
My ID : 4930
My Parent Id :4819

Child
My ID : 4931
My Parent Id : 4930
*/
