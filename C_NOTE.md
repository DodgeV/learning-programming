* 编译型语言，先编译为机器语言，再执行
* C语言有32个关键字, 9个控制语句, 34种运算符
* C语言由函数组成，有且只有一个main函数，且程序运行从main函数开始，main函数由系统自动调用，不用人为调用
* 使用某个函数`printf`前，需要包含对应头文件`#include <stdio.h>`，头文件类似于菜单，列举了菜名，函数调用相当于点菜，用`vi /usr/include/stdio.h`查看调用某个函数需要包含的头文件，`<>`包含系统标准的头文件，`""`包含自定义的头文件

```C
#include <stdio.h>

int main()
{
    // return 0，程序正常结束
    printf("Hello C++ World\n");
    printf("Hello C world!");

    return 0;
}
```