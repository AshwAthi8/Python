#include<stdio.h>
int main(int argc, char const *argv[])
{
	int n,i;
	printf("Enter the size of the array: ");
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++)s
	{
		scanf("%d",&a[i]);

	}
	int max_sum = -10000;
	int num2 = 0;

	for(i=0;i<n;i++)
	{
		num2 = num2 +a[i];
		if(max_sum<num2)
		{
			max_sum = num2;
		}
		if(num2<0){
			num2 =0;
		}
	}
	printf("this is max:%d\n", max_sum);


	return 0;
}