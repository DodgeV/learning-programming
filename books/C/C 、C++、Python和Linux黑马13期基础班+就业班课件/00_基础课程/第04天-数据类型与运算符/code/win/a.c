#include <stdio.h>

int main()
{
	int a = 02572575257;//这个地方是用的八进制
	//printf("a = %d\n", a);//输出的时候是10进制
	a = 0x554410f5;

	printf("a = %d\n", a);
	int i = sizeof(a);//计算a的占用空间大小
	printf("i = %d\n", i);//i输出的结果是4，证明a是4个字节大小，就是一个DWORD
	a = 0x7fffffff;
	printf("a = %d\n", a);
	a = 2147483647 + 5;
	printf("a = %d\n", a);

	a = 0x7ffffffc;
	printf("%d\n", a);
	
	return 0;
}
