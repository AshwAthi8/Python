#include<stdio.h>
int int main(int argc, char const *argv[])
{
	int i,n,sum;
	
	scanf("%d",&n);
	int set[n];
	for (i=0;i<n;i++)
	{
		scanf("%d",&set[i]);
	}
	scanf("%d",&sum);

	int dp[n+1][sum+1];
	for(i=0;i<n+1;i++)
	{
		for(j=0;j<sum+1;j++)
		{
			if(j==0){
				dp[i][j]=1;
			}
			else if(i==0){
				dp[i][j]=0;
			}
			else
			{
				if(dp[i-1][j]==1){
					dp[i][j]=1;
				}
				else{
				if(i>=set[i] & (dp[i][(i-set[i])]==1)){
					{
						dp[i][j]=1;
				
					}
				else{
					dp[i][j]=-0;

				}

				}
			}
		}
	}
}
printf("\n");

for(i=0;i<n+1;i++){
	for(j=0;j<sum+1;j++)
	{
		printf("%d ", dp[i][j]);
	}
	printf("\n");
}

	return 0;
}