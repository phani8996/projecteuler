#include<stdio.h>

void main(){
	int i,count=0,n;
	printf("enter the upper limit");
	scanf("%d",&n);
	for (i=0;i<n;i++){
		if(i%3==0 || i%5==0){
			count+=i;
		}
	}
	printf("Sum of all multiples of 3,5 is %d\n",count);
	getchar();
}
