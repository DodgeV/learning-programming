#include <stdio.h>

int main01()
{
	int a = 3;
	//a++;
	int b = ++a + a++;
	printf("a = %d, b= %d\n", a ,b );
	return 0;
}

int main03()
{
	int a = 2;
	int b = 3;
	int c = 4;
	int d = 5;
	int i = (c = b, c + d);
	printf("i = %d\n", i);
	return 0;
}

int main()
{
	int a = 3;
	int b = 2;
	double c = (double)a / b;//把a强制转化为double类型
	printf("%lf\n", c);
	return 0;
}


