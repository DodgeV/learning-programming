#include <stdio.h>

int main()
{
	volatile int a = 10;
	a = a + 3;
	a = a + 2;
	a = a + 6;//编译器可能会优化这些代码
	printf("a = %d\n", a);
	register int a1;
	register int a2;
	register int a3;
	register int a4;
	register int a5;
	register int a6;
	register int a7;
	register int a8;
	return 0;
}

