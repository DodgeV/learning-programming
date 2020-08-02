#include <stdio.h>

int main()
{
	int len = sizeof(int);
	printf("%d\n", len);
	len = sizeof(short);
	printf("%d\n", len);
	len = sizeof(long);
	printf("%d\n", len);
	len = sizeof(long long);
	printf("%d\n", len);
	int a = 0x7ffffffe;
	a = a + 10;
	printf("%d\n", a);
	unsigned int b = 0xfffffffe;
	b = b + 2;
	printf("%u\n", b);
	return 0;
}

