#include<stdio.h>
int len(char str[]);
void dup(char str[],int n);

int main(){

	char a[100];
	scanf("%[^\n]s",a);
	int n = len(a);
	printf("Length of the array is %d\n",n);
	dup(a,n);
	return 0;

}
int len(char str[]){
	int c=0;
	while((str[c])!= '\0'){
		c++;
	}
	return c;

}

void dup(char str[],int n){

	int i,j,k =0;

	for(i =0;i<n-2;i++){
		//printf("Testing %c\n",str[i]);
		if(str[i]!=1)
		{
			for(j=i+1;j<n;j++){
			if(str[i]==str[j]){
				k=1;
				str[j]=1;
			}

		}
		if(k==1){
			printf("Duplicate found: %c\n",str[i]);
			k=0;
		}
	}
}

return;
}
