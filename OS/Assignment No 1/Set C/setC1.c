#include<sys/types.h>
#include<stdio.h>
#include<unistd.h>
//#include<sys/wait.h>
#define max 100
void bubblesort(int arr[],int n)
{
      int i,j,temp;
      for(i=0;i<n;i++)
        for(j=0;j<n-1;j++)
            if (arr[j]>arr[j+1])
            {
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
}
int main(int argc,char *argv[])
{
        int n,i,arr[max];
        printf("Enter the size of array element :");
        scanf("%d",&n);
        printf("Enter the elements in array :");
        for(i=0;i<n;i++)
            scanf("%d",&arr[i]);
            pid_t pid=fork();

            if (pid < 0)
            {
                printf("Forking Faild");
                return 1;
            }
            else if(pid==0)
            {
              sleep(5);
              execv("./ex2",argv);
            }
            else
            { 
                  wait(NULL);
                  bubblesort(arr,n);
                  printf("\n Sorted Element using bubble sort by process :");
                  for (int i=0;i<n;i++)
                      printf("%5d",arr[i]);
                  printf("\n");
            }
            return 0;
}

