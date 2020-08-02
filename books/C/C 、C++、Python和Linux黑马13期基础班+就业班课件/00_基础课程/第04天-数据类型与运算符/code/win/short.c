#include <stdio.h>

int main()
{
	short a = 0;
	size_t len = sizeof(a);//得到a的大小
	printf("%u\n", len);
	int b = 0x7ffffffe;
	a = b;
	printf("%d\n", a);
	a = -2;
	b = a;//b还是-2的补码,c语言编译器会自动将2个字节的-2补码转化为4个字节的-2补码
	printf("%d\n", b);
	long c = 0;
	len = sizeof(c);
	printf("%u\n", len);
	len = sizeof(long long);
	printf("%u\n", len);
	c = 100;
	return 0;
}
