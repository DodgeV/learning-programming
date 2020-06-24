* 编译型语言，先用`gcc`编译为`a.out`机器语言，再执行
> + 或`gcc XXX.c -o XXX`编译为自定义XXX文件，
> + 或`gcc XXX.c -shared -o XXX.so`编译为动态库以便其它语言调用
* C语言所有的库函数调用，只能保证语法一致，不能保证执行结果是一致的，同样的库函数在不同的操作系统下执行结果可能不同，Unix和Linux很多库函数都支持POSIX，代码互相移植代价小，但Windows支持的比较差，代码移植较麻烦
* 另外操作系统编码不一样也会造成乱码，Windows--gbk/gb2312/ANSI,linux--utf-8(unicode)
* C语言有32个关键字, 9个控制语句, 34种运算符
* C语言每一句可执行行代码都用`;`结尾，且必须放在代码块里面，所有`#`开头的行都代表预编译指令，可以不用`;`结尾
* C语言的注释有两种，行注释`//要写的注释`是C标准的注释方式，块注释`/*要写的注释*/`是从C++借鉴而来
* C语言由函数组成，有且只有一个main函数，且程序运行从main函数开始，main函数由系统自动调用，不用人为调用，其他函数的调用必须放在`{}`内部
* 使用某个函数`printf`前，需要包含对应头文件`#include <stdio.h>`，头文件类似于菜单，列举了菜名，函数调用相当于点菜，用`man 3 printf`可以查看头文件也可用`vi /usr/include/stdio.h`查看调用某个函数需要包含的头文件，`<>`包含系统标准的头文件，`""`包含自定义的头文件

```C
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // return 0，程序正常结束
    printf("Hello C++ World before system!\n");
    system("ls -lha");   //在已经运行的程序中，执行一个外部程序(命令)
    system("./a.out");
    
    return 0;
}
```
