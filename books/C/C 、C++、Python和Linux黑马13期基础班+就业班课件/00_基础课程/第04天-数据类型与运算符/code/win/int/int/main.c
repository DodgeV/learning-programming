#include <stdio.h>

int main()
{
	int a = 0x12345678;
	printf("%p\n", &a);//将a的地址输出
	return 0;
}