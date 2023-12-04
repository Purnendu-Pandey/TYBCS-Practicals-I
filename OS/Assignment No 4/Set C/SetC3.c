#include <stdio.h>
typedef struct
{
    int val;
    int freq;
    int time;
}page;
page frame[20];
int LFU(int f)
{
		int minf=frame[0].freq,pos=0,cnt=0;
		for(int i=1; i<f; i++)
		{
				if(minf>frame[i].freq)
				{
						minf=frame[i].freq;
						pos=i;
				}
		}
		int temp[20],s=0;
		for(int i=0; i<f; i++)
		{
				if(frame[i].freq==minf)
				{
						cnt++;
						temp[s]=i;
						s++;
				}
		}
		if(cnt==1)
		{
				return pos;
		}
		else if(cnt>1)
		{
				int mint=99;
				for(int i=0; i<s; i++)
				{
					int j=temp[i];
					if(mint>frame[j].time)
					{
							mint=frame[j].time;
							pos=j;
					}
				}
		}
		return pos;
}
int main()
{
    int n,f,rs[100],fault=0,pos=0,hit=0,rear=0;

    printf("Enter Size of Reference String: ");
    scanf("%d",&n);
    
		printf("Enter Reference String: ");
    for (int i=0;i<n;i++)
    {
        scanf("%d",&rs[i]);
    }

    printf("Enter Frame Size: ");
    scanf("%d", &f);
    for (int i=0;i<f;i++)
    {
        frame[i].val=-1;
        frame[i].freq=0;
        frame[i].time=0;
    }

    for (int i=0;i<n;i++)
    {
    		int flag1=0;
    		for(int j=0; j<f; j++)
    		{
    				if(frame[j].val==rs[i])
    				{
    						flag1=1;
    						frame[j].freq++;
    						hit++;
    						break;
    				}
    		}
    if(flag1==0)
    {
    	 	pos=LFU(f);
     		frame[pos].val=rs[i];
     		frame[pos].freq=1;
     		frame[pos].time=i+1;
     		fault++;	
    }
        printf("\n");
        for (int j=0;j<f;j++)
        {
            printf("%d\t",frame[j].val);
        }
    }
    printf("\n No of Page Faults: %d\n ",fault);
		prinf("\n No of Page Hits: %d\n",hit);

    return 0;
}