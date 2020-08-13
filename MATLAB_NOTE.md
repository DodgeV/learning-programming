## 基本知识
* 布局里面的默认，回到软件最初的样子
* 预设，里面设置字体大小
* 新建脚本，打开编辑器，写入脚本，右键点执行所选内容
* 将编辑器点住拖开，再点右上角倒三角停靠

* `%%`分隔开代码块 再按`ctrl+Enter`执行所选内容 注释以`%`开头
* `clc`清空历史
* 如果有`function`而没有参数或没有`function`直接`ctrl+Enter`运行
* 如果有参数运行出错后 输入函数名再传入参数调用该函数
* `doc` + 函数名 查看该函数的帮助
* 语句末尾无`;`则输出该句执行结果 末尾有`;`则只执行不输出
* 一行写不开，用`...`续行

* 工具箱(Toolbox) (分为功能性和学习型)
* 搜索在命令窗口输入一条命令的搜索过程:是否变量、是否函数、是否当前目录下的M文件、是否搜索路径下的其他M文件
* 设置方法:`path`输出所有的搜索路径,`help path`查看path的用法
* `cd`返回当前工作目录,`userpath`返回当前工作目录 
* `userpath()`后加更改的打开默认文件夹,`savepath`保存更改
* `pathtool`打开path工具箱 添减搜索路径

* 变量命名:字母开头，包括字母、数字、下划线，区分大小写,不用声明，拿来即用
* 赋值有两种 变量=表达式 或者 直接写表达式赋值给默认变量`ans`
* `who`显示所有的变量名 `whos` 显示变量名和对应值
* `clear`清除所有变量 后可以加指定变量
* `save`文件名 变量名 -append 
* `load`加文件名 导入文件
* `format`后加格式符 控制数据的输出格式默认`short` 不影响存储 [详见此博客](https://blog.csdn.net/xuxinrk/article/details/83012624)

## 15种基本的数据结构
### 数值类型非为整数和浮点数
> * 单精度浮点型4个字节 single 双精度浮点型8个字节 double
+ `a = 1.2`MATLAB将所有变量均存成double的形
+ `b = single(a)`
+ `d1 = [realmin('single') realmax('single')]`找到单精度的值的范围

> * 8种整型数据 带符号整型(int8 int16 int32 int64)和无符号整型(uint8 uint16 uint32 uint64)
+ `class(a)`查看a的类型
+ `a = uint8(a)`a转换为uint8类型
+ `a = double(a)`a转换为double型精度
+ `round`向最接近的整数取整，如果小数为0.5，则取绝对值大的整数`a1 = round(-2.4)`
+ `fix`向0取整`b1 = fix(-3.6)``b2 = fix(-3.5)`
+ `floor`不大于该数的最接近整数`c1 = floor(4.9)``c2 = floor(-4.2)`
+ `ceil`不小于该数的最接近整数`d1 = ceil(4.2)``d2 = ceil(-4.4)`

> * 复数 对实数的扩展
* 可以直接赋值`z = 3 + 4i`也可用j表示虚部的单位
* 也可用`a = complex(2:3,3:4)`得行向量 [2+3i 3+4i]
* `real(z)`得到复数z的实部
* `imag(z)`得到z的虚部
* `abs(z)`得到z的模
* `angle(z)`得到z的角度
* `conj(z)`得到z的共轭复数

### 逻辑型 logical
* `a = complex(2:3,3:4);a = logical(a)` 非0全转换为真 0全部转换为假
+ `a1 = true`赋值逻辑真 用1表示
+ `a2 = false`赋值逻辑假 用0表示
+ `a3 = true(3,4)`3行4列全为逻辑真
+ `a4 = false(3)`3行3列全为逻辑真

### 单元数组型 cell
单元数组中的每个元素都以单元的形式存在，可以是任意类型
+ `c = {'中国','China';[1 2 3],100}`可以用大括号创建单元数组 同行用`,`隔开 不同行用`;`隔开
+ `c{2,2} = []`访问但数组第2行第2列元素并将之改为空值
+ cell 也可用函数创建单元数组

### 函数句柄型 function_handle
+ `fhandle = @cos`创建余弦的函数句柄 之后可以通过函数句柄fhandle间接调用余弦函数
+ `func2str(fhandle)`将函数句柄转换为字符串
+ `str2func(str)`将字符串转换为函数句柄
+ `functions(fhandle)`返回包含函数信息的结构体变量
+ `isa(a,'function_handle')`判断是否为函数句柄
+ `isequal(fhandle1,fhandle2)`检测两个函数句柄是否对应同一函数

### 字符串 char 用单引号括起来
* `double(a)`获得a的ascii码
* `double('a')`获得'a'的ascii码
* `abs('a')`获得'a'的ascii码
* `char(99)`获得数字对应的字符串
* `str2num`输出变量名对应的数值`num2str`输出数值对应的变量名
* `input_str = input('请输入一个命令:')`
* `print(eval('input_str'))` 将字符串作为语句来执行,最好不要直接转换input的结果,防止外部操作内部比如`__import__("os").system("rm XX")`

### 结构体 struct
* 结构体.成员名 = 表达式
* isstruct 判断是否为结构体 是则返回1 否返回0
* fieldnames 返回该结构体包含的所有成员名
* isfield+结构体名+成员名 判断成员名是否属于该结构体 是则返回1
* rmfield 删除成员
* getfield 获得某个成员
* 单元 a={1,'str',[11 12]} 里面的元素可以是数值或字符或矩阵

### 矩阵 40%
* 直接输入法建立矩阵：用中括号包括所有元素，同行元素用空格或`,`隔开，不同行用`;`或者回车进行间隔
* M文件建立矩阵:鼠标启动编辑器或输入edit命令 语法同直接输入法 可以在一个文件中建立多个矩阵 输入文件名执行文件
* 特殊矩阵的建立:
> * `zeros(4,5)`建立4行5列零矩阵 
> * `ones(3,4)`建立3行4列全为1的幺矩阵
> * 单位矩阵
> * 随机矩阵
> * 魔方矩阵
> * Hilbert矩阵
> * Toeplitz矩阵
> * `a:b:c`建立以a开头c结尾步长为b的行向量 
> * `linspace(1,5,3)`建立1开头5结尾的3个元素的行向量
* 索引矩阵：
> * 用行列标或矩阵元素位置，(从1开始)`A(2,3)`表示A中第2行第3列的元素,
> * 用序号索引
> * 序号和下标转换
* 重排矩阵：
* 矩阵转置：
* 矩阵拆分：
* 直接赋值修改矩阵的值
* 删除矩阵：可以用赋空值的方式
* 扩展矩阵：
* 压缩矩阵：
```Matlab
clear;clc;close all;
a = zeros(3,3)
b = zeros(3)  %也是3行3列的矩阵
a * b     %执行矩阵的标准乘法
A = [1 2 3]
B = [4 5 6]
A .* B    %点乘，对应元素相乘
sin(A)    %对于常用的函数 每个元素都要运算
A/B       %等同于A乘B的逆
A\\B      %等同于A的逆乘B
```

+ 重装系统后，如何恢复matlab 文件关联及图标(Win7 XP均适) 苍天大地，重装系统后的一大幸事就是发现matlab可以直接运行，倒不是觉得装matlab麻烦，真正麻烦的是我的那些toolbox哦。这下清心了，除了....
+ 问题1：每次在外面点m文件，都会重新打开一个matlab，而不是在已经打开的editor里打开..
+ 问题2：m文件和mat文件的图标没了
+ 以下转自http://www.eefocus.com/czzheng/blog/10-01/183657_c7e69.html 
> 重装系统后，若没动MATLAB安装目标，则MATLAB不用重新安装。（同样的原因，可以移动MATLAB安装目标）
> 对MATLAB相关文件，建立重新关联就行了。
> 在MATLAB命令窗口执行如下命令，即可。
```Shell
cwd=pwd;
cd([matlabroot '\toolbox\matlab\winfun\private']);
fileassoc('add',{'.m','.mat','.fig','.p','.mdl',['.' mexext]}); %重点
cd(cwd);
disp('Changed Windows file associations. FIG, M, MAT, MDL, MEX, and P files are now associated with MATLAB.')
```
> 或者
> 1. 打开matlab，运行 help
> 2. 在help窗口中搜索Utility to Change Windows File Associations
> 3. 找到Utility to Change Windows File Associations的对应解释
> 4. 最后就是直接点击所需的文件关联
- 如果文件图标不能恢复的话,在我的电脑>工具>文件夹选项>文件类型 中寻找各个文件名称修改。在键盘上按首字母可以快速搜索
- 图标文件在：D:\Program files\MATLAB\R2009b\bin\win32 中，后缀为ico
- 另外，在Win7系统下，文件夹选项中取消了更改文件图标的功能。
- 利用之前步骤将matlab文件与程序关联后，（以管理员运行matlab）在控制面板>程序>默认程序>将文件类型或协议与程序关联中，找到任意一个matlab文件，如.m、.mat等，选中matlab程序，等待系统刷新一下，即可恢复图标。

