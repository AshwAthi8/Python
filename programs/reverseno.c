#include<stdio.h>
int revnum(int n);

int main(){
	int num;
	scanf("%d",&num);
	revnum(num);
	return 0;

}
int revnum(int n){
	if(n==0){
		return 0;
	}
	else{
		printf("%d",n%10);
		revnum(n/10);
		
}
}