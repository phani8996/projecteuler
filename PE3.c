/**********************************************************************
*This Code wont work for higher numbers								  *
*																	  *
***********************************************************************/

#include<stdio.h>

void main(){
	long unsigned int i=2,n,m;
	printf("enter the number");
	scanf("%d",&n);
	m=n;
	while(i*i<n){
	while(n%i==0){
		n/=i;
	}
		i+=1;
	}
	printf("Highest prime factor of %ul is %ul\n",m,n);
}
