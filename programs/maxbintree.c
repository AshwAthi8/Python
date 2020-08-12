#include<stdio.h>
int main()
{
	int n; 
	scanf("%d",&n);
	int heap[n];
	int i,x,temp =0;
	while(i<n)
	{
		scanf("%d",&x);
		heap[i]=x;
		a = i;
		k = (a-1)/2

		while(a!=0 & heap[a]>heap[k])
		{	temp = heap[a];
			heap[a]=heap[k];
			heap[k]=temp;
			a=k;
			k=(a-1)/2;
		}
	i++;
	}
	for(i=0;i<n;i++)
	{
		print("%d",heap[i]);
	}

	return 0;
}