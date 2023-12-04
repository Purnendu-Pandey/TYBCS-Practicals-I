//sample program
#include<stdio.h>
#include<sys/types.h>
void ChildProcess();
void ParentProcess();
int main()
{
	 pid_t pid;
	 pid=fork();
	 if (pid==0)
	    ChildProcess();
	 else 
	     ParentProcess();
	 return 0;
}
	 void ChildProcess()
	 {
	    printf("\n I am a child process..\n");
	 }
	 void ParentProcess()
	 {
	     printf("\n I am parent process..\n");
	 }
