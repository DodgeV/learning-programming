#include <stdio.h>

int main()
{
	int a;//定义一个变量，名字叫a
	int b;
	int c;
	
	a = 2;
	b = 3;
	c = a + b;
	
	/*
	__asm
	{
		mov a, 2//将2放到a里面
		mov b, 3
		mov eax, a//将a放到寄存器eax里面
		add eax, b//将b和eax加，加以后的结构放入eax
		mov c, eax//把eax的值放入c

	}
	*/
	printf("c = %d\n", c);
	return 0;
}