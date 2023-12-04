#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
void main()
{
	pid_t child_pid;
	child_pid=fork();
	if(child_pid<0)
	{
	  perror("fork error");
	  exit(1);
	}
	 else if(child_pid==0)
	 {
	    printf("\n Child Process");
	    printf("\n PID :%d",getpid());
	    printf("\n Parent PID :%d",getppid());
	    printf("\n Child process is sleeping For 5sec");
	    sleep(5);
	    printf("\n Child process is completed...");
	 }
	 else
	 {
	    printf("\n Parent Process");
	    printf("\n PID :%d\n",getpid());
	    printf("\n Parent PId :%d",getppid());
	    printf("\n Child process is Terminated...");
	 }
	 return 0;  
}

/*
ty32@pc38:~/TYBCS-32/OS/Assignment No 1$ cc setB2.c
ty32@pc38:~/TYBCS-32/OS/Assignment No-1$ ./a.out

Parent Process
PID :4737
Parent PId :4728
Child process is Terminated...
Child Process
PID :4738
Parent PId :4737
*/
