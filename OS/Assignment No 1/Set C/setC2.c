#include<sys/types.h>
#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>  
int main(int args,char *argve[])
{
	pid_t pid=fork();
	if (pid < 0)
	{
	     printf("Forking Failed");
	     return 1;
	}
	else if(pid > 0)
	{
	    printf("\n I am Parent Process \n Parent Id = %d",getpid());
	    printf("\n I am Child Process \n Child Id = %d ",getpid());
	}
	return 0;
}
/*
output :-
ty32@pc38:~/TYBCS-32/OS/Assignment No 1$ ./a.out
I am Parent Process 
Parent Id = 15043 
I am Child Process 
Child Id = 15043
*/
