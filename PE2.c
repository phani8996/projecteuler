#include<stdio.h>

int fib(n){
	if(n==0 || n==1){
		return 1;
	}
	else 
		return fib(n-1)+fib(n-2);
}

void main(){
int i,n,count=0;
for(i=0;i<=100;i++){
	n=fib(i);
	if(n>1000000) break;
	if(n%2==0)
		count+=n;
}
printf("Sum of all even valued terms less than one million is %d\n",count);
}
