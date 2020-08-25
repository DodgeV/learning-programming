🌍

# matlab笔记

[![Join the chat at https://gitter.im/jlevy/the-art-of-command-line](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/jlevy/the-art-of-command-line?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

- [基础知识](#基础知识)
- [数据结构](#数据结构(15种))
> - [文件及数据处理](#文件及数据处理)
> - [系统调试](#系统调试)
> - [单行脚本](#单行脚本)
> - [冷门但有用](#冷门但有用)
> - [仅限 OS X 系统](#仅限-os-x-系统)
> - [仅限 Windows 系统](#仅限-windows-系统)

- [免责声明](#免责声明)
- [常见问题](#常见问题)

## 基本知识
* 布局里面的默认，回到软件最初的样子
* 预设，里面设置字体大小
* 新建脚本，打开编辑器，写入脚本，右键点执行所选内容
* 将编辑器点住拖开，再点右上角倒三角停靠
* 工具箱(Toolbox) (分为功能性和学习型)：封存繁琐复杂的流程，方便以后使用
* Notebook可以用于记录笔记
* Simulink动态仿真集成环境，节约实际环境中的资源
* 搜索在命令窗口输入一条命令的搜索过程:是否变量、是否函数、是否当前目录下的M文件、是否搜索路径下的其他M文件
* 设置方法:`path`输出所有的搜索路径,`help path`查看path的用法
* `cd`返回当前工作目录,`userpath`返回当前工作目录 
* `userpath()`后加更改的打开默认文件夹,`savepath`保存更改
* `pathtool`打开path工具箱,添减搜索路径

* `%%`分隔开代码块，再按`ctrl+Enter`可执行所选内容，注释以`%`开头
* `clc`清空历史，清除Command Window中的所有命令
* 语句末尾无`;`则输出该句执行结果,末尾有`;`则只执行命令不输出
* MATLAB可在同时执行数个命令，只要以`,`或`;`将命令隔开
* 一行写不开，用`...`续行，续行前面最好留一个空格
* 按`Esc`清除命令

* 变量命名规则：字母开头，包括字母、数字、下划线，区分大小写，长度不超过63位，不用声明，拿来即用
* 赋值有两种：变量=表达式 或 直接写表达式赋值给默认变量`ans`
* `who`显示所有的变量名，`whos` 显示变量名和对应属性
* `clear all`清除Workspace中的所有变量，可把`all`换成指定变量名
* `save`将所有变量存入文件`matlab.mat`，可以后加文件名存入指定文件
* `save 文件名 变量名列表`，将指定变量存入指定文件，变量之间用空格隔开 
* `load 文件名`，导入指定文件
* `load 文件名 变量名列表`，将指定变量从指定文件导入，变量之间用空格隔开
* `format`后加格式符,控制数据的输出格式默认`short` 不影响存储,[详见此博客](https://blog.csdn.net/xuxinrk/article/details/83012624)
* 常用数学函数：包括正余弦，正余切
> * `sqrt(x)`开平方
> * `sign(x)`符号函数(Signum function)
* 常用永久常数(预定义变量)：应尽量避免对这些变量重新赋值
> * `pi`圆周率 （值为 3.1415926... 或 imag(log(-1))） 
> * `inf`或`Inf`无限大， 例如1/0
> * `nan`或`NaN`非数值（Not a number） 例如0/0 
> * `realmax`系统所能表示的最大数值  
> * `realmin`系统所能表示的最小数值 
> * `i`或`j`基本虚数单位，复数输入时如`z=3+4i`加号两边不能空格
> * `eps`系统的浮点（Floating-point）精确度 
> * `ans`特殊变量
* matlab中的数默认为双精度实数，表示方法同C语言
* 浮点运算的相对误差为`eps`
* 浮点数表示范围为：10^-308 ~ 10^308

* M文件分为命令文件(Script File)和函数文件(Function File)
> * 命令文件没有输入，没有返回，直接`ctrl+Enter`运行，命令文件可以对工作空间的变量操作，结果返回工作空间
> * 函数文件中的变量为局部变量，函数执行完毕，变量被清除，函数文件如果没有参数也可以直接`ctrl+Enter`运行，其他函数文件需要调用形式运行
> * 如果有参数运行出错后,输入函数名再传入参数调用该函数
> * 函数参数可调标识变量：nargin，nargout，varargin，varargout
> * 程序调试：断点和单步
* `doc`+命令，以网页形式查看该命令的帮助
* `help`+命令，查看该命令的简单帮助 
* 其他帮助命令：`helpdesk`&`helpwin`
* `lookfor XX`，按指定的关键词查询与之相关的命令
* `which`+函数名，显示指定函数所在的目录
* * *
## 数据结构(15种)
### 数值类型
> * 单精度浮点型`single`4个字节，双精度浮点型`double`8个字节
+ `a = 1.2`MATLAB将所有变量均存成double的形
+ `b = single(a)`
+ `d1 = [realmin('single') realmax('single')]`找到单精度的值的范围

> * 8种整型数据，带符号整型(int8 int16 int32 int64)和无符号整型(uint8 uint16 uint32 uint64)
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

### 字符串`char`用单引号括起来
* `double(a)`获得`a`的ascii码
* `double('a')`获得`'a'`的ascii码
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
* 直接输入法建立矩阵：用`[]`包括所有元素，同行元素用空格或`,`隔开，不同行用`;`或者回车隔开
* M文件建立矩阵：鼠标启动编辑器或输入`edit`命令，语法同直接输入法，可以在一个文件中建立多个矩阵，输入文件名执行文件
* 特殊矩阵的建立:
> * `zeros(4,5)`建立4行5列零矩阵，`zeros(3)`建立3行3列的零矩阵
> * `ones(3,4)`建立3行4列全为1的幺矩阵
> * `eye(size(A))`产生与A矩阵同阶的单位矩阵
> * `rand(m,n)`产生随机矩阵 m=n 时简写为 rand(n)
> * `randn(m,n)`产生均值为0，方差为1的标准正态分布随机矩阵m=n 时简写为 randn(n)
> * `pascal(n)`
> * `magic(n)`生成n阶魔方矩阵，每行每列加起来相等
> * `hilb(n)`Hilbert矩阵
> * Toeplitz矩阵
> * `a:b:c`建立以a开头c结尾步长为b的行向量 
> * `linspace(1,5,3)`建立1开头5结尾的3个元素的行向量
> * `diag(X)`若 X 是矩阵则产生X的主对角线向量，若 X 是向量则产生以 X 为主对角线的对角矩阵
* `tril(A)`提取一个矩阵的下三角部分
* `triu(A)`提取一个矩阵的上三角部分
* `Size(A)` 以向量的形式返回矩阵的行数与列数
* `Length(A)` 返回向量的长度。
* 索引矩阵：
> * 用行列标，(从1开始)`A(2,3)`表示A中第2行第3列的元素
> * 用序号索引，`A(3)`表示A中的第3个元素，竖着一列数完再数第二列
> * 序号和下标转换，`A(i:j, m:n)`表示由矩阵 A 的第 i 到第 j 行和第 m 到第 n列交叉线上的元素组成的子矩阵，`:`表示矩阵的整行或整列。
* 重排矩阵：
* 矩阵拆分：
```Matlab
x = [1 3 5 2];   
y = 2*x+1   
y = 3 7 11 5           % 我们可以随意更改、增加或删除向量的元素：  
y(3) = 2                  % 直接赋值更改第三个元素   
y =3 7 2 5   
y(6) = 10                % 加入第六个元素   
y = 3 7 2 5 0 10      % 未赋值部分自动为零
y(4) = []                  % 用赋空值的方式删除第四个元素，   
y = 3 7 2 0 10   
x(2)*3+y(4)             % 取出x的第二个元素和y的第四个元素来做运算   
ans = 9   
y(2:4)-1                   % 取出y的第二至第四个元素来做运算   
ans = 6 1 -1   
```
* 扩展矩阵：
* 压缩矩阵：
* 矩阵和向量运算：
> * `a * b`执行矩阵的标准乘法
```Matlab
clear;clc;close all;
A = [1 2 3]
B = [4 5 6]
A * B                 %行数和列数不匹配则不能相乘
A * B'                %可以乘转置
A .* B                %点乘，对应元素相乘
sin(A)                %对于常用的函数 每个元素都要运算
inv(A)                %数组的逆矩阵
rank(A)              %矩阵的秩
eig(A)                %矩阵的特征值与特征向量
rref(A)               %矩阵的行最简形
det(A)                %计算行列式
A/B=A*inv(B)    %矩阵右除，要求两个矩阵列数一样
A\B=inv(A)*B    %矩阵左除，要求两个矩阵行数一样
A\\B                  %等同于A的逆乘B
A^2                   %矩阵的乘方 
```
* 线性方程组求解
* 矩阵的相似化简和分解
* 矩阵和向量的范数
* 矩阵分析
* 适用於向量的常用函数有：
> * min(x): 向量x的元素的最小值 
> * max(x): 向量x的元素的最大值 
> * mean(x): 向量x的元素的平均值 
> * median(x): 向量x的元素的中位数 
> * sort(x): 对向量x的元素进行排序（Sorting） 
> * length(x): 向量x的元素个数 
> * norm(x): 向量x的欧氏（Euclidean）长度 
> * sum(x): 向量x的元素总和 
> * prod(x): 向量x的元素总乘积 
> * dot(x, y): 向量x和y的内 积 
> * cross(x, y): 向量x和y的外积（大部份的向量函数也可适用於矩阵。） 
* * *
## 程序控制结构
### 顺序
### 选择
### 循环
* * *
## 图形可视化
### 二维平面图形和坐标系
* 1. 几个基本的绘图命令 
> * 高层绘图线性坐标曲线：`plot(X,Y)`或`plot(x1,y1,x2,y2,…)`
```Matlab
x=0:0.01:2*pi;
y=[sin(x);cos(x)];
plot(x,y)
```
* 2. 线型和颜色：plot 函数可以设置曲线的线段类型、定点标记和线段颜色。 
> * 调用格式：plot(x,y,s) ，s 为类型说明参数，是字符串。其中s可以是三种类型的符号，也可以是线型与颜色和定点标记与颜色的组合
![图片-s参数含义](https://github.com/DodgeV/learning-programming/blob/master/png/%E5%9B%BE%E7%89%87-s%E5%8F%82%E6%95%B0%E5%90%AB%E4%B9%89.png)
> * 如果没有 s 参数，plot 将使用缺省设置（实线，前七种颜色顺序着色）绘制曲线； 
> * 在当前坐标系中绘图时，每调入一次绘图函数，MATLAB将擦掉坐标系中已有的图形对象。可以用 `hold on`命令在一个坐标系中增加新的图形对象。
> * 注意MATLAB会根据新图形的大小，重新改变坐标系的比例。
```Matlab
t1=0:0.1:2*pi; 
t2=0:0.1:6; 
y1=sin(t1);
y2=sqrt(t2); 
plot(t1,y1,'hb',t2,y2,'--g')             %用不同的线型和标注来绘制两条曲线
```
* 3. 图形窗口的分割(同一窗口含有多个坐标轴)
> * `subplot(m，n，i)`把图形窗口分割为 m 行 n 列子窗口，然后选定第 i 个窗口为当前窗口
> * 该命令不仅用于二维图形，对三维图形一样适用。其本质是将 figure 窗口分为几个区域，再在每个区域内分别绘图
```Matlab
subplot(2,2,1) 
t=0.1:0.1:2*pi; 
y=sin(t); 
semilogx(t,y)                   %对x轴部分取对数，让低幂次部分完全显示
grid on  
subplot(2,2,2) 
t=0:0.1:4*pi; 
y=sin(t); 
plot(t,y)
subplot(2,2,3) 
x=1:0.01:5; 
y=exp(x); 
plot(x,y,x,y,’semilogx’,’plot’)  
subplot(2,2,4) 
x=1:0.1:10; 
y=sqrt(x); 
plot(x,y,’:rd’) 
```
* 4. 坐标轴控制
> * `axis([xmin,xmax,ymin,ymax,zmin,zmax])`坐标的最小值（ xmin,ymin,zmin）必须小于相应的最大值（ xmax,ymax,zmax），否则会出错
```Matlab
subplot(2,1,1) 
t=0:0.1:4*pi; 
y=sin(t); 
plot(t,y)  
subplot(2,1,2) 
t=0:0.1:4*pi; 
y=sin(t); 
plot(t,y) 
axis([0,max(t),min(y),max(y)]) 
```
![坐标轴调整命令](https://github.com/DodgeV/learning-programming/blob/master/png/%E5%9D%90%E6%A0%87%E8%BD%B4%E8%B0%83%E6%95%B4%E5%91%BD%E4%BB%A4.png)
* 5. 图形标注
> * 坐标轴和图形标题标注 
>> * 标注坐标轴 x、y 和 z 的命令函数为 xlabel、ylabel 和 zlabel ，调用格式为：
>> * xlabel(’text’) 
>> * xlabel(’text’,’Property1’,PropertyValue1,’Property2’,PropertyValue2,...)
>> * H = xlabel(...)  返回坐标轴标注的句柄。
>> * 其中，’text’是要添加的标注文本。’Property’是文本的属性名，’PropertyValue’是属性值（所用字体、大小、标注角度等）。
>> * 图形加标题的函数为 title，其调用格式与坐标轴标注类似。
> * 图例的标注 
>> * legend命令实现不同图例的说明。其调用格式为： 
>> * legend(string1,string2,string3, ...)   
>> * legend(string1,string2,string3,...,Pos)   
>> * 按顺序把字符串添加到相应的曲线线型符号之后；Pos对图例的位置作出设置和调整： 
>> * 0 = 自动把图例置于最佳位置（ 和图中曲线重复最少）； 
>> * 1 =  置于图形窗口的右上角（ 缺省值）； 
>> * 2 =  置于图形窗口的左上角； 
>> * 3 =  置于图形窗口的左下角； 
>> * 4 =  置于图形窗口的右下角； 
>> * -1 =  置于图形窗口的右侧（ 外部）。 
* 6. 控制分格线对二维和三维图形都适用。
> * 有三种用法： 
> * grid on：打开分格线控制开关，绘制的图形都带有分格线； 
> * grid off：关闭分格线控制开关，绘制的图形都不带分格线； 
> * grid：用于实现分格线绘制切换。
```Matlab
%绘制图形，并用函数 xlabel、title 和 legend 命令进行标注。
t=0:0.1:4*pi; y=sin(t); y1=cos(t); plot(t,y,':',t,y1,'r*') 
xlabel('x 轴  (0--4\pi)','fontsize',12,'fontweight','bold') 
ylabel('y 轴','fontsize',12,'fontweight','bold') 
title('绘制正弦波和余弦波      Pos=1','fontsize',10,'fontweight','bold','fontangle','italic') 
text(pi,0,'\leftarrowsin(\pi)=0') 
text(pi,-1,'\leftarrowcos(\pi)=-1')
text(pi/2,0.9,['\uparrowsin(\pi/2)=',num2str(sin(pi/2))]) 
text(0,-0.6,['绘图日期：',date]) 
text(0,-0.8,['MATLAB 版本：',version]) 
legend('正弦波','余弦波') 
figure(2) 
plot(t,y,':',t,y1,'r*') 
title('绘制正弦波和余弦波    Pos=0','fontsize',10,'fontweight','bold','fontangle','italic') 
legend('正弦波','余弦波',0) 
grid on 
figure(3) 
plot(t,y,':',t,y1,'r*') 
title('绘制正弦波和余弦波  Pos=-1','fontsize',10,'fontweight','bold','fontangle','italic') 
text(7*pi/2,0,'\rightarrowcos(\pi*7/2)=0') 
legend('正弦波','余弦波',-1) 
grid off
```
### 三维图形
* 1. 三维曲线绘图命令
> * `plot3(X1,Y1,Z1,s1,X2,Y2,Z2,s2,…)`其中Xn、Yn、Zn为第一到三维数据，是尺寸相等的向量/矩阵，s、s1、s2：是字符串，用来设置线型、颜色、数据点标记
```Mablab
t=0:0.1:8*pi; 
plot3(sin(t),cos(t),t)   %x、y、z 是向量
title(’绘制螺旋线’)  %用命令 title 对图形主题进行标注 
xlabel('sin(t)')         
ylabel('cos(t)') 
zlabel('t')              %命令 zlabel 用来指定 z 轴的数据名称 
grid on                      %加上网格线
```
```Matlab
[X,Y]=meshgrid(-pi:0.1:pi);
Z=sin(X)+cos(Y); 
plot3(X,Y,Z)               %x、y、z 都是矩阵
```
* 2. 三维曲面绘图命令 
* 三维曲面绘图命令可分为平面网格点的生成、在平面网格基础上绘制三维网格及对三维表面进行处理三个步骤
> * 平面网格点的生成：`[X,Y]=meshgrid(x,y)`将由两个向量决定的区域转换为x-y 平面上对应的网格点矩阵，当x=y时，可简写为`meshgrid(x)`
> * 参数含义如下： 
> * x：是区间[x0,xm]上分划的向量； 
> * y：是区间[y0,yn]上分划的向量； 
> * [X,Y]：输出变量矩阵，矩阵 X 的行向量都是向量 x，矩阵 Y 的列向量都是向量 y。 
> * 绘制三维网格：
> * 调用格式为：
> * mesh(X，Y，Z，C)：X、Y、Z、C 是同维数的矩阵，X、Y、Z 对应空间上的网格点，网格线颜色由C决定；
> * mesh(X，Y，Z)：相当于上面的 C=Z 的情况； 
> * mesh(x，y，Z，C)：x 和 y 是向量，Z 和 C 是同维数的矩阵，网格曲面的网格顶点是（ x(j)，y(i)，Z(i,j)），网格线的颜色由矩阵 C 决定； 
> * mesh(x，y，Z)：相当于上面的 C=Z 的情况； 
> * mesh(Z，C)：等价于 mesh(x，y，Z，C)，此时向量x=1:n，向量 y=1:m； 
> * mesh(Z)：相当于上面的 C=Z 的情况
> * mesh(...,’PropertyName’,PropertyValue,...)：给函mesh设置曲面属性。
> * 另外还有：meshc(增加等高线) 和 meshz(在图形下面生成网格线)
> * 三维表面处理：
> * 函数 surf 可实现对网格曲面片进行着色，将网格曲面转化为实曲面。surf 命令的调用格式与 mesh 相同。
> * z=peaks;              %绘制山峰的图像，将函数值赋予变量z 
> * surf(z)  ;            %对山峰的图像进行着色处理
> * shading interp        %函数 shading 改变着色方式 
> * 柱面的表达 
> * cylinder命令中，柱面的轴线定义为 z 轴，只要给出母线的描述就可完成一个柱面。 
> * 调用格式为： 
> * [X,Y,Z] = cylinder(R,N)；R是一描述柱面母线的向量，N是旋转柱面上的分割线条数
> * [X,Y,Z] = cylinder(R)：缺省值 N=20； 
> * [X,Y,Z] = cylinder：缺省值 N=20，R=[1，1]。 
> * [X,Y,Z] 是返回的x,y,z坐标向量。 
```Matlab 
t=pi:0.01:3*pi; 
r=sin(t)+t; 
cylinder(r,30) 
shading interp
```
> * 球面的表达
> * sphere调用格式为： 
> * [X,Y,Z]=sphere(N)：产生一个（ N+1）×（ N+1）×（ N+1）的矩阵，然后用函数 surf 命令绘制一个单位的球面，N 为设置分割线的条数； 
[X,Y,Z] = sphere：缺省值 N = 20。
```Mablab
[X,Y,Z]=sphere;
surf(X,Y,Z)  %画一个球面。
```
* 特殊图形的绘制:除了绘制二维、三维图形外，还要用到直方图、面积图、饼图等特殊图形
![特殊图形-表](https://github.com/DodgeV/learning-programming/blob/master/png/%E7%89%B9%E6%AE%8A%E5%9B%BE%E5%BD%A2-%E8%A1%A8.png)
> * 1.面积图命令`area`表现各个不同部分对整体所作的贡献 
> * area(X,Y)：与 plot 的命令的使用方法相似，将连线图到 x 轴的那部分填上了颜色； 
> * area(Y)：缺省值 X=1:SIZE(Y)； 
> * area(X,Y,LEVEL)或 area(Y,LEVEL)：填色部分为由连线图到 y=level 的水平线之间的部分。
```Matlab
X=-2:2; 
Y=[3,5,2,4,1;5,4,2,3,5;3,4,5,2,1]; 
area(X',Y')                       % 绘制一面积图 
legend('因素 1','因素 2','因素 3') 
grid on
```
> * 2.直方图命令`bar`常用于统计数据的作图， 有bar、bar3、barh 和 bar3h几种函数，其调用格式类似。
> * 以函数 bar 为例： 
> * bar(X,Y)：X 是横坐标向量，Y 可以是向量或矩阵。Y 是向量时，每一个元素对应一个竖条；Y 是 m 行 n 列矩阵时，将画出 m 组竖条，每组包括 n 个竖条； 
> * bar(Y)：横坐标使用缺省值 X=1:M； 
> * bar(X,Y,WIDTH)  或 bar(Y,WIDTH)：用 WIDTH 指定竖条的宽度，如果 WIDTH＞1，条与条之间将重合。缺省宽度为 0.8； 
> * bar(...,’grouped’)：产生缺省的组合直方图； 
> * bar(...,’stacked’)：产生累积的直方图； 
> * bar(...,linespec)：指定条的颜色；
> * H = bar(...)：返回条形图对象的句柄。 
```Matlab
X=-2:2; 
Y=[3,5,2,4,1;5,4,2,3,5;3,4,5,2,1]; 
subplot(2,2,1) 
bar(X,Y','r') 
xlabel('x')
ylabel('y') 
colormap(cool) 
subplot(2,2,2) 
barh(X,Y','grouped') 
xlabel('y') 
ylabel('x') 
colormap(cool) 
subplot(2,2,3) 
bar(X,Y','stacked') 
xlabel('x') 
ylabel('\Sigma y') 
colormap(summer) 
subplot(2,2,4) 
barh(X,Y','stacked') 
xlabel('y');ylabel('\Sigma x') 
colormap(summer)
```
```Matlab
% 绘制三维直方图。
X=-2:2; 
Y=[3,5,2,4,1;5,4,2,3,5;3,4,5,2,1]; 
subplot(2,2,1) 
bar3(X,Y','r') 
zlabel('y') 
ylabel('x') 
colormap(cool) 
subplot(2,2,2) 
bar3h(X,Y','grouped') 
ylabel('x') 
zlabel('y') 
colormap(cool) 
subplot(2,2,3) 
bar3(X,Y','stacked') 
ylabel('x') 
zlabel('\Sigma y') 
colormap(summer) 
subplot(2,2,4) 
bar3h(X,Y’,’stacked’) 
zlabel(’x’) 
ylabel(’\Sigma y’) 
colormap(summer)
```
> * 3.饼图命令`pie`又叫扇形图，用于显示向量中元素所占向量元素总和的百分比
> * pie 和 pie3分别用于绘制二维和三维饼图。
> * 调用格式： 
> * pie(X)：向量 X 的饼图。把 X 的每一个元素在所有元素总和中占的比例表达出来； 
> * pie(X,EXPLODE)：向量EXPLODE（和向量X长度相等）用于指定饼图中抽出一部分的块（非零值对应的块）
> * pie(...,LABELS)：LABELS 是用于标注饼图的字符串数组，其长度必须和向量 X相等； 
> * H = pie(...)：返回包括饼图和文本对象句柄。 
```
%用函数 pie 和 pie3 绘制饼图
x=[200,360,120,400,320]; 
subplot(2,2,1),
pie(x,[0 0 0 1 0]) 
subplot(2,2,2),
pie3(x,[0 0 0 1 0])
subplot(2,2,3),
pie(x(2:5)) 
subplot(2,2,4), 
x=[0.1,0.12,0.21,0.34,0.11];
pie3(x ,{'A','B','C','D','E'})
```
> * 底层绘图：line对象和line函数
### 二维绘图的辅助操作
#### 标注：图形名称，坐标轴名称，曲线标注，图例
* text对象和text函数
#### 图形保持(同一坐标轴绘制多个图形)
* 对象和句柄：MATLAB把构成图形的各个基本要素称为图形对象，产生每个图形对象时，MATLAB会自动分配一个唯一的值用于表示该对象，称为句柄
* 对象之间的关系
* * *
## 符号运算
### 符号计算基础
* 符号常量和符号变量
* 符号四则运算
* 符号表达式的化简
* 符号矩阵运算
### 符号函数
* 极限
* 微分
* 积分
### 符号级数
### 符号方程求解
* 代数方程
* 微分方程
* * *
## 免责声明
除去特别小的工作，你编写的代码应当方便他人阅读。能力往往伴随着责任，你 *有能力* 在 Bash 中玩一些奇技淫巧并不意味着你应该去做！;)
* * *
## 常见问题
+ 重装系统后，如何恢复matlab 文件关联及图标(Win7 XP均适)?苍天大地，重装系统后的一大幸事就是发现matlab可以直接运行，倒不是觉得装matlab麻烦，真正麻烦的是我的那些toolbox哦。这下清心了，除了....
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
