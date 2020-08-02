#include <stdio.h>

int main()
{
	char a = 'a';//第一个a是一个char类型的变量名，第二个a是一个char的常量
	a = 'b';
	a = '1';
	//'a' = '1';//错误的，因为常量的值不能修改
	printf("%c\n", a);
	int len = sizeof(a);
	printf("%d\n", len);
	a = 'b';
	printf("%d\n", a);
	a = 100;
	printf("%c\n", a);
	a = 'A';
	printf("%d\n", a);
	a = 'A' + 32;
	printf("%c\n", a);
	a = 'd';
	a = a - 32;
	printf("%c\n", a);
	a = 32;
	printf("%c\n", a);
	a = 'a' - ' ';
	printf("%c\n", a);
	a = 'a';
	a = a + 1;
	printf("%c\n", a);
	a = 'a';
	printf("%c", a);
	a = 'b';
	printf("%c", a);
	//a = '\b';//退格键的转义字符
	a = '\t';
	printf("%c", a);
	a = 'c';
	printf("%c", a);
	a = '\n';
	printf("%c", a);
	a = 3.14;
	printf("%d\n", a);
	return 0;
}


