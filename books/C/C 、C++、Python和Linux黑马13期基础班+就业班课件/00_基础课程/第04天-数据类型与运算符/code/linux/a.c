#include <stdio.h>

#define MAX 100

int main()
{
	//MAX = 10;
	printf("%d\n", MAX);
	const int a = 100;
	a = 0;
	printf("a = %d\n", a);
	return 0;
}

