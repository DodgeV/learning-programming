#include <stdio.h>

int main()
{
	int a1;//定义了一个变量，名字叫a
	extern int b;//声明了一个变量，名字叫b
	int a2;
	int a3;
	//int 4a;错误的名字
	int A1;//虽然语法没有问题，但变量一般习惯用小写字母
	int a_1;
	int a__2;
	int _a;
	int __a;
	int a___;
	int _;
	int __;
	int ___;
	//int a2;
	//int 你好;
	/*
	你好，今天不错
	上午吃了20个大包子，没便便
	中午再吃30个，
	还没便便
	*/
	//打印一个字符串 “hello world”
	printf("hello\n world");
	;//空语句
	;
	;
	{
		printf("哈哈\n");
	}
	{
		;
	}
	//return 0;//告诉调用者，程序执行成功
	return 100;
}


