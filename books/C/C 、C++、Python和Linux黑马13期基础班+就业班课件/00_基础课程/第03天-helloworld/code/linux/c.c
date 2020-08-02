#include <stdio.h>

int main()
{
	int a;//定义了一个变量，名字叫a
	a = system("ls -l");//执行system函数，同时得到函数的返回值,并且把返回值赋值给a
	printf("a = %d\n", a);//通过printf函数输入a的值

	a = system("ps -aux");
	printf("a = %d\n", a);
	a = system("a");
	printf("a = %d\n", a);
	return 0;
}

