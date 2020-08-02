#include <stdio.h>

int main01()
{
	char a = getchar();//从标准输入设备读取一个char
	printf("%d\n", a);
	return 0;
}

int main02()
{
	int a = 0;
	int b = 0;
	scanf("%d", &a);//通过标准输入设备输入一个整数，赋值给变量a
	scanf("%d", &b);
	printf("a = %d, b = %d, a + b = %d\n", a, b, a + b);
	float c = 0;
	scanf("%f", &c);
	printf("c = %f\n", c);
	return 0;
}

int main()
{
	int a = 20 % 7;
	printf("%d\n", a);
	return 0;
}

