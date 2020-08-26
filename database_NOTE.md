🌍

# 数据库笔记

[![Join the chat at https://gitter.im/jlevy/the-art-of-command-line](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/jlevy/the-art-of-command-line?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

- [基础知识](#基础知识)

- [免责声明](#免责声明)
- [常见问题](#常见问题)

## 基本知识
* 随着数据存储越来越多，索引的手段开始越来越先进，一直到现在的数据库
* 数据库就是一种特殊的文件(类似于txt)，通过特殊的读写来存储数据以方便将来的读写操作，读写速度比一般文件快
* 行为记录，列为字段，把能够唯一标记某个记录的特殊字段称为主键
* RDBMS(Relational Database Management System)是一套程序的简称，当前主要使用两种类型的数据库：关系型数据库、非关系型数据库；所谓的关系型数据库，是建立在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据；类似一个Excel工作簿，让其中一张表映射另一张表，从而节省修改的时间，这就是关系型数据库
* 关系型数据库的主要产品(SQL语句都可以操作)：
> * oracle：在以前的大型项目中使用,银行,电信等项目
> * mysql：web时代使用最广泛的关系型数据库
> * ms sql server：在微软的项目中使用
> * sqlite：轻量级数据库，主要应用在移动平台
* C/S架构(client-server)即客户端服务器模型，自己开发客户端，比如QQ,MySQL，通过个人PC或移动端访问
* B/S架构(browser-server)即浏览器服务器模型，比如网站，通过某个浏览器访问
## MySQL
* 多用于存储网站数据
* 编写好的数据库即读写文件存放在`/var/lib/mysql`
![QQ20170814-163342@2x.png](https://github.com/DodgeV/learning-programming/blob/master/png/QQ20170814-163342%402x.png)
* RDBMS-server就是每个数据库自己写的一套程序，用于管理该数据库调用时产生的文件
* 通过SQL语句从RDBMS-client到RDBMS-server发送调用请求，来调用数据库
* **SQL语句**主要分为：
> * DQL：数据查询语言，用于对数据进行查询，如select
> * DML：数据操作语言，对数据进行增加、修改、删除，如insert、udpate、delete
> * TPL：事务处理语言，对事务进行处理，包括begin transaction、commit、rollback
> * DCL：数据控制语言，进行授权与权限回收，如grant、revoke
> * DDL：数据定义语言，进行数据库、表的管理等，如create、drop
> * CCL：指针控制语言，通过控制指针完成表的操作，如declare cursor
* 重点是数据的crud（**增删改查**），必须熟练编写DQL、DML，能够编写DDL完成数据库、表的操作，其它语言如TPL、DCL、CCL了解即可
* SQL不区分大小写
## Redis
* 多用于存储缓存数据
## MongoDB
* 一般用于非关系型数据

## 免责声明
除去特别小的工作，你编写的代码应当方便他人阅读。能力往往伴随着责任，你 *有能力* 在 MySQL 中玩一些奇技淫巧并不意味着你应该去做！;)
* * *
## 常见问题
+ 
