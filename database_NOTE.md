🌍

# 数据库笔记

[![Join the chat at https://gitter.im/jlevy/the-art-of-command-line](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/jlevy/the-art-of-command-line?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

- [基础知识](#基础知识)
- [MySQL](#MySQL)
- [Redis](#Redis)
- [MongoDB](#MongoDB)
- [免责声明](#免责声明)
- [常见问题](#常见问题)

------

## 基本知识

* 数据管理三阶段：人工管理、文件系统、数据库系统，①随着数据存储越来越多，②需要满足高并发(多用户同时访问)，③且数据一旦丢失就找不回来了，于是放弃了原来的普通文件存储，索引的手段开始越来越先进，一直到现在的数据库
* 数据库(DB)就是一种特殊的文件(类似于txt)，通过特殊的读写来存储数据，使数据结构化，以方便将来的共享读写操作，读写速度比一般文件快
* 数据库(DB)中的数据具有两大特点：“集成”、“共享”
* 数据库技术的根本目标是：**解决数据共享问题**
* 一个应用对应一个数据库(DB)，应用中实体的数据会存储于多个表中，表中的行为记录，列为字段，把能够唯一标记某个记录的特殊字段称为主键
* 数据库管理系统（DBMS）：数据库管理系统是数据库系统的核心。
* 数据库管理员（DBA）：主要工作：① 数据库设计；② 数据库维护；③ 改善系统性能，提高系统效率。
* 数据库系统（DBS）：

> + 组成：
>
> > + ① 数据库（数据）——集成，共享。
> > + ② 数据库管理系统DBMS（软件）——定义，构建，操纵，检查，控制，服务。DDL,DML,DCL. 
> > + ③ 数据库管理员DBA（人员）——设计，维护，改善性能，提高效率。
> > + ④ 软件平台——操作系统，开发工具，接口软件。
> > + ⑤ 硬件平台——计算机，网络。
>
> + 特点：集成性、高共享低冗余、独立性、统一管理控制

* 三级模式和两级映射：
  ![三级模式和两级映射](https://github.com/DodgeV/learning-programming/blob/master/png/%E4%B8%89%E7%BA%A7%E6%A8%A1%E5%BC%8F%E5%92%8C%E4%B8%A4%E7%BA%A7%E6%98%A0%E5%B0%84.png)

* 两级映射保证了数据库中数据具有较高的逻辑独立性和物理独立性
* 数据库应用系统(DBAS)，包括：数据库系统、应用软件以及应用界面
* RDBMS(Relational Database Management System)是一套程序的简称，当前主要使用两种类型的数据库：关系型数据库、非关系型数据库；所谓的关系型数据库，是建立在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据；类似一个Excel工作簿，让其中一张表映射另一张表，从而节省修改的时间，这就是关系型数据库
* 关系型数据库的主要产品(SQL语句都可以操作)：

> + oracle：在以前的大型项目中使用,银行,电信等项目
> + mysql：web时代使用最广泛的关系型数据库
> + ms sql server：在微软的项目中使用
> + sqlite：轻量级数据库，主要应用在移动平台

* C/S架构(client-server)即客户端服务器模型，自己开发客户端，比如QQ,MySQL，通过个人PC或移动端访问
* B/S架构(browser-server)即浏览器服务器模型，比如网站，通过某个浏览器访问

### 数据模型

+ 三要素：数据结构、数据操作、数据约束
+ 分类：按不同的应用层次分为：

> + a.概念数据模型（概念模型）：E-R模型
> + b.逻辑数据模型（数据模型）：层次模型(树)、网状模型(无向图)、关系模型(二维表)、面向对象模型
> + c.物理数据模型（物理模型）

+ E-R模型：实体联系模型
+ E-R模型图符：
  ![E-R模型图符](https://github.com/DodgeV/learning-programming/blob/master/png/E-R%E6%A8%A1%E5%9E%8B%E5%9B%BE%E7%AC%A6.png)
+ E-R模型举例：
  ![E-R模型举例](https://github.com/DodgeV/learning-programming/blob/master/png/E-R%E6%A8%A1%E5%9E%8B%E4%B8%BE%E4%BE%8B.png)
+ 联系：一对一，一对多（学生与宿舍），多对多（学生与课程）
+ 关系模型：采用二维表来表示，简称表，每一个二维表称为一个关系

> + ① 属性：二维表中的一列称为属性；
> + ② 元祖：二维表中的一行称为元祖。（分量不可再分）
> + ③ 关系操纵：查询、增加、删除和修改。
> + ④ 关系中的数据约束：
>
> > + a.实体完整性约束；
> > + b.参照完整性约束；
> > + c.束和用户定义的完整性约束。

+ 关系代数

> + ① 关系模型的基本操作：插入、删除、修改、查询。
> + 查询运算：a.投影运算；（投影列）b.选择运算；（选择行）c.笛卡尔积运算（连接运算）（T=R×S）
> + ② 关系代数中的扩充运算：
> + 交运算、除运算、连接与自然连接运算。
> + 并（T=R+S）、差（T=R-S）、交、除（T=R÷S）、自然连接
> + 两个表为投影或选择，三个表为其他；属性列增加为自然连接，ST属性列相加等于R为除。

### 数据库设计与管理

+ 1.数据库设计概述：设计一个能满足用户要求，性能良好的数据库。

> + ① 基本任务：根据用户对象的信息需求、处理需求和数据库的支持环境设计出数据模式。
> + ② 两种方法：
>
> > + a.以信息需求为主，兼顾处理需求（面向数据的方法）。
> > + b.已处理需求为主，兼顾信息需求（面向过程的方法）。
> > + c.面向数据的设计方法已成为主流方法。

+ 2.数据库设计的步骤：数据库设计目前一般采用生命周期法，分若干阶段：

> + ① 需求分析阶段：建立数据字典；
> + ② 概念设计阶段：设计E-R图；
> + ③ 逻辑设计阶段：把E-R图转换为关系模式。实体与联系表示成关系，E-R图中属性转换成关系的属性；
> + ④ 物理设计阶段；
> + ⑤ 编码阶段；
> + ⑥ 测试阶段；
> + ⑦ 运行阶段；
> + ⑧ 进一步修改阶段。

+ 在数据库设计中采用前四个阶段，并且重点以数据结构与模型的设计为主线。

+ 3.数据库管理：

> + ① 数据库的建立；
> + ② 数据库的调整；
> + ③ 数据库的重组；
> + ④ 数据库安全性控制与完整性控制；
> + ⑤ 数据库的故障恢复；
> + ⑥ 数据库监控。

------

## MySQL

+ 多用于存储网站数据
  ![QQ20170814-163342@2x.png](https://github.com/DodgeV/learning-programming/blob/master/png/QQ20170814-163342%402x.png)
+ RDBMS-server就是每个数据库自己写的一套程序，用于管理该数据库调用时产生的文件
+ 通过SQL语句从RDBMS-client到RDBMS-server发送调用请求，来调用数据库
+ **SQL语句**是IBM开发的，主要分为：

> - DQL：数据查询语言，用于对数据进行查询，如select
> - DML：数据操作语言，对数据进行增加、修改、删除，如insert、udpate、delete
> - TPL：事务处理语言，对事务进行处理，包括begin transaction、commit、rollback
> - DCL：数据控制语言，进行授权与权限回收，如grant、revoke
> - DDL：数据定义语言，进行数据库、表的管理等，如create、drop
> - CCL：指针控制语言，通过控制指针完成表的操作，如declare cursor

+ 重点是数据的crud（**增删改查**），必须熟练编写DQL、DML，能够编写DDL完成数据库、表的操作，其它语言如TPL、DCL、CCL了解即可
+ 想要在Linux中使用Windows下的软件比如navicat，需要安装wine
+ 面对有试用时间限制的软件，将记录天数的文件删掉，或将时间往前面调
+ Windows下的MySQL目录结构：

> + `bin`：该目录存放可执行文件
> + `data`：存放编写好的数据库即读写文件，Linux下存放在`/var/lib/mysql`
> + `Docs`：存放相关文档
> + `share`：存放字符集、语言等的信息
> + `my.ini`：是MySQL的核心配置文件，其余的`ini`文件都是配置文件，分别运用于不同的场景

+ 可以通过修改`my.ini`或者运行`bin`目录下的`MySQLInstanceConfig.exe`来重新配置MySQL

### 数据完整性

- 一个数据库就是一个完整的业务单元，可以包含多张表，数据被存储在表中
- 在表中为了更加准确的存储数据，保证数据的正确有效，可以在创建表的时候，为表添加一些强制性的验证，包括数据字段的类型、约束

#### 类型

+ 使用类型的目的是匹配数据
+ 使用数据类型的原则是：够用就行，尽量使用取值范围小的，而不用大的，这样可以更多的**节省存储空间**
+ 可以通过查看帮助文档查阅所有支持的数据类型
+ 常用数据类型如下：
+ 整数：int，bit
+ 小数：decimal
+ 字符串：varchar,char
+ 日期时间: date, time, datetime
+ 枚举类型(enum)
+ 特别说明的类型如下：
+ decimal表示浮点数，如decimal(5,2)表示共存5位数，小数占2位
+ char表示固定长度的字符串，如char(3)，如果填充'ab'时会补一个空格为'ab '，即使没有3个也会存储3个
+ varchar表示可变长度的字符串，如varchar(3)，填充'ab'时就会存储'ab'
+ 字符串text表示存储大文本，当字符大于4000时推荐使用
+ 对于图片、音频、视频等文件，不存储在数据库中，而是上传到某个服务器上，然后在表中存储这个文件的保存路径
+ ![mysql数据类型](https://github.com/DodgeV/learning-programming/blob/master/png/%E6%89%B9%E6%B3%A8%202020-09-09%20195436.jpg)

#### 约束

+ 主键`primary key`：物理上存储的顺序
+ 非空`not null`：此字段不允许填写空值
+ 惟一`unique`：此字段的值不允许重复
+ 默认`default`：当不填写此值时会使用默认值，如果填写时以填写为准
+ 自动增长`auto_increment`
+ 外键`foreign key`：对关系字段进行约束，当为关系字段填写值时，会到关联的表中查询此值是否存在，如果存在则填写成功，如果不存在则填写失败并抛出异常，即存储其他表主键的键，但因为比较消耗资源所以能不用则不用
+ 说明：虽然外键约束可以保证数据的有效性，但是在进行数据的crud（增加、修改、删除、查询）时，都会降低数据库的性能，所以不推荐使用，那么数据的有效性怎么保证呢？答：可以在逻辑层进行控制

### 命令行

+ SQL不区分大小写

+ `mysql -uroot -p`回车然后输入密码

+ `quit`或`exit`或按下`Ctrl`+`d`退出

+ `help`显示帮助信息

+ `--`开头为注释

+ `show databases;`查看所有数据库，只要不加`;`则不管输入多少行只当做一行命令执行

+ `select now();`显示当前数据库的时间

+ `select version();`显示当前版本

+ `explain`

+ `slow log`慢日记

+ `set long_query_time = 数值`

+ `analyze table t`重新统计索引信息

+ `show index from table`重看索引基数

+ `show processlist`查看线程的情况

+ `create database XX charset=utf-8;`创建名为XX的数据库，charset不写则默认拉丁文

+ `show create database XX;`查看创建数据库的语句，详细显示charset等信息

+ `drop database XX`删除数据库

+ 可以在数据库的名字两边加上TAB键上面的符号，来声明一个整体

+ `use XX;`使用xx数据库

+ `select database();`查看当前使用的数据库

> + `show tables;`查看当前数据库中所有表
> + `create table XX(id int, name varchar(20));`创建名为XX的数据表，其中有id和name两个字段
> + `create table XX(id int primary key not null auto_increment, name varchar(20));`也可以在类型后面加限制，如果限制过长可以换行继续输

```mysql
create table students(
    id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','人妖','保密'),
    cls_id int unsigned default 0
)
```

> + `desc 表名`查看表的结构
> + `insert into students values(0,"老王", 18, 188, 88, "男", 0);`插入记录，里面的0是按照自动增长的值自动生成
> + `select * from students;`从students表中查询记录
> + `alter table 表名 add 字段名 类型及约束;`往表添加字段
> + `alter table 表名 modify 字段名 类型及约束;`更改字段类型
> + `alter table 表名 change 原名 新名 类型及约束;`更改字段名
> + `alter table 表名 drop 字段名;`删除字段，注意会将字段包含的所有记录都删掉，所以需慎用，多做加法少做减法
> + `drop table 表名`删除表
> + `show create table 表名;`查看创建表的语句，会详细显示所使用的引擎，以及其他设置，`auto_increment`即自动增长的值，该变量就是插入记录的主键的值
> + MySQL常用的存储引擎--MyISAM、InnoDB、memory
>   ![常用引擎对比](https://github.com/DodgeV/learning-programming/blob/master/png/%E4%B8%8D%E5%90%8C%E5%BC%95%E6%93%8E%E5%AF%B9%E6%AF%94.jpg)

+ 增删改查(curd) 
+ 增加Create

> + 全部插入：
> + `insert into 表名 values(0,"XXX");`第一个主键会随着`auto_increment`变化而变化，所以可以输入很多类型的值而不产生影响
> + `insert into 表名 values(null,"XXX");`
> + `insert into 表名 values(default,"XXX");`
> + 后面的字段类型如果是枚举型，可以换成从1开始的索引
> + 部分插入：
> + `insert into 表名(列1,列2,...) values(值1,值2,...)`只插入要插入的字段，并且只要不是非空`not null`型的字段，就可以不写值
> + 多行插入：
> + `insert into 表名 values(...),(...)...;`多行全部插入
> + `insert into 表名(列1,...) values(值1,...),(值1,...)...;`多行部分插入

+ 改update

> + `update 表名 set 列1=值1,列2=值2... where 条件`
> + `update students set gender=1;`将性别这一列全部改为值1
> + `update students set gender=2 where id=1;`选定某行记录改动对应性别，写的条件若是很苛刻，就用主键
> + `update students set gender=2 name="XX" where id=1;`也可以改多个字段

+ 查询select，读取Retrieve

> + `select * from students where id < 7;`查询也可以加条件
> + `select 字段名1 字段名2 from students where id>3`也可以只查询几个字段
> + `select name as 姓名,gender as 性别 from students;`也可以用别名，并且书写字段的顺序就是显示的顺序

+ 删除delete
+ 物理删除：

> + `delete from 表名;`会将整个数据表中的所有数据都删除
> + `delete from students where name="小李飞刀";`将特殊字段名的记录删除
> + 删完整条记录之后，再次添加记录，默认会在末行添加，而不会在删完的位置增加，最好不要强制增加在删完的位置

+ 逻辑删除：网站为了流量，并不会给用户注销的机会，并不会在库中真的将用户记录删除，而是标记一列新的字段来显示注销的用户

> + `alter table students add is_delete bit default 0;`用`is_delete`字段标记是否真的删除，字节长度为8位，默认值为0
> + `update students set isdelete=1 where id=1;`注销的用户并不需要删除，只需要将特殊字段的值更新，即值改为1
> + `select * from students where is_delete=1;`查询注销的用户

#### 索引

> + 前缀索引：例如对于一些字段值很大的，如TEXT，BLOB就可以使用前缀索引了
> + 最左前缀原则
> + 聚族索引：其实就是主键索引
> + 二级索引：其实就是非主键索引

#### 事物

![事物](https://github.com/DodgeV/learning-programming/blob/master/png/%E4%BA%8B%E7%89%A9.jpg)

#### 锁

+ 全局锁

> + 一般用于备份
> + flush tables with read lock(FTWRL)，只读状态

+ 表级锁

> + 表锁：lock tables ... read/write
> + 元数据锁（MDL）

+ 行级锁

> + 两阶段协议
> + 解决死锁的方法
>
> > + 超时释放
> > + 检测-回滚

#### 日记系统

+ redo log

> + InnodDB 特有的
> + 记录的是这个数据页做了什么修改
> + 更新操作时，先把记录写到redolog上，再更新内存。系统再空闲的时候把redoLog持久化到磁盘
> + 循环写

+ binlog

> + server层，所有引擎都共用
> + 记录的是一个完整的更新命令
> + binlog可以追加

+ 两阶段提交
+ 为什么需要两个日记系统

#### 性能相关

#### 面试题

+ 一条sql语句是如何执行的？

> + 连接器->查询缓存->分析器（语法-词法分析）->优化器->执行器

------

## Redis

+ 多用于存储缓存数据

### 基本数据结构及其应用

+ 字符串

> + 1、缓存功能 2、计数，例如浏览量的统计
> + 共享session
> + 限制过期时间，例如短信验证吗的有效期

+ 列表

> + 消息队列
> + 文章列表

+ 集合

> + 给用户打标签
> + 点赞、关注之类的，由于集合之间支持合并等操作，可以用来求共同好友之类的

+ 有序集合：排名系统
+ 哈希

> + 缓存一些对象
> + 底层实现原理----由dict结构表示
>
> > + `dictType *type`
> > + `void *privatedata` 私有数据
> > + `dictht ht[2]`
> > + `int trehashidx`，如果没有在rehash则值为-1
>
> + rehash过程
>
> > + 拓展
> >
> > > + 大小为 used * 2 的 2^n
> > > + 渐进式rehash----rehashidx记录哈希到n哪了，如果有增删改查的话，则会现在ht[0]进行，如果没有则到ht[1]
> > > + 如果没有执行 bgsave命令，则负载因子大于等于1，否则大于等于5
> >
> > + 收缩：负载因子为 0.1

### 面试题相关

+ 为什么Redis很快？

> + 采用非阻塞的IO多路复用，使得单个线程可以处理多个连接，并且把相关请求直接直接压到队列中
> + 纯内存操作：文件事件分派器从队列中取出事件分配给对应处理器进行处理（连接应答、命令请求、命令回复三中处理器）
> + 单线程避免的线程上下文切换的消耗、加锁、解锁等消耗

+ 过期按键删除策略以及内存淘汰机制

> + 定期删除+惰性删除，注意，定期删除每隔一段时间是随机抽取一些元素删除的
> + 内存淘汰机制

+ 并发竞争问题

### 集群

### 哨兵

### 如何保证高可用

+ 单机redis很难支撑10+的qps。

#### 主从复制（★）

### 事务

+ 把命令放入队列，直到提交才开始执行
+ 不具有原子性，也就是说不会回滚，因此也没有一致性
+ 不过又隔离性和持久性

### 数据库、缓存双写不一致问题

+ 1、采用先删除缓存后更新数据库的策略  + 对同一商品的更新、读取的请求映射到同一个队列
+ 2、先更新数据库在删除缓存会，如果删除缓存失败会出现不一致问题
+ 3、先更新缓存在更新数据库可能会出现不一致和如果更新操作频繁的话，会出现资源浪费问题

### 如何解决多线程竞争问题

+ 可以采用分布式锁 + 时间戳

### 持久化

#### AOF

+ 开启AOF：appendonly yes
+ 大致过程

> + 写入命令追加到 aof_buf 缓存区
> + AOF 缓冲区根据对应策略做硬盘同步操作
> + AOF越来越大，所以会做重写操作
> + 加载AOF恢复

+ 文件同步机制

> + always----命令写入aof_buf后马上调用fsync命令操作做同步操作
> + everysec----先调用系统write操作，之后返回。fsync操作由专门的线程每隔1秒调用一次
> + no----调用write，不对aof文件做同步操作，同步操作由操作系统自己负责，周期最长为30秒

+ wirte和fsync解释

> + write----会触发延迟写机制。Linux内核会提供一个页缓冲区来提供IO性能。write操作写入缓冲区后直接返回
> + fsync----强制硬盘同步，将阻塞知道写入硬盘完成

+ 重写机制----fork一个子进程来重写，父进程依然响应，把命令存放再AOF重写缓冲区中。子进程完成后，父进程再把AOF缓存区的数据写入到AOF文件中
+ 相关问题定位

#### RDB

+ Save：阻塞持久化
+ bgsave：阻塞fork子进程持久化
+ 采用LZF压缩算法
+ 优点

> + 压缩的二进制文件恢复非常快
> + 适合全量复制等场景

+ 缺点

> + 无法做到实时持久化，频繁操作成本高
> + 不同版本的RDB格式可能无法兼容

### 用redis实现分布式锁

------

## MongoDB

* 一般用于非关系型数据

------

## 免责声明

除去特别小的工作，你编写的代码应当方便他人阅读。能力往往伴随着责任，你 *有能力* 在 MySQL 中玩一些奇技淫巧并不意味着你应该去做！:)

------

## 常见问题
