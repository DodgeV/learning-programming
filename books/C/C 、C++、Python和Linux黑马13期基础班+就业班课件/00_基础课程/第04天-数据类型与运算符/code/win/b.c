#include <stdio.h>

int main()
{
	signed int a;//定义了一个有符号的int,省略的signed这个关键字，等于有符号
	a = 13;
	printf("a = %d\n", a);//用有符号的十进制方式输出
	printf("a = %o\n", a);//用有符号的八进制方式输出
	printf("a = %x\n", a);//用有符号的十六进制方式输出
	printf("a = %X\n", a);//用有符号的十六进制方式输出
	unsigned int b;//定义了一个无符号的int，最高位就不是符号位了
	b = 0;
	b = 0xffffffff;
	a = 0x7fffffff;
	a = 10;
	b = 100;
	printf("a = %u, b = %u\n", a, b);//同时输出a和b的值
	a = -5;
	printf("a = %u\n", a);//用无符号数输出一个负数
	b = a - 1;
	printf("b = %x\n", b);
	b = 0xfffffff5;
	a = b;
	printf("a = %d\n", a);
	a = -2;
	printf("%x\n", a);
	return 0;
}
