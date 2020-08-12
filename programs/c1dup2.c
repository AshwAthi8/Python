//This is finding the duplicate using hashmap

#include<stdio.h>
int main(){
	char str[100];
	int i;
	scanf("%[^\n]",str);
	int ar[26] = {0};
	for (i=0;str[i]!='\0';i++){
		ar[str[i]-'a']++;
	}
	for(i=0;i<26;i++){
		if(ar[i]>1){
			printf("Duplicate found %c\n",(i+97));
		}
	}
	return 0;
}