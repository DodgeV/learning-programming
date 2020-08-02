#include <stdio.h>

int main()
{
	putchar(100);
	putchar('a');
	putchar('h');
	putchar('e');
	putchar('\n');
	printf("hello\n");
	short a = 10;
	printf("%hd\n", a);
	printf("%s + %s\n", "aaaaa", "bbbbb");
	printf("%p\n", &a);//&a取变量a的地址
	printf("%%d\n");
	unsigned long b = 10;
	printf("%lu\n", b);
	int a1 = 32;
	printf("a1 = '%-06d'\n", a1);
	return 0;
}

