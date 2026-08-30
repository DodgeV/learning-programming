# 🌍 命令行的艺术 · 学习笔记（整理版）

> **说明**：本文整理自《命令行的艺术》（[jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line)）中文学习笔记 `command.md`。整理方式：**保留全部原始链接、代码块与知识要点**；重排为带目录的分章结构，并为每节补充一句用途说明；可对比内容转为表格；修正明显笔误；适度补充缺失内容（以「✨ 整理补充」标注），原笔记留白处保留（以「📌 待补充」标注）。原文件 `command.md` 未改动。

---

## 📑 总目录

- [0. 总览](#0-总览)
- [1. 前言](#1-前言)
  - [1.1 涵盖范围](#11-涵盖范围)
  - [1.2 注意事项](#12-注意事项)
  - [1.3 参考教程与资源](#13-参考教程与资源)
- [2. 基础](#2-基础)
  - [2.1 Linux 目录结构](#21-linux-目录结构)
  - [2.2 基本命令与快捷键](#22-基本命令与快捷键)
  - [2.3 Bash 概况](#23-bash-概况)
  - [2.4 用户与权限管理](#24-用户与权限管理)
  - [2.5 IO 操作模型（select / epoll / 同步异步 / 阻塞非阻塞）](#25-io-操作模型select--epoll--同步异步--阻塞非阻塞)
  - [2.6 进程管理](#26-进程管理)
  - [2.7 性能优化](#27-性能优化)
  - [2.8 打包压缩](#28-打包压缩)
- [3. Vim 编辑器](#3-vim-编辑器)
  - [3.1 打开文件与编辑模式](#31-打开文件与编辑模式)
  - [3.2 移动光标](#32-移动光标)
  - [3.3 文本选择](#33-文本选择)
  - [3.4 删除与复制粘贴](#34-删除与复制粘贴)
  - [3.5 撤销与查找替换](#35-撤销与查找替换)
  - [3.6 保存与退出](#36-保存与退出)
  - [3.7 分屏与多行注释](#37-分屏与多行注释)
- [4. Git 版本控制](#4-git-版本控制)
  - [4.1 GitHub 基础概念](#41-github-基础概念)
  - [4.2 git 三区域](#42-git-三区域)
  - [4.3 本地仓库操作流程](#43-本地仓库操作流程)
  - [4.4 远程仓库管理](#44-远程仓库管理)
  - [4.5 搭建个人网页](#45-搭建个人网页)
  - [4.6 软件包管理（apt 等）](#46-软件包管理apt-等)
- [5. 日常使用](#5-日常使用)
- [6. 文件及数据处理](#6-文件及数据处理)
- [7. 网络调试](#7-网络调试)
- [8. 单行脚本](#8-单行脚本)
- [9. 冷门但有用](#9-冷门但有用)
- [10. 仅限 OS X 系统](#10-仅限-os-x-系统)
- [11. 仅限 Windows 系统](#11-仅限-windows-系统)
  - [11.1 在 Windows 下获取 Unix 工具](#111-在-windows-下获取-unix-工具)
  - [11.2 使用 Windows 命令行](#112-使用-windows-命令行)
  - [11.3 Cygwin 注意事项](#113-cygwin-注意事项)
  - [11.4 在 Windows 下使用 PowerShell](#114-在-windows-下使用-powershell)
- [12. 免责声明与授权条款](#12-免责声明与授权条款)

---

## 0. 总览

> **本节用途**：说明本笔记的定位——Linux 命令行的快速参考，本文后续各章均在此基础上展开。

![png](https://github.com/jlevy/the-art-of-command-line/blob/master/cowsay.png)

熟练使用命令行是一种常常被忽视，或被认为过时的技能，但实际上，它可以让你以更快的速度完成任务。本篇文章是你在 Linux 上使用命令行时的一个快速参考。其中包含了一些你要学习的基础和技能。有一些命令有重叠，但你其实不需要掌握所有的命令。

这篇文章是[值得学习及认可](AUTHORS.md)的成果。以下的章节按[难易程度](http://www.quora.com/What-are-some-lesser-known-but-useful-Unix-commands)、[入门](http://www.quora.com/What-are-the-most-useful-Swiss-army-knife-one-liners-on-Unix)与[时间节省技巧](http://www.quora.com/What-are-some-time-saving-tips-that-every-Linux-user-should-know)（Quora 上）整理，在 GitHub 上也有很多人对这篇文章进行过修改。如果你想在你的笔记中看到或使用这些命令，请[遵循贡献指南](CONTRIBUTING.md)（✨ 原笔记此处转写有误，已修正为"遵循贡献指南"）。

---

## 1. 前言

> **本节用途**：说明本文的涵盖范围、注意事项，并汇总学习该主题的参考教程与工具资源。

### 1.1 涵盖范围

- 这篇文章不是要教你全部的命令行，而是要帮助你掌握最核心的部分。本文基于 Linux，但很多内容同样适用于 [仅限 OS X 系统](#10-仅限-os-x-系统)和 [仅限 Windows 系统](#11-仅限-windows-系统)章节中也有相关说明。除这两章外，本文的内容也大多适用于 Unix 系统或 OS X，比如考虑 Cygwin 中也可以使用。
- 本文不是要篇幅很大的 Bash，但也还有很多技能可以使用到其他 shell 和 Bash 脚本中去。
- 本文讲到的"核心的" Unix 命令，本文也整理了一些针对常见问题的命令（前面是它们具有普遍性的）。

### 1.2 注意事项

- 对于要在一定内存较大的场景，一个实用的做法可以在文档中找到。我们注意到你准备要使用的 Google 或其他的问题搜索来找到更详细的命令。文中主要命令可以使用 `apt-get`、`yum`、`dnf`、`pacman`、`pip` 或 `brew`（以及其它系统的安装方式）来安装对应的方法。
- 遇到问题时，欢迎使用 [Explainshell](https://explainshell.com/)和[Linux命令大全](https://man.linuxde.net/) 查看解析命令、参数、命令的详细信息。

### 1.3 参考教程与资源

**视频教程（B 站）**

- [鸟哥的Linux私房菜](https://www.bilibili.com/video/av18156598)
- [Linux入门教程与从入门到精通](https://www.bilibili.com/video/BV12Z4y1M7dL)
- [狂神Linux中](https://www.bilibili.com/video/av22025899)&[p7](https://www.bilibili.com/video/av28534854)
- [狂神Linux下](https://www.bilibili.com/video/av22588048)
- [狂神day1](https://www.bilibili.com/video/av8012017)
- [狂神day2](https://www.bilibili.com/video/av8012272)
- [狂神day3](https://www.bilibili.com/video/av8012998)
- [狂神进阶](https://www.bilibili.com/video/av22912632)

**图文与工具资源**

- [awesome-shell](https://github.com/alebcay/awesome-shell)：一个分类整理的命令行工具和资源的清单。
- [awesome-osx-command-line](https://github.com/herrbischoff/awesome-osx-command-line)：一个针对 OS X 命令行的很好的入门。
- [Strict mode](http://redsymbol.net/articles/unofficial-bash-strict-mode/)：了解更好的脚本文件。
- [shellcheck](https://github.com/koalaman/shellcheck)：一个静态 shell 脚本检测工具，本质上就是 bash/sh/zsh 的 lint。
- [Filenames and Pathnames in Shell](http://www.dwheeler.com/essays/filenames-in-shell.html)：含有关于在 shell 脚本中如何正确处理文件名的注意事项。
- [Data Science at the Command Line](http://datascienceatthecommandline.com/#tools)：用于数据科学的命令与工具，适用于许多领域。

---

## 2. 基础

> **本节用途**：掌握 Linux 系统的目录结构、常用基本命令、用户权限管理、IO 操作模型、进程管理、性能优化与打包压缩，是使用命令行的地基。

### 2.1 Linux 目录结构

> 原笔记要点：Linux 系统本身是多人使用的，可以创建用户，还有一套权限系统。常见目录及其用途如下表。

| 目录 | 用途 |
| --- | --- |
| `/bin` | 保存了系统基础的二进制文件，文件都是可以被执行的 |
| `/home` | 保存用户下的文件，用户自己的目录，相当于 Windows 中的 `Users/` 目录 |
| `/root` | root 用户的目录 |
| `/etc` | 保存系统配置文件 |
| `/boot` | 保存 linux 系统启动所需的文件，还存 Linux 文件（壳），名称大小写敏感 |
| `/Dev` | 保存设备接口，比如 U 盘、磁盘的设备文件；在它们中的设备接口不一定能直接使用，可能需要手动挂载（类似于 Windows 下的磁盘设备） |
| `/Proc` | 保存了 Linux 运行时的进程信息 |
| `/Sbin` | 保存了一些可执行的二进制文件，但需要有 super 权限才能执行 |
| `/Tmp` | 保存了系统运行时的临时文件，类似于 Windows 中的 `C:/windows/Temp` |
| `/Usr` | 保存用户安装的应用程序，类似于 Windows 中的 `Program Files/` |
| `/Usr/bin` | 最重要的一个应用程序目录 |
| `/Usr/sbin` | 管理员用的一个命令方案 |
| `/Var` | 保存了日志/系统的数据文件 |
| `/mnt` | 保存设备接口挂载点 |

**路径与目录操作**

- `cd ~` 或 `cd /home` 进入用户目录；`cd -` 在最近两个目录之间切换。
- 相对路径使用 `/` 或 `~` 开头；使用 `..` 可以返回上一级目录，`../..` 可以返回上上级目录。

### 2.2 基本命令与快捷键

> 命令行基础操作：补全、翻页、光标移动、时间日期、关机重启等。

- `TAB` 创建一个命令补全，再创建一个 `TAB` 可以显示可用的命令。
- 上下键翻页查看命令，上键使用 `ctrl`+`p` 实现，下键使用 `ctrl`+`n` 实现。
- `ctrl`+`c` 取消当前的操作 / 不执行下一个命令 / 清除命令行。
- `ctrl`+`u` 删除光标位置前的内容，`ctrl`+`k` 删除光标位置后的内容。
- `ctrl`+`a` 将光标移到命令行中的最前面。
- `clear` 清空屏幕中的内容。
- `date` 查看系统当前时间。
- `cal` 查看本月的日历，`-y` 查看一年的日历。

**关机与重启**

| 命令 | 作用 |
| --- | --- |
| `shutdown` | 关闭一台服务器或关机 |
| `shutdown -r now` | 重启 |
| `shutdown +10` | 10 分钟后关机 |
| `shutdown 20:10` | 系统将在晚上 20:10 关机 |
| `shutdown -c` | 取消关机 |

### 2.3 Bash 概况

> ✨ 整理补充：原笔记此段转写较乱，以下按原意整理为清晰要点。

- 准备好后，在命令行中输入 `man bash` 可以进行更多的了解。
- 下面的 shell 也可以使用，但 Bash 的优势逐渐变得更流行；也可以了解 zsh、fish 或其他的 shell 的特点（如 `*` 通配等），在已有的配置中可以更加灵活。
- 查看命令帮助的两种格式：`man command` 或 `command --help`（注意不同命令的参数并不统一）。
- 可以使用 `apropos` 来查找命令。
- 如果命令不多也不常用，或者是 Bash 内置的，可以使用 `help` 和 `help -d` 命令查看相关命令。
- 你可以使用 `type` 来查看这个命令到底是文件还是 shell 内置命令。

### 2.4 用户与权限管理

> **本节用途**：Linux 是多用户系统，理解用户、组与权限，才能安全地管理文件和执行特权命令。

**权限基本概念**

> 原笔记要点：用户是 Linux 系统中需要的一条命令，用户以不相同的文件权限可以不同（r 读、w 写、x 执行）。如果遇到了权限问题，就是出现了问题；之前的权限仍有备份，不同的用户又进入到不同的组中。

| 命令 | 说明 |
| --- | --- |
| `chmod +/- r/w/x 目录名/文件名` | 修改权限。一个目录要拥有执行权限 `x` 才能进入目录，否则不能查看目录内容；`r` 和 `w` 可以互相搭配使用，和修改目录的执行权限；`s` 进入之后才可执行 |
| `chmod [-R] 755 文件名/目录名` | 3 个数字分别对应拥有者/组/其他用户的权限，`-R` 表示进入之后包含的所有文件 |
| `r`-4，`w`-2，`x`-1 | 三组权限可以组合 |
| 755 | user=rwx  group=rx  other=rx |
| 管理员用户 | root 属于用户组，用户需要运行系统相关的任务时，命令前面加 `sudo` 进入一次命令，超时 5 分钟 |
| `sudo groupadd 组名` | 创建组 |
| `sudo groupdel 组名` | 删除组 |
| `cat -n /etc/group` | 查看所有组以及成员权限，组字段 |

**用户与组管理命令**

| 命令 | 说明 |
| --- | --- |
| `cat -n /etc/group \| grep xzc` | 查看 xzc 组的信息以及所有 xzc 用户的所在组 |
| `chgrp -R 组名 文件名/目录名` | 修改文件/目录的所有组 |
| `chown 用户名 文件名/目录名` | 修改拥有者 |
| `sudo useradd [-m] [-g 所有组] 用户名` | `-m` 创建用户的同时创建目录（无需密码即可登录），`-g` 修改用户所有组；若要删除用户需要先删除 |
| `sudo passwd 用户名` | 设置用户密码。如果不设置密码，就无法使用 ssh 登录；修改用户密码的方式保存在 `/usr/bin/passwd` 中 |
| `cat -n /etc/passwd` | 查看所有用户的信息 |
| `cat -n /etc/passwd \| grep xzc` | 在文件中查询 xzc 用户的信息 |
| `passwd` 文件字段 | 每行由 7 个字段组成：用户名 : 密码（x 隐藏的密码）: 用户ID : 组ID : 用户全名或主机名 : 用户根目录 : 登录使用的 Shell |
| `sudo userdel -r 用户名` | 删除用户，`-r` 指定删除目录 |
| `id [用户名]` | 查看用户的用户组以及所属组和所有管理组的字段 |
| `who` | 查看当前所有登录的用户 |
| `whoami` | 查看当前用户当前用户名 |
| `sudo usermod -g 组名 用户名` | 修改用户的所属组 |
| `sudo usermod -G 管理组名 用户名` | 将用户加入管理组或加入权限 |
| `sudo usermod -s /bin/bash 用户名` | 修改用户登录的 shell（用户登录目录的 shell 是 dash，root 用户的 shell 是 bash） |
| `which ls` / `which passwd` | 查看执行命令所在的位置（如 `which passwd` → `/usr/bin/passwd`） |

> ✨ 补充：如果需要创建的用户没有权限使用 sudo，可以使用 `sudo usermod -G sudo XX` 将 XX 加入 sudo 管理组获得权限。

**切换用户**

- `su 用户名`：切换用户，`-` 可以切换到用户的目录。
- `su -`：不切换用户直接切换到 root 用户（并不是退出）；下一次切换 root 用户需要 `sudo passwd root` 修改 root 密码。
- `exit`：退出当前用户。

### 2.5 IO 操作模型（select / epoll / 同步异步 / 阻塞非阻塞）

> ✨ 整理补充：原笔记此段转写较乱，以下按原意整理为清晰要点。

- `select`：一个 socket 连接可以负责一个文件的操作；socket 可以实现多次复用，通常采用 `select` 方法可以监听所有的 socket，最大 1024 个。
- `epoll`：只需要监听需要监听的 socket（对 select 的改进）。
- **同步**：一个连接执行一个数据读写或网络操作时，必须等待本次操作完成之后才能进行其他操作。
- **异步**：异步的问题由操作系统来帮你解决，不需要使用者关注；多个连接时，操作系统可以同时执行多个数据读写操作。
- **同步/异步是通知机制的区别**：处理方在数据就绪之后会进行回调并返回数据；数据越多就越占用回调的时间。
- **阻塞/非阻塞是发起处理的方式**：处理方在数据没有准备好的情况下，请求未被完成时立刻返回。阻塞的问题在于：发起一个请求后，请求会一直等待完成才能返回，在等待期间无法处理其他事件（比如其他请求），所以当请求被阻塞时，无法处理其他请求。
- 阻塞非阻塞与同步异步是两码事，一个请求可以只等待阻塞非阻塞。
- `iostat`：查看磁盘信息。

### 2.6 进程管理

> **本节用途**：掌握查看、控制进程的方法，并理解进程信号、僵尸进程与孤儿进程的概念。

**进程查看与控制**

- 在 Linux 中运行进程：`init`（initialize，首进程），进程 ID 为 1，是系统启动后第一个执行的进程；查询系统运行的服务：`inittab`（系统运行级别配置，CentOS6 在 `/etc/inittab`，CentOS7 改在 `/usr/lib/systemd/system/ctrl-alt-del.target`）。
- `ps [aux]`：查看进程的运行状况，指定查看当前用户运行的进程；`a` 显示查看其他用户的进程；`u` 显示进程的详细信息；`x` 显示所有有处理机状态的进程。
- `ps -l`：查看当前的进程。
- `ps -ef | grep init`：查看 `init` 的进程。
- `pstree -A`：查看进程树。
- `top`：动态显示运行中 CPU 和内存占用最多的进程，`q` 退出。
- `netstat`：查看网络与端口。
- `kill [-9] 进程号`：杀死进程，`-9` 强制杀死进程；如果不需要杀死当前用户的进程，可以强杀 root 用户启用的进程。

**进程信号**

> 原笔记要点如下表：

| 状态/信号 | 说明 |
| --- | --- |
| R | 运行中 |
| D | 不可中断的，就是 IO 操作 |
| S | 可中断睡眠，还能处理其他事情 |
| Z | 停止的进程：进程已经被停止，但是它的父进程没有处理（回收）资源 |
| T | 暂停 |
| SIGCHLD | 当父进程退出时，进程信号会退出；如果有几个（子进程）都在父进程里 |
| 1 | 挂起 SIGHCLD 信号 |
| 2 | waitpid() 或 wait() 系统调用返回 |

**僵尸进程**

> 一个僵尸进程已经开始退出或都在运行，这个僵尸进程被停止，它变成了僵尸进程。僵尸进程将被 init 进程收养，都可以被回收，但不可以被终止。

**孤儿进程**

> 当父进程退出，父进程的子进程还在运行，然后它被 init 进程收养，即变成孤儿进程，然后被 init 进程回收。

> ✨ 整理补充（原笔记要点归纳）：如果父进程没有执行 `wait()`，子进程结束以后不能正确退出，父进程就产生了僵尸进程；此时僵尸进程不能使用 `wait()` 退出，则被 init 进程收养；孤儿进程被 init 进程回收。孤儿进程的父进程变成 init（PPID=1）。fork 一次，子进程创建了僵尸进程，僵尸进程再创建子进程，依次……（📌 原笔记该处内容不完整，此句为要点归纳）。

### 2.7 性能优化

> **本节用途**：当系统或 Java 应用出现 CPU/内存/IO 占用过高时，用以下命令定位占用资源的进程与线程。

- 查看占用资源的进程：用 `top` 和 `jstack` 命令
  - `top` 查看进程列表
  - `top -Hp pid` 查看进程线程
  - `jstack pid | grep -A 200 线程id`
  - `pidstat` 命令：可以监控单个进程的 IO、CPU、内存等数据
    - `pidstat -u 1`：CPU
    - `pidstat -r 1`：内存
    - `pidstat -d 1`：IO
- 查看 Java 线程信息
  - 用 `jps` 查看启动的 Java 进程
  - 使用 `jstack` 查看线程的信息
  - CPU 使用率较高，但 top 看不到线程的后面时间有几个（📌 原笔记此处表述不完整）
  - 问题线程很多，比如使用不对应的（JDK 工具）问题（📌 原笔记此处表述不完整）

### 2.8 打包压缩

> **本节用途**：三种操作系统使用的压缩格式 `Windows`--`rar`，`Mac`--`zip`，`Linux`--`tar/gz`；掌握 gzip / bzip2 / tar 的打包压缩与解压解包命令。

**gzip 压缩**

- `gzip -cv filename`：压缩。
- `gzip -d filename`：解压。
- 可以使用 `zcat`、`zmore` 查看压缩文件。

**bzip2 压缩**

- `bzip2 [-cdzv] filename`：其中多了一个 `k` 保留原压缩文件（✨ 原笔记此处表述不清，指 `-k` 参数可保留原文件）。
- 可以使用 `bzip2cat`、`bzmore`、`bzcat`、`bzless`、`bzgrep` 查看压缩文件内容。

**tar 打包压缩**

| 命令 | 说明 |
| --- | --- |
| `tar -cvf 打包文件.tar 要打包的文件或目录` | 打包（多个文件使用空格分隔）。常用参数：`c` 创建、`v` 显示详细信息、`f` 使用文件名、压缩时不使用压缩） |
| `tar -xvf 打包文件.tar` | 解包 |
| `tar -zcvf 打包压缩文件.tar.gz 要打包压缩的文件或目录` | 对文件或目录进行打包压缩（gzip） |
| `tar -zxvf 解压文件.tar.gz [-C 指定目录]` | 解压（gzip），解压到当前目录即可，`-C` 指定目录 |
| `tar -jcvf 打包压缩文件.tar.bz2 要打包压缩的文件或目录` | 打包压缩（bzip2 算法） |
| `tar -jxvf 解压文件.tar.bz2 [-C 指定目录]` | 解压（bzip2 算法），`-C` 指定的目录要存在才会解压 |


---

## 3. Vim 编辑器

> **本节用途**：Vim（`vi`）是 Linux 系统上最常用的文件编辑器，掌握其模式切换、光标移动、编辑、删除、撤销、查找替换、保存退出与分屏等操作，即可高效编辑文件。

> 原笔记要点：熟练记住一个对文件系统的编辑器。再就是 Vim（`vi`）就是你最好的选择，可以在系统上编辑文件时 Vim 是最常用的编辑器（熟悉大部分功能下，Vim 需要 Emacs、大号 IDAE 或是学习编辑器的实用——📌 原笔记此处表述不清）。

### 3.1 打开文件与编辑模式

- 创建文件：创建其实是打开，打开就是创建；删除文件用 `rm`，删除 vim 可编辑文件时使用 swap（📌 原笔记此处表述不清）。
- 如果是不能创建目录，需要在 `vimrc` 文件中修改。

**进入/退出编辑模式**

| 按键 | 作用 |
| --- | --- |
| `i` | 进入编辑模式，在当前字符前插入；按 `esc` 退出编辑模式 |
| `I` | 在行首插入 |
| `o` | 在当前行下方新开一行并进入编辑模式 |
| `O` | 在当前行上方新开一行并进入编辑模式 |
| `a` | 进入追加模式（当前字符后追加），按 `esc` 退出 |
| `A` | 在当前行的末尾追加 |
| `esc` | 退出编辑模式，回到命令行模式 |

> 原笔记补充：第 5 行修改编辑使用——`i` 进入在当前字符前插入文件，`I` 在行首插入文件，小写 `o` 在下一行插入一行，大写 `O` 在上一行插入一行，`A` 在行末追加文件，`a` 在当前字符后追加文件。（✨ 与上表内容一致，已合并去重）

**打开文件时的定位**

- `vi 文件名 +行数`：创建文件时定位到某行；或创建文件后在命令行输入 `+` 定位到末行。
- `vi 文件名 +`：定位到最后一行的下一行，或使用 `+` 定位到最后一行。
- 一创建就已经是命令行模式，可用操作、移动、编辑等。

### 3.2 移动光标

| 按键 | 作用 |
| --- | --- |
| `h` / `j` / `k` / `l` | 左移 / 下移 / 上移 / 右移一个字符 |
| `w` | 移动到下一个单词的首字母 |
| `e` | 移动到当前单词的末尾 |
| `b` | 移动到上一个单词的首字母 |
| 数字+`h`/`j`/`k`/`l` | 按数字移动键位 |
| `0` | 移动到行首 |
| `^` | 移动到行首第一个不是空白的字符 |
| `$` | 移动到行尾 |
| `gg` | 移动到文件第一行 |
| `G` | 移动到文件最后一行 |
| `行号+G/gg` 或 `:+行号` | 跳转到指定行 |
| `H` / `M` / `L` | 跳转到屏幕顶端 / 中间 / 屏幕底端 |
| `{` / `}` | 跳转到上一段 / 下一段 |
| `%` | 在括号中切换匹配的括号 |
| `'x'` | 跳转到以后的标记 |
| `Ctrl+b` / `Ctrl+f` | 向上翻页 / 向下翻页 |
| `Ctrl+d` | 向下翻半页 |

### 3.3 文本选择

| 按键 | 作用 |
| --- | --- |
| `v` | 进入可视模式，选择文本 |
| `V` | 进入行可视模式，选择整行 |
| `ctrl+v` | 进入块可视模式，选择块（可配合 `h`/`j`/`k`/`l` 上下左右选中文件） |

> 进入 `v` 进入可视模式，进入命令行模式后退出可重新进入；`V` 进入行可视模式，要复制整行时使用，可以与其他编辑命令组合使用；`ctrl`+`v` 进入块可视模式，可以按上下进行选中文件，可以与编辑命令组合使用。

### 3.4 删除与复制粘贴

**删除**

| 按键 | 作用 |
| --- | --- |
| `x` | 删除光标后的字符 |
| `X` | 删除光标前的字符 |
| `dd` | 删除 1 行（可以与其他编辑命令组合使用），删除当前行并光标移动 |
| `D` | 删除光标至行尾的内容 |
| 行号删除 | 通过命令行输入行号，进入该功能删除哪行/多行 |

**复制粘贴**

| 按键 | 作用 |
| --- | --- |
| `y` | 复制，可以与其他编辑命令组合使用 |
| `yy` | 复制 1 行 |
| `yny` | 复制 n 行 |
| `p` | 粘贴 |

> 原笔记补充：删除文件后若已经保存，可以直接恢复，将恢复的文件属性部分替换原有文件删除（📌 原笔记此处重复且表述不清，疑似描述 vim 的 `:e!` / swap 恢复机制）。

### 3.5 撤销与查找替换

**撤销**

- `u`：撤销。
- `ctrl+r`：撤销撤销（重做）。

**查找**

- `/内容` 然后回车进行搜索。
- `n` 跳转到下一处匹配；`N` 跳转到上一处匹配；`#` 跳转到上一处匹配。

**替换**

| 命令 | 作用 |
| --- | --- |
| `r` | 替换当前字符 |
| `:s/旧内容/新内容` | 替换单行 |
| `:%s/旧内容/新内容/g` | 替换多行 |
| `:s/文件/内容/gc` | 强制保存（✨ 原笔记此处为 `:s/文件/内容/gc`，疑为 `%s/旧/新/gc` 的笔误，`gc` 表示替换前逐一确认） |

### 3.6 保存与退出

- 进入 `:` 进入命令行模式，`:w 文件名`：新建文件。

| 命令 | 作用 |
| --- | --- |
| `:w` | 保存；同时也可以保存到当前文件，如果保存到当前文件则不能退出 |
| `:q` | 退出 |
| `:q!` | 强制退出 |
| `:wq` 或 `:x` | 保存并退出 |
| `:e 文件名` | 创建并打开新文件；如果使用 `.` 创建目录当前目录下的所有文件 |
| `:sp 文件名` | 上下分屏打开文件；也可以使用 `.` 创建当前目录下的所有文件 |
| `:vsp 文件名` | 左右分屏打开文件；也可以使用 `.` 创建当前目录下的所有文件 |

### 3.7 分屏与多行注释

**分屏操作**

- 多行注释使用 `ctrl`+`w` 分屏；分屏的命令可以同时有多个。
- `r` 可以切换窗口；`c` 关闭其他窗口；`q` 退出当前窗口；`o` 关闭其他窗口。
- 注意分屏文件名的前面保持保存新建文件（📌 原笔记此处表述不清）。

**多行注释**

- 使用 `ctrl`+`v` 进入块可视，选择要注释的行，`0` 定位到行首，再输入大写的 `I` 插入多行注释，按 `esc` 保存退出。

---

## 4. Git 版本控制

> **本节用途**：使用 `git` 版本控制系统并配合 GitHub 远程仓库，实现代码的版本管理与多人协作。

> 原笔记要点：版本控制系统工具是 `git`，配合 GitHub 远程仓库管理。

### 4.1 GitHub 基础概念

> + [Git教程（从入门到精通）](https://www.bilibili.com/video/BV1sJ411D7xN)

- **仓库（Repository）**：仓库是在本地建立的一个目录，每一个目录都是独立的一个仓库。
- **提交（Commit）**：每一次修改文件，都会 `Commit changes`，都可以进入提交的信息，可以看到每次修改。
- 输入 `Go to file` 可以查看仓库中的文件。
- **发布 Issues（问题）**：发布 bug，但没有什么结果的时候可以使用，或者使用工具去搜索使用。
- **Pull Request**：将 Forked 的仓库修改好的代码提交到原仓库中，最后可以提交流程提交。
- 使用命令行 `git` 配置 GitHub，如果需要了解[下载](https://www.git-scm.com/download)进去。

### 4.2 git 三区域

- **git repository（Git 仓库）**：储存最新版本的修改在仓库中，建立了一个全新的版本。
- **工作区**：工作区已经被修改的文件在仓库的修改（📌 原笔记此处表述不清）。
- **暂存区**：暂存区可以多次修改的文件，不需要一次提交到 git 仓库中。
- **修改区（Working Directory）**：创建、编辑、修改文件已经完成。

### 4.3 本地仓库操作流程

> 在仓库添加文件的过程：

1. 检查配置信息，检查用户名：`git config --global user.name 'XXX'`；设置用户名昵称：`git config --global user.name 'XX'`；还是可以查看配置：`git config list`。
2. 创建或编辑一个 git 文件先，然后 `cd` 进入该文件目录。
3. `git init` 初始化 git，将当前目录或目录完成一个新的版本仓库，然后再建立一个不需要上传的文件。
4. `git status` 查看当前三个仓库的状态。
5. `git add [文件名]` 将文件添加进暂存区；`git reset -- [文件名]` 或 `git rm --cached [文件名]` 取消暂存区修改；如果不加文件名就是取消所有修改。
6. `git status` 再次查看状态，再使用 `git diff` 查看工作区被修改文件的内容修改情况；`git diff --cached` 查看暂存区中的修改。
7. `git commit -m '提交信息'` 将文件提交到仓库，然后进行提交信息。
8. 需要修改文件，需要先在本地修改，然后再更新提交。
9. 如果需要删除文件，需要先在本地删除，然后再 `git rm XX` 和 git 删除文件，最后 `git commit -m '提交信息'` 提交到仓库。

### 4.4 远程仓库管理

- `git clone [仓库地址]`：克隆仓库，下载到当前目录下；仓库的文件夹中含有一个 `.git` 隐藏文件夹，里面包含所有仓库信息，不能删除。
- `git clone -o [仓库地址] [自定义名]`：克隆远程仓库时，也可以修改文件名。
- 克隆一个仓库到本地，本地仓库就会与远程仓库关联；`git remote` 命令用于管理本地仓库与远程仓库信息，一个本地仓库可以关联多个仓库。
- 运行 `git remote -v` 命令可以查看本地仓库关联的远程仓库信息。
- `git push`：将本地提交到远程仓库。
- `vi .git/config`：修改 remote 信息。

### 4.5 搭建个人网页

- 创建名字为 `[用户名].github.io` 的仓库：`https://[用户名].github.io`。
- 1. 创建名字为 `[用户名].github.io` 的仓库。
- 2. 在仓库里新建一个名为 `index.html` 文件。
- 注意：仓库必须是 `html` 文件（📌 原笔记此处表述不清，指仓库中需要放 html 文件）。
- 搭建个人网页步骤（使用 `setting` 部分）：
  1. 在仓库的 `settings` 页面找到 `setpages` 部署。
  2. 新建仓库名称和描述信息。
  3. 点击新建完成后生成网页。

### 4.6 软件包管理（apt 等）

> 了解使用 `apt-get`、`yum`、`dnf` 或 `pacman`（取决于你使用的 Linux 发行版）安装或移除软件，了解你的发行版中的 `pip` 来安装关于 Python 的命令行工具（动手前多了解用的发行版来使用 `pip` 会很合适）。

| 命令 | 说明 |
| --- | --- |
| `sudo apt install 软件名` | 安装软件 |
| `sudo apt remove 软件名` | 卸载软件 |
| `sudo apt upgrade` | 更新所有软件 |

> 软件包 ===> 软件

> 原笔记附：Ubuntu 阿里云镜像源配置（`/etc/apt/sources.list` 示例）：

```
deb-src http://archive.ubuntu.com/ubuntu xenial main restricted #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted multiverse universe #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted multiverse universe #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe
deb http://mirrors.aliyun.com/ubuntu/ xenial multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse #Added by software-properties
deb http://archive.canonical.com/ubuntu xenial partner
deb-src http://archive.canonical.com/ubuntu xenial partner
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted multiverse universe #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-security multiverse
```


---

## 5. 日常使用

> **本节用途**：覆盖日常操作命令行时最常用的技能——重定向、补全、历史记录、任务管理、脚本调试、变量展开、SSH 等，是"用得最多"的一章。

### 5.1 重定向与管道

- 学会使用 `>` 和 `<` 来重定向输出和输入，学会使用 `|` 来重定向管道。明白 `>` 会覆盖输出文件，而 `>>` 是在文件末添加。了解标准输出 stdout 和标准错误 stderr。

> 原笔记示例：

> * `tree >> a`：把要在终端中显示的树状图追加到文件 a 中
> * `ls -lha ~ | more`：第一个命令的输出作为第二个命令的输入，分屏显示家目录的所有文件夹
> * `ls -lha ~ | grep vi`：利用管道，查询所有名字中含有 vi 的文件（夹）
> * `echo hello`：把 hello 打印在终端中
> * `echo hello python > a`：把 hello python 保存到文件 a 中，没有则新建一个

### 5.2 通配符与引用

- 学会使用通配符 `*`（或许再算上 `?` 和 `[`...`]`）和引用，以及引用中 `'` 和 `"` 的区别（后文中有一些具体的例子）。

### 5.3 正则表达式与 grep

- 熟悉正则表达式，学会使用 `grep`／`egrep`，它们的参数中 `-i`、`-o`、`-v`、`-A`、`-B` 和 `-C` 这些是很常用并值得认真学习的。

### 5.4 任务管理

- 熟悉 Bash 中的任务管理工具：`&`，**ctrl-z**，**ctrl-c**，`jobs`，`fg`，`bg`，`kill` 等。

### 5.5 命令行编辑与历史记录

- 在 Bash 中，可以通过按 **Tab** 键实现自动补全参数；使用 **ctrl-r** 搜索命令行历史记录（按下按键之后，输入关键字便可以搜索，重复按下 **ctrl-r** 会向后查找匹配项，按下 **Enter** 键会执行当前匹配的命令，而按下右方向键会将匹配项放入当前行中，不会直接执行，以便做出修改）。
- 在 Bash 中，可以按下 **ctrl-w** 删除你键入的最后一个单词，**ctrl-u** 可以删除行内光标所在位置之前的内容，**alt-b** 和 **alt-f** 可以以单词为单位移动光标，**ctrl-a** 可以将光标移至行首，**ctrl-e** 可以将光标移至行尾，**ctrl-k** 可以删除光标至行尾的所有内容，**ctrl-l** 可以清屏。键入 `man readline` 可以查看 Bash 中的默认快捷键。内容有很多，例如 **alt-.** 循环地移向前一个参数，而 **alt-*** 可以展开通配符。
- 你喜欢的话，可以执行 `set -o vi` 来使用 vi 风格的快捷键，而执行 `set -o emacs` 可以把它改回来。
- 为了便于编辑长命令，在设置你的默认编辑器后（例如 `export EDITOR=vim`），**ctrl-x** **ctrl-e** 会打开一个编辑器来编辑当前输入的命令。在 vi 风格下快捷键则是 **escape-v**。
- 键入 `history` 查看命令行历史记录，再用 `!n`（`n` 是命令编号）就可以再次执行。其中有许多缩写，最有用的大概就是 `!$`，它用于指代上次键入的参数，而 `!!` 可以指代上次键入的命令了（参考 man 页面中的 "HISTORY EXPANSION"）。不过这些功能，你也可以通过快捷键 **ctrl-r** 和 **alt-.** 来实现。
- 如果你输入命令的时候中途改了主意，按下 **alt-#** 在行首添加 `#` 把它当做注释再按下回车执行（或者依次按下 **ctrl-a**、**#**、**enter**）。这样做的话，之后借助命令行历史记录，你可以很方便恢复你刚才输入到一半的命令。

### 5.6 目录与路径

- `cd` 命令可以切换工作路径，输入 `cd ~` 可以进入 home 目录。要访问你的 home 目录中的文件，可以使用前缀 `~`（例如 `~/.bashrc`）。在 `sh` 脚本里则用环境变量 `$HOME` 指代 home 目录的路径。
- 回到前一个工作路径：`cd -`。

### 5.7 xargs 与并行执行

- 使用 `xargs`（或 `parallel`）。他们非常给力。注意到你可以控制每行参数个数（`-L`）和最大并行数（`-P`）。如果你不确定它们是否会按你想的那样工作，先使用 `xargs echo` 查看一下。此外，使用 `-I{}` 会很方便。例如：

```bash
      find . -name '*.py' | xargs grep some_function
      cat hosts | xargs -I{} ssh root@{} hostname
```

### 5.8 进程与后台任务

- `pstree -p` 以一种优雅的方式展示进程树。
- 使用 `pgrep` 和 `pkill` 根据名字查找进程或发送信号（`-f` 参数通常有用）。
- 了解你可以发往进程的信号的种类。比如，使用 `kill -STOP [pid]` 停止一个进程。使用 `man 7 signal` 查看详细列表。
- 使用 `nohup` 或 `disown` 使一个后台进程持续运行。

### 5.9 端口与网络检查

- 使用 `netstat -lntp` 或 `ss -plat` 检查哪些进程在监听端口（默认是检查 TCP 端口；添加参数 `-u` 则检查 UDP 端口）或者 `lsof -iTCP -sTCP:LISTEN -P -n`（这也可以在 OS X 上运行）。
- `lsof` 来查看开启的套接字和文件。
- 使用 `uptime` 或 `w` 来查看系统已经运行多长时间。

### 5.10 别名与 shell 配置文件

- 使用 `alias` 来创建常用命令的快捷形式。例如：`alias ll='ls -latr'` 创建了一个新的命令别名 `ll`。
- 可以把别名、shell 选项和常用函数保存在 `~/.bashrc`，具体看下这篇[文章](http://superuser.com/a/183980/7106)。这样做的话你就可以在所有 shell 会话中使用你的设定。
- 把环境变量的设定以及登陆时要执行的命令保存在 `~/.bash_profile`。而对于从图形界面启动的 shell 和 `cron` 启动的 shell，则需要单独配置文件。
- 要想在几台电脑中同步你的配置文件（例如 `.bashrc` 和 `.bash_profile`），可以借助 Git。

### 5.11 处理含空格的文件名

- 当变量和文件名中包含空格的时候要格外小心。Bash 变量要用引号括起来，比如 `"$FOO"`。尽量使用 `-0` 或 `-print0` 选项以便用 NULL 来分隔文件名，例如 `locate -0 pattern | xargs -0 ls -al` 或 `find / -print0 -type d | xargs -0 ls -al`。如果 for 循环中循环访问的文件名含有空字符（空格、tab 等字符），只需用 `IFS=$'\n'` 把内部字段分隔符设为换行符。

### 5.12 Bash 脚本调试与严格模式

- 在 Bash 脚本中，使用 `set -x` 去调试输出（或者使用它的变体 `set -v`，它会记录原始输入，包括多余的参数和注释）。尽可能地使用严格模式：使用 `set -e` 令脚本在发生错误时退出而不是继续运行；使用 `set -u` 来检查是否使用了未赋值的变量；试试 `set -o pipefail`，它可以监测管道中的错误。当牵扯到很多脚本时，使用 `trap` 来检测 ERR 和 EXIT。一个好的习惯是在脚本文件开头这样写，这会使它能够检测一些错误，并在错误发生时中断程序并输出信息：

```bash
      set -euo pipefail
      trap "echo 'error: Script failed: see failed command above'" ERR
```

### 5.13 子 shell、大括号与 here documents

- 在 Bash 脚本中，子 shell（使用括号 `(...)`）是一种组织参数的便捷方式。一个常见的例子是临时地移动工作路径，代码如下：

```bash
      # do something in current dir
      (cd /some/other/dir && other-command)
      # continue in original dir
```

- 编写脚本时，你可能会想要把代码都放在大括号里。缺少右括号的话，代码就会因为语法错误而无法执行。如果你的脚本是要放在网上分享供他人使用的，这样的写法就体现出它的好处了，因为这样可以防止下载不完全代码被执行。

```bash
{
      # 在这里写代码
}
```

- 了解 Bash 中的 "here documents"，例如 `cat <<EOF ...`。

### 5.14 变量扩展与参数展开

- 在 Bash 中，变量有许多的扩展方式。`${name:?error message}` 用于检查变量是否存在。此外，当 Bash 脚本只需要一个参数时，可以使用这样的代码 `input_file=${1:?usage: $0 input_file}`。在变量为空时使用默认值：`${name:-default}`。如果你要在之前的例子中再加一个（可选的）参数，可以使用类似这样的代码 `output_file=${2:-logfile}`，如果省略了 $2，它的值就为空，于是 `output_file` 就会被设为 `logfile`。数学表达式：`i=$(( (i + 1) % 5 ))`。序列：`{1..10}`。截断字符串：`${var%suffix}` 和 `${var#prefix}`。例如，假设 `var=foo.pdf`，那么 `echo ${var%.pdf}.txt` 将输出 `foo.txt`。

### 5.15 括号扩展

- 使用括号扩展（`{`...`}`）来减少输入相似文本，并自动化文本组合。这在某些情况下会很有用，例如 `mv foo.{txt,pdf} some-dir`（同时移动两个文件），`cp somefile{,.bak}`（会被扩展成 `cp somefile somefile.bak`）或者 `mkdir -p test-{a,b,c}/subtest-{1,2,3}`（会被扩展成所有可能的组合，并创建一个目录树）。

### 5.16 进程替换

- 通过使用 `<(some command)` 可以将输出视为文件。例如，对比本地文件 `/etc/hosts` 和一个远程文件：

```sh
      diff /etc/hosts <(ssh somehost cat /etc/hosts)
```

### 5.17 重定向补充

- 在 Bash 中，同时重定向标准输出和标准错误：`some-command >logfile 2>&1` 或者 `some-command &>logfile`。通常，为了保证命令不会在标准输入里残留一个未关闭的文件句柄捆绑在你当前所在的终端上，在命令后添加 `</dev/null` 是一个好习惯。

### 5.18 编码与帮助手册

- 使用 `man ascii` 查看具有十六进制和十进制值的 ASCII 表。`man unicode`、`man utf-8`，以及 `man latin1` 有助于你去了解通用的编码信息。

### 5.19 终端复用与 SSH

- 使用 `screen` 或 [`tmux`](https://tmux.github.io/) 来使用多份屏幕，当你在使用 ssh 时（保存 session 信息）将尤为有用。而 `byobu` 可以为它们提供更多的信息和易用的管理工具。另一个轻量级的 session 持久化解决方案是 [`dtach`](https://github.com/bogner/dtach)。
- ssh 中，了解如何使用 `-L` 或 `-D`（偶尔需要用 `-R`）开启隧道是非常有用的，比如当你需要从一台远程服务器上访问 web 页面。
- 考虑使用 [`mosh`](https://mosh.mit.edu/) 作为 ssh 的替代品，它使用 UDP 协议。它可以避免连接被中断并且对带宽需求更小，但它需要在服务端做相应的配置。

### 5.20 ssh 配置优化

- 对 ssh 设置做一些小优化可能是很有用的，例如这个 `~/.ssh/config` 文件包含了防止特定网络环境下连接断开、压缩数据、多通道等选项：

```
      TCPKeepAlive=yes
      ServerAliveInterval=15
      ServerAliveCountMax=6
      Compression=yes
      ControlMaster auto
      ControlPath /tmp/%r@%h:%p
      ControlPersist yes
```

- 一些其他的关于 ssh 的选项是与安全相关的，应当小心翼翼的使用。例如你应当只能在可信任的网络中启用 `StrictHostKeyChecking=no`、`ForwardAgent=yes`。
- 获取八进制形式的文件访问权限（修改系统设置时通常需要，但 `ls` 的功能不那么好用并且通常会搞砸），可以使用类似如下的代码：

```sh
      stat -c '%A %a %n' /etc/timezone
```

### 5.21 交互式选取与实用工具

- 使用 [`percol`](https://github.com/mooz/percol) 或者 [`fzf`](https://github.com/junegunn/fzf) 可以交互式地从另一个命令输出中选取值。
- 使用 `fpp`（[PathPicker](https://github.com/facebook/PathPicker)）可以与基于另一个命令（例如 `git`）输出的文件交互。
- 将 web 服务器上当前目录下所有的文件（以及子目录）暴露给你所处网络的所有用户，使用：`python -m SimpleHTTPServer 7777`（使用端口 7777 和 Python 2）或 `python -m http.server 7777`（使用端口 7777 和 Python 3）。

### 5.22 用户权限切换与简易服务

- 以其他用户的身份执行命令，使用 `sudo`。默认以 root 用户的身份执行；使用 `-u` 来指定其他用户。使用 `-i` 来以该用户登录（需要输入*你自己的*密码）。
- 将 shell 切换为其他用户，使用 `su username` 或者 `sudo - username`。加入 `-` 会使得切换后的环境与使用该用户登录后的环境相同。省略用户名则默认为 root。切换到哪个用户，就需要输入*哪个用户的*密码。
- 了解命令行的[参数（Argument）限制](https://wiki.debian.org/CommonErrorMessages/ArgumentListTooLong)。使用通配符匹配大量文件名时，常会遇到 "Argument list too long" 的错误信息。（这种情况下换用 `find` 或 `xargs` 通常可以解决。）（✨ 原笔记此处缺失"参数"二字，已补全）

### 5.23 命令行计算器

- 当你需要一个基本的计算器时，可以使用 `python` 解释器（当然你要用 python 的时候也是这样）。例如：

```
>>> 2+3
5
```


---

## 6. 文件及数据处理

> **本节用途**：覆盖文件管理、文件系统、搜索、文本/格式转换、数据整理与批量处理等命令，是"对文件做增删改查与加工"的一章。

### 6.1 基本文件管理工具

> 原笔记要点（含大量手记示例）：

- `ls` 和 `ls -l`（了解 `ls -l` 中每一列代表的意义）：
  > - `ls -l` 最后一列是文件名，往前 3 列是修改时间月/日/时；第一列显示是否是文件：`-` 文件、`d` 文件夹、`l` 软（硬）链接；之后每 3 列分别是用户的权限、用户所属组的权限、其他用户的权限；之后的数字是硬连接数，即能够访问该文件（夹）的方法的个数，比如用绝对路径或 `.` 或 `..`，即子目录越多硬连接数越多，文件的硬连接数一般都是 1
  > - `ls -a` 查看隐藏文件，以 `.` 开头的文件为隐藏文件，蓝色为文件夹，白色为文件
  > - `ls -l` 以列表方式显示文件的详细信息，如果是目录第一列为 d，如果是文件第一列为 -
  > - `ls -lh` 将文件大小更直观的显示出来
  > - `*` 表示任意多个字符，`?` 表示任意单个字符，`[]` 匹配指定字符组
  > - `ls *3.txt` 显示以 3 结尾的 txt 文件
  > - `ls ?2?.txt` 显示文件名中有 2 的 txt 文件
  > - `ls [1-3]23.txt` 显示 1-3 开头的文件
  > - `less` 可以往前翻，加载部分，实时加载
  > - `head`
  > - `tail` 和 `tail -f`（甚至 `less +F`）
  > - `ln` 和 `ln -s`（了解硬链接与软链接的区别：`ln -s source dest` 建立文件的软链接，类似快捷方式，源文件 `source` 要使用绝对路径，不能使用相对路径，这样移动链接文件的位置后仍然能够正常使用；而 `ln source dest` 建立一个硬链接，即创建一个真实存在的文件，但共用一个 inode，两个文件占用相同大小的硬盘空间，工作中几乎不会建立文件的硬链接。如果删除源文件，硬链接不受影响，软链接会失效。在 Linux 中文件数据和文件名是分开存储在硬盘上的，软链接创建的是一个指向源文件名的路径，源文件名已删除则路径就断了；硬链接则是创建了指向源文件数据的路径，源文件名删除不会对该路径产生影响）
  > - `touch`：创建文件，可以写多个文件；如果文件已经存在则修改文件的末次修改时间
  > - `mkdir -p a1/a2/a3`：一次性连续创建目录，创建的目录和文件名不能重名
  > - `rm [-r] [-f]`：直接删除文件不能恢复，`-r` 删除文件夹，`-f` 强制删除文件不会有任何提示
  > - `tree [-d]`：以树状图的形式显示所有文件，`-d` 只显示目录不显示文件
  > - `tree ~`：查看家目录的所有文件
  > - `cp 源文件路径 新文件名路径`：复制文件，默认覆盖文件
  > - `cp [-i] [-r]`：`-i` 弹出覆盖同名文件的提示，`-r` 复制目录
  > - `mv`：移动目标目录到目的目录，或重命名——移动文件或文件夹
  > - `mv -i`：弹出覆盖同名文件的提示
  > - `cat [-b] [-n] 文件名`：一次性全部显示文件的内容，`-b` 显示内容同时输出行号不会标注空行，`-n` 显示内容同时输出行号会标注空行
  > - `more`：只显示一页，用空格键或 `f` 翻下一页，`Enter` 翻下一行，`b` 回滚一屏，`q` 退出

### 6.2 文件系统组成与磁盘

**文件系统组成**

- `Inode`：一个文件占用一个 inode，记录文件属性，同时记录此文件所属的 block 编号。
- `inode` 与 `ls -i` 和 `df -i` 等命令相关。
- `Block`：记录文件的具体内容，文件太大会占用多个 block。
- `Superblock`：记录文件系统的整体信息，包括 inode 和 block 的总量、文件系统的格式等。
- `block bitmap`：记录 block 是否被使用的位图。

**文件系统类型**

- `Exts`：要读取文件时，根据 inode 来查找对应的 block。
- `Fat`：没有 inode，每个 block 中存放着下一个 block 的编号。

**磁盘命令**

- `df [-h]`：disk free，显示磁盘剩余空间，重点看根目录 `/`，`-h` 更为人性化。
- `du`（硬盘使用情况概述：`du -hs *`）。
- `du [-h] [目录名]`：disk usage，显示目录下的文件大小，默认显示当前目录。
- `mount`、`fdisk`、`mkfs`、`lsblk`。

### 6.3 搜索相关

- `find [路径] -name '*.py'`：不输入路径默认在当前文件夹查找。
- `locate`：使用 /var/lib/mlocate 数据库搜索，速度快，可以用 `updatedb` 更新数据库（✨ 原笔记写 `update`，应为 `updatedb`）。
- `locate [-ir] keyword`：`-r` 表示正则。
- `grep [-acinv] [--color=auto] 关键字符串 filename`：`-c` 统计个数，`-i` 忽略大小写，`-n` 显示包含搜索内容的行的同时显示行号，`-v` 反向选择（显示不包含搜索内容的行）。
- `grep 'XX' XX.txt`：在 XX.txt 中搜索 XX，显示所有包含该内容的行。
- `grep ^a`：搜索以 a 开头的行。
- `grep a$`：搜索以 a 结尾的行，语法同正则表达式。
- `awk`：文本处理（后文单行脚本中还有示例）。

### 6.4 按文件名查找

- 在当前目录下通过文件名查找一个文件，使用类似于这样的命令：`find . -iname '*something*'`。在所有路径下通过文件名查找文件，使用 `locate something`（但注意到 `updatedb` 可能没有对最近新建的文件建立索引，所以你可能无法定位到这些未被索引的文件）。
- 使用 [`ag`](https://github.com/ggreer/the_silver_searcher) 在源代码或数据文件里检索（`grep -r` 同样可以做到，但相比之下 `ag` 更加先进）。

### 6.5 文本处理与格式转换工具

| 工具 | 用途 |
| --- | --- |
| `lynx -dump -stdin` | 将 HTML 转为文本 |
| [`pandoc`](http://pandoc.org/) | Markdown、HTML 以及所有文档格式之间的转换 |
| `xmlstarlet` | 处理棘手的 XML 时的神器 |
| [`jq`](http://stedolan.github.io/jq/) | 处理 JSON |
| [`shyaml`](https://github.com/0k/shyaml) | 处理 YAML |
| [csvkit](https://github.com/onyxfish/csvkit) | 处理 Excel 或 CSV 文件，提供 `in2csv`、`csvcut`、`csvjoin`、`csvgrep` 等方便易用的工具 |
| [`s3cmd`](https://github.com/s3tools/s3cmd) | 处理 Amazon S3 相关工作时很方便 |
| [`s4cmd`](https://github.com/bloomreach/s4cmd) | 比 s3cmd 效率更高 |
| [`aws`](https://github.com/aws/aws-cli) 以及 [`saws`](https://github.com/donnemartin/saws) | Amazon 官方 AWS 相关工作的基础 |

### 6.6 数据整理命令

- 了解如何使用 `sort` 和 `uniq`，包括 uniq 的 `-u` 参数和 `-d` 参数，具体内容在后文单行脚本节中。另外可以了解一下 `comm`。
- 了解如何使用 `cut`、`paste` 和 `join` 来更改文件。很多人都会使用 `cut`，但遗忘了 `join`。
- 了解如何运用 `wc` 去计算新行数（`-l`）、字符数（`-m`）、单词数（`-w`）以及字节数（`-c`）。
- 了解如何使用 `tee` 将标准输入复制到文件甚至标准输出，例如 `ls -al | tee file.txt`。
- 要进行一些复杂的计算，比如分组、逆序和一些其他的统计分析，可以考虑使用 [`datamash`](https://www.gnu.org/software/datamash/)。

### 6.7 语言环境与排序

- 注意到语言设置（中文或英文等）对许多命令行工具有一些微妙的影响，比如排序的顺序和性能。大多数 Linux 的安装过程会将 `LANG` 或其他有关的变量设置为符合本地的设置。要意识到当你改变语言设置时，排序的结果可能会改变。明白国际化可能会使 sort 或其他命令运行效率下降*许多倍*。某些情况下（例如集合运算）你可以放心的使用 `export LC_ALL=C` 来忽略掉国际化并按照字节来判断顺序。

### 6.8 指定单条命令的环境

- 你可以单独指定某一条命令的环境，只需在调用时把环境变量设定放在命令的前面，例如 `TZ=Pacific/Fiji date` 可以获取斐济的时间。

### 6.9 awk 与 sed

- 了解如何使用 `awk` 和 `sed` 来进行简单的数据处理。参阅 [单行脚本](#8-单行脚本) 获取示例。

### 6.10 批量替换与重命名

- 替换一个或多个文件中出现的字符串：

```sh
      perl -pi.bak -e 's/old-string/new-string/g' my-files-*.txt
```

- 使用 [`repren`](https://github.com/jlevy/repren) 来批量重命名文件，或是在多个文件中搜索替换内容。（有些时候 `rename` 命令也可以批量重命名，但要注意，它在不同 Linux 发行版中的功能并不完全一样。）

```sh
      # 将文件、目录和内容全部重命名 foo -> bar:
      repren --full --preserve-case --from foo --to bar .
      # 还原所有备份文件 whatever.bak -> whatever:
      repren --renames --from '(.*)\.bak' --to '\1' *.bak
      # 用 rename 实现上述功能（若可用）:
      rename 's/\.bak$//' *.bak
```

### 6.11 rsync 同步

- 根据 man 页面的描述，`rsync` 是一个快速且非常灵活的文件复制工具。它闻名于设备之间的文件同步，但其实它在本地情况下也同样有用。在安全设置允许下，用 `rsync` 代替 `scp` 可以实现文件续传，而不用重新从头开始。它同时也是删除大量文件的[最快方法](https://web.archive.org/web/20130929001850/http://linuxnote.net/jianingy/en/linux/a-fast-way-to-remove-huge-number-of-files.html)之一：

```sh
mkdir empty && rsync -r --delete empty/ some-dir && rmdir some-dir
```

### 6.12 复制进度查看

- 若要在复制文件时获取当前进度，可使用 `pv`、[`pycp`](https://github.com/dmerejkowsky/pycp)、[`progress`](https://github.com/Xfennec/progress)、`rsync --progress`。若所执行的复制为 block 块拷贝，可以使用 `dd status=progress`。

### 6.13 排序进阶

- 了解了 `sort` 的选项。处理数字时，使用 `-n` 或 `-h` 处理可读数字（例如 `du -h` 的结果）。明白键是如何工作的（`-t` 和 `-k`）。例如，注意你需要 `-k1，1` 来仅按第一个字段排序，`-k1` 则是按整行排序。稳定排序（`sort -s`）在有些场景下有用。例如，以第二个字段为主关键字、第一个字段为次关键字进行排序，你可以使用 `sort -k1，1 | sort -s -k2，2`。
- 如果你想在 Bash 命令行中写 tab 字面量，按 **ctrl-v** **[Tab]** 或键入 `$'\t'`（后者更好，因为你可以在复制粘贴时也保持正确）。
- 使用 `shuf` 打乱或以随机顺序读取一个文件的行，或者从一个文件中选取多行。

### 6.14 二进制文件处理

- 检查二进制文件用 `diff` 和 `patch`。使用 `diffstat` 查看变更统计数据。注意 `diff -r` 会遍历目录中的整个文件。使用 `diff -r tree1 tree2 | diffstat` 查看变更统计数据。`vimdiff` 用于查看并编辑文件。
- 对于二进制文件，使用 `hd`、`hexdump` 或 `xxd` 进行简单的查看和编辑，使用 `bvi`、`hexedit` 或 `biew` 进行二进制编辑。
- 同样对于二进制文件，`strings`（配合 `grep` 等）能帮你找出其中的文本。
- 对比二进制文件（Delta 压缩），使用 `xdelta3`。

### 6.15 编码转换

- 使用 `iconv` 处理文字编码。需要更复杂的应用，可以使用 `uconv`，可以处理一些更复杂的 Unicode 需求。例如：

```sh
      uconv -f utf-8 -t utf-8 -x '::Any-Lower; ::Any-NFD; [:Nonspacing Mark:] >; ::Any-NFC; ' < input.txt > output.txt
```

### 6.16 文件拆分、日期时间与压缩查看

- 拆分文件可以使用 `split`（按大小拆分）和 `csplit`（按模式拆分）。
- 日期和时间处理，可以使用 [`dateutils`](http://www.fresse.org/dateutils/) 中的 `dateadd`、`datediff`、`strptime` 等工具。
- 使用 `zless`、`zmore`、`zcat` 和 `zgrep` 对压缩过的文件进行一些操作。

### 6.17 文件属性与权限（chattr / ACL）

- 文件属性可以通过 `chattr` 进行设置，比通过 `chmod` 实现更高的文件属性。例如，为了防止一个文件被篡改：`sudo chattr +i /critical/directory/or/file`。
- 使用 `getfacl` 和 `setfacl` 以保存和恢复文件权限。例如：

```sh
   getfacl -R /some/path > permissions.txt
   setfacl --restore=permissions.txt
```

### 6.18 稀疏文件

- 对于[稀疏文件](https://zh.wikipedia.org/wiki/稀疏文件)（✨ 原笔记此处为"空文件"，应为"稀疏文件"），使用 `truncate`（创建稀疏文件）、`fallocate`（用于 ext4、xfs、btrfs 和 ocfs2 文件系统）、`xfs_mkfile`（用于一些平台的文件系统，主要是在 xfsprogs 中）、`mkfile`（用于类似 Unix 的系统，如 Solaris 和 Mac OS）。

---

## 7. 网络调试

> **本节用途**：掌握网络连接查看、SSH 远程传输、HTTP 调试、系统资源监控、JVM 调试与网络抓包等技能，用于排查网络与系统问题。

### 7.1 网络连接与配置基础

> 原笔记要点：网络调试的基础，最基本的是查看网络连接和配置信息。

- CentOS7 网络配置文件在 `/etc/sysconfig/network-scripts/`，其中 `ifcfg-eth0` 的文件是网络配置文件，重启是否生效是取决于是否重启网卡：
  > - `service network restart` 重启网卡，有网卡测试等功能有这一选项
  > - `/etc/init.d/` 这一个目录下面存放的是各个服务的启动脚本，你想重启网络就使用 `/etc/init.d/network restart`
  > - `ip`
  > - `ifconfig` 查看网络设备配置
  > - `ifconfig | grep inet` 查看 IPv4 和 IPv6 地址的配置
  > - `dig`
  > - `ping` 判断对方主机是否在运行
  > - `ping 127.0.0.1` 测试本机网卡是否在运行
  > - 域名是 IP 地址的别名，负责将域名解析到 IP 地址的 web 服务器叫做域名服务器
  > - ssh 默认使用 Linux 和 UNIX 下使用，Windows 则使用 Putty 或 XShell
  > - SSH 端口号 22，web 端口号 80，HTTP 端口号 443，FTP 端口号 21（✨ 原笔记"HTTP端口号443"应为"HTTPS 端口号 443"）
  > - 需要记住 SSH 端口号和 web 端口号，如果连接端口或服务端口改变，就无法连接

### 7.2 SSH 与远程传输

- `.ssh` 文件夹保存了私钥公钥等密钥相关的信息。
- `ssh -p 22 python@192.168.0.144`：`-p` 指定端口 22，用户名@IP地址或主机名。
- 连接之后需要输入密码才能登录。
- `scp -P 22 01.py python@192.168.0.144:Desktop/01.py`：远程传输文件。
- `scp -P 22 python@192.168.0.144:Desktop/01.py 01.py`：将远程 python 用户的 Desktop/01.py 文件下载到当前目录下的 01.py。
- `scp -r python@192.168.0.144:Desktop demo`：将远程的 Desktop 目录下载到当前目录 demo 目录。
- `ssh-agent`、`ssh-add`：已准备好的密钥无需密码重复使用。
- FileZilla：用于 Windows 与 Linux 远程传输文件，一次使用 FTP 端口 21。
- 安全外壳协议配置：同时使用公开密钥和私有密钥进行认证的流程。
- 在 `.ssh` 文件夹下生成密钥 `ssh-keygen`：生成公开密钥；再次输入 `ssh-copy-id -p 22 用户名@IP`：将公开密钥发送给我认识的服务器 XX@IP地址，并添加到 ssh。
- 在 `.ssh` 文件夹下修改 `config` 文件，输入主机别名时省去输入 IP 的方式：
  - `Host myserver`
  - `HostName 172.16.140.1` / `User 使用者名称` / `Port 22`
  - 之后继续连接就直接使用 `ssh myserver`

### 7.3 HTTP 调试

- `curl` 和 `curl -I` 可以被用来被许多便捷地用于 web 调试中，它们的好兄弟 `wget` 或者是更现代的 [`httpie`](https://github.com/jkbrzt/httpie) 也可以用。

### 7.4 系统资源监控

- 了解 CPU 和硬盘的状态，可以使用 `top`（`htop` 更佳）、`iostat` 和 `iotop`。使用 `iostat -mxz 15` 可以了解 CPU 和每块硬盘分区信息的详细信息和使用情况。
- 使用 `netstat` 和 `ss` 查看网络连接的详细情况。
- `dstat` 在你需要了解实时的系统信息时很好用。如果想了解文件系统中有多少流量，使用 [`glances`](https://github.com/nicolargo/glances)，它可以为在一个系统级页面中向你展示一个文件系统很多的数据。
- 想要了解系统内存状态，查看 `free` 和 `vmstat` 的输出。特别是注意 "cached" 的内存，它是 Linux 内核用来进行文件缓存的内存，因此有效地近似于空闲内存。

### 7.5 Java 虚拟机调试

- Java 虚拟机调试是一个不一样的世界，一个可以用来调试 Oracle 的 JVM 或者其它 JVM 上的调试的工具是 `kill -3 <pid>` 也可以获得一个线程转储（线程转储使用 GC 的情况），或者被完整地保存到文件。JDK 中的 `jps`、`jstat`、`jstack`、`jmap` 使用有用。[SJK tools](https://github.com/aragozin/jvm-tools) 是更完整。

### 7.6 网络诊断与带宽监控

- 使用 [`mtr`](http://www.bitwizard.nl/mtr/) 更便于网络诊断，用于路由追踪。
- 使用 [`ncdu`](https://dev.yorhel.nl/ncdu) 来查看磁盘使用情况，它比常用的命令更加友好，比如 `du -sh *`，能列出项目最大的目录。
- 寻找正在监听网络连接的套接字或进程，使用 [`iftop`](http://www.ex-parrot.com/~pdw/iftop/) 或 [`nethogs`](https://github.com/raboof/nethogs)。
- `ab` 很好用（Apache 中自带），可以对 web 服务器进行基准压力测试。遇到问题再做连接尝试，使用 `siege`。
- [`wireshark`](https://wireshark.org/)、[`tshark`](https://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html) 和 [`ngrep`](http://ngrep.sourceforge.net/) 可用于网络调试。

### 7.7 系统调用与调试

- 要理解 `strace` 和 `ltrace`。这可能会帮助你诊断一些问题，磁盘占用高、内存耗尽等问题，而你不知道有些进程的流量是活跃的。注意 profile 数据（`-c`）和附加到一个运行的进程（`-p`）。
- 要查看某动态库，用 `ldd` 查看依赖。如果不是需要在不确定的文件中运行[某动态库](http://www.catonmat.net/blog/ldd-arbitrary-code-execution/)，那更好。
- 要解决阻塞，用 `gdb` 来调试一个正在运行的进程的情况。
- 可以使用 `/proc`。当调试正在运行的程序时，它将发挥作用。比如：`/proc/cpuinfo`、`/proc/meminfo`、`/proc/cmdline`、`/proc/xxx/cwd`、`/proc/xxx/exe`、`/proc/xxx/fd/`、`/proc/xxx/smaps`（这里的 `xxx` 是进程的 id 或 pid）。
- 调试出现一些运行时间的问题，[`sar`](http://sebastien.godard.pagesperso-orange.fr/) 是非常有用的。它可以分析 CPU、内存和网络的数据。
- 涉及到系统调优，用 `sysdig` 可以检测系统级的情况，看看 `stap`（[SystemTap](https://sourceware.org/systemtap/wiki)）、[`perf`](https://en.wikipedia.org/wiki/Perf_(Linux))，以及 [`sysdig`](https://github.com/draios/sysdig)。

### 7.8 系统信息查询

- 查看你最近使用的命令（✨ 原笔记此处表述不准确，应为"查看你的系统信息"），使用 `uname`、`uname -a`（Unix、kernel 信息）或者 `lsb_release -a`（Linux 发行版信息）。
- 无论何时都很适用的（可能是命令行或嵌入式），可以试试 `dmesg`。
- 如果你删除了一份文件，但通过 `du` 查看磁盘占用仍然较高的空间，请先确认文件是否被进程占用：

```
lsof | grep deleted | grep "filename-of-my-big-file"
```


---

## 8. 单行脚本

> **本节用途**：用一行命令完成文本处理、统计、监控等常见任务，是"命令行威力"的集中体现。

> 原笔记总述：一些命令的技巧如下——

### 8.1 sort 与 uniq

- 当你要处理文本或文件行时，`sort` 和 `uniq` 便是你的好朋友。处理数字时，配合参数 `-n` 或者 `-h` 进行排序，多了解下面一行命令的用法。比如，通过 `-T` 参数设置临时文件存放位置（当内存不足时你可能会需要 `-T` 选项，但是当要排序的内容太多时 sort 就不会对文本进行部分排序），以下展示了最常见的用法：

```sh
      sort a b | uniq > c   # c 是 a 并 b
      sort a b | uniq -d > c   # c 是 a 交 b
      sort a b b | uniq -u > c   # c 是 a - b
```

### 8.2 查看目录下所有文件内容

- 使用 `grep . *`（每行都可以追加文件名）或 `head -100 *`（每个文件有一百行）来查看目录下所有文件的内容。这在查找一个有参考价值的配置文件（比如 `/sys`、`/proc`、`/etc`）时特别有用。

### 8.3 awk 统计数值

- ✨ 整理补充：统计文件中某一列（如第三列 `$3`）的数值总和，可以使用 awk：

```sh
      awk '{ x += $3 } END { print x }' myfile
```

（原笔记此条描述为"统计文件系统行中的数量以及……文件五列和表格表头"，转写混乱，以上为按代码语义整理的说明。）

### 8.4 find 列出文件详情

- ✨ 整理补充：如果你想在文件的每一行上查看大小/日期等信息（类似 `ls -l`，比 `ls -lR` 显示更清晰），可以使用：

```sh
      find . -type f -ls
```

（原笔记此条描述转写混乱，以上为按代码语义整理的说明。）

### 8.5 统计访问频率

- ✨ 整理补充：统计 web 日志 `access.log` 中 `acct_id` 字段各值的访问次数，并按次数降序排列（高频访问统计）：

```sh
      egrep -o 'acct_id=[0-9]+' access.log | cut -d= -f2 | sort | uniq -c | sort -rn
```

（原笔记此条描述为"要找出你有一个各种类型到 web 服务器或文件的数据的文件……"转写混乱，以上为按代码语义整理的说明。）

### 8.6 watch 实时监控

- ✨ 整理补充：要实时重复运行一条命令并观察输出变化，可以使用 `watch`。例如观察目录文件变化：`watch -d -n 2 'ls -rtlh | tail'`；或者在监控 WiFi 连接信号变化时进行观察，可以使用 `watch -d -n 2 ifconfig`。（原笔记此条描述转写混乱，已按原意整理。）

### 8.7 随机抽取一条命令（taocl）

- ✨ 整理补充：下面这个函数 `taocl` 会从本笔记的 Markdown 源文件中随机抽取一条命令提示（适合"抽奖式"复习）：

```sh
      function taocl() {
        curl -s https://raw.githubusercontent.com/jlevy/the-art-of-command-line/master/README-zh.md|
          pandoc -f markdown -t html |
          iconv -f 'utf-8' -t 'unicode' |
          xmlstarlet fo --html --dropdtd |
          xmlstarlet sel -t -v "(html/body/ul/li[count(p)>0])[$RANDOM mod last()+1]" |
          xmlstarlet unesc | fmt -80
      }
```

（原笔记此条描述为"运行这个数据从这些数据文件中获取一系列核心（例计 Markdown 文件的通用方法）"，转写混乱，以上为按代码语义整理的说明。）

---

## 9. 冷门但有用

> **本节用途**：收录一些不那么常用、但关键时刻能派上用场的小命令，全部保留原笔记的命令与链接，转为表格便于速查。

| 命令 | 用途 |
| --- | --- |
| `expr` | 执行算术运算或字符串比较 |
| `m4` | 简单的宏处理器 |
| `yes` | 重复打印字符串 |
| `cal` | 漂亮的日历 |
| `env` | 执行一个命令（打印脚本文件中有用的变量） |
| `printenv` | 打印环境变量（调试时或在脚本文件中很有用） |
| `look` | 查找以特定字符串开头的单词或行 |
| `cut`、`paste` 和 `join` | 数据修改 |
| `fmt` | 格式化文本段落 |
| `pr` | 将文本文件格式化成打印/分页格式 |
| `fold` | 折行文本中的行 |
| `column` | 将文本格式化成多列或表格的宽度 |
| `expand` 和 `unexpand` | 制表符与空格互换 |
| `nl` | 计算行号 |
| `seq` | 打印数字 |
| `bc` | 计算器 |
| `factor` | 分解因数 |
| [`gpg`](https://gnupg.org/) | 加密并签名文件 |
| `toe` | terminfo 表头 |
| `nc` | 网络调试及数据流 |
| `socat` | 套接字代理，与 `netcat` 类似 |
| [`slurm`](https://github.com/mattthias/slurm) | 网络流量可视化 |
| `dd` | 文件或文件系统镜像 |
| `file` | 识别文件类型 |
| `tree` | 以树的模式打印文件和目录，类似于递归的 `ls` |
| `stat` | 文件信息 |
| `time` | 执行命令，然后计算时间 |
| `timeout` | 在指定时间限时执行命令（例如 `timeout 5s whoami`） |
| `lockfile` | 文件锁（防止 `rm -f` 的情况） |
| `logrotate` | 轮换、压缩以及邮件日志文件 |
| `watch` | 重复运行一个命令，或关注输出的变化 |
| [`when-changed`](https://github.com/joh/when-changed) | 当检测到文件时运行命令。注意 `inotifywait` 和 `entr` |
| `tac` | 反向打印文件 |
| `shuf` | 文件中随机选取行 |
| `comm` | 一行一行地比较排序后的文件 |
| `strings` | 从二进制文件中提取文本 |
| `tr` | 转换字母 |
| `iconv` 或 `uconv` | 文本编码转换 |
| `split` 和 `csplit` | 分割文件 |
| `sponge` | 在写入前获取所有输入，在获取文件后再对同一文件进行操作，比如 `grep -v something some-file \| sponge some-file` |
| `units` | 将一种测量单位转换为另一种测量单位（利用 `/usr/share/units/definitions.units`） |
| `apg` | 生成密码 |
| `xz` | 压缩/解压的文件（✨ 原笔记"压缩/解压的文件"应为"压缩/解压文件"） |
| `ldd` | 动态库信息 |
| `nm` | 获取 obj 文件中的符号 |
| `ab` 或 [`wrk`](https://github.com/wg/wrk) | web 服务器基准测试 |
| `strace` | 系统调用调试 |
| [`mtr`](http://www.bitwizard.nl/mtr/) | 更好的网络诊断工具 |
| `csh` | 简单的通用 shell |
| `rsync` | 同步 ssh 或本地文件系统镜像文件与文件 |
| [`wireshark`](https://wireshark.org/) 和 [`tshark`](https://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html) | 抓包和网络调试 |
| [`ngrep`](http://ngrep.sourceforge.net/) | 网络的 grep |
| `host` 和 `dig` | DNS 查询 |
| `lsof` | 查看文件被进程打开的文件或查找端口信息 |
| `dstat` | 系统信息查看 |
| [`glances`](https://github.com/nicolargo/glances) | 高层的多子系统监控 |
| `iostat` | 硬盘使用情况 |
| `mpstat` | CPU 使用情况 |
| `vmstat` | 内存使用情况 |
| `htop` | top 的增强版 |
| `last` | 查看登录 |
| `w` | 查看连接用户的进程 |
| `id` | 用户/组 ID 信息 |
| [`sar`](http://sebastien.godard.pagesperso-orange.fr/) | 系统历史数据 |
| [`iftop`](http://www.ex-parrot.com/~pdw/iftop/) 或 [`nethogs`](https://github.com/raboof/nethogs) | 网络带宽或进程的网络使用情况 |
| `ss` | socket 数据 |
| `dmesg` | 错误与系统信息 |
| `sysctl` | 在系统运行时查看和调整系统内核的参数 |
| `hdparm` | SATA/ATA 磁盘修改及参数查询 |
| `lsblk` | 查看磁盘设备信息：可以查看你所使用的设备以及分区信息 |
| `lshw`、`lscpu`、`lspci`、`lsusb` 和 `dmidecode` | 查看硬件信息，包括 CPU、BIOS、RAID、内存、USB 设备 |
| `lsmod` 和 `modinfo` | 查看内核模块，以及模块的详细信息 |
| `fortune`、`ddate` 和 `sl` | 有趣，这个需要你自己判断是否有足够的磁盘和资源名是否"有用"（✨ 原笔记此句转写混乱，已按原意整理为"取决于你是否认为它们有用"） |


---

## 10. 仅限 OS X 系统

> **本节用途**：OS X（macOS）用户在命令行中的专属注意事项，包括包管理、剪贴板、快捷键、Spotlight 以及与 Linux 命令的差异。

以下是一些*仅限* OS X 系统的重要注意事项。

### 10.1 包管理与剪贴板

- 用 `brew`（Homebrew）或 `port`（MacPorts）进行包管理。这样可以在 OS X 系统中安装未包含在其中的大部分命令。
- 用 `pbcopy` 将备份好的文件粘贴到剪贴板，用 `pbpaste` 粘贴出来。

### 10.2 键盘与文件打开

- 想要在 OS X 系统中把 Option 键作为 alt 键（比如在终端中使用的 **alt-b**、**alt-f** 等命令中使用），在设置 → 键盘 → 修饰键 → 将 Option 设置为 Meta 键。
- 用 `open` 或 `open -a /Applications/Whatever.app` 使用鼠标打开文件。

### 10.3 Spotlight 搜索

- Spotlight：用 `mdfind` 查找文件，用 `mdls` 显示元数据（比如文件的 EXIF 信息）。

### 10.4 与 Linux 命令的差异

- 注意 OS X 系统是基于 BSD UNIX 的，很多命令（比如 `ps`、`ls`、`tail`、`awk`、`sed`）都与 Linux 中有很多的不同（Linux 很多命令往往向上兼容了 System V-style Unix 和 GNU 扩展）。你可以使用 "BSD General Commands Manual" 的 man 页面来运行这些不同的选项（比如 `gawk` 和 `gsed` 与 GNU 中的 awk 和 sed 对应）。如果你要编写兼容的 Bash 脚本，最好使用跨平台的命令（比如，避免使用 Python 或者 `perl`）或者是跨平台的工具。（✨ 原笔记此段转写较乱，已按原意整理。）

### 10.5 版本信息

- 使用 `sw_vers` 获取 OS X 的版本信息。

---

## 11. 仅限 Windows 系统

> **本节用途**：在 Windows 上使用类 Unix 工具链的注意事项，包括 Cygwin/WSL/MinGW、Windows 自带命令行、Cygwin 细节以及 PowerShell 的对应命令。

以下是一些*仅限* Windows 系统的注意事项。

### 11.1 在 Windows 下获取 Unix 工具

- 可以安装 [Cygwin](https://cygwin.com/) 使你可以在 Microsoft Windows 中使用 Unix shell 的功能。基本上所有的命令都可以使用。
- 在 Windows 10 下，你可以使用 [Bash on Ubuntu on Windows](https://msdn.microsoft.com/commandline/wsl/about)，这个提供了一些完整的 Bash 命令行，甚至可以不用靠 Unix 命令行来运行。最大的优势是 Linux 中的命令是在 Windows 中运行，而且运行一条命令，Windows 中运行的命令同样可以在 Bash 命令行中来运行。
- 如果你想在 Windows 中使用 GNU 命令或者工具（比如 GCC——✨ 原笔记"GCP"应为"GCC"），可以使用 [MinGW](http://www.mingw.org/) 并与其一起的 [MSYS](http://www.mingw.org/wiki/msys)，这个安装包含了类似 bash、gawk、make 和 grep 的工具。MSYS 中不需要包含所有可以与 Cygwin 类似使用的功能。使用 Unix 工具下的 Windows 端口时 MinGW 便已经包含使用。（✨ 原笔记此段转写较乱，已按原意整理。）
- 顺便说一下在 Windows 中启动一个 Unix 命令行工具是 [Cash](https://github.com/dthree/cash)。注意在工具中包含了很多的 Unix 命令和命令行使用。

### 11.2 使用 Windows 命令行

- 可以使用 `wmic` 在命令行中获取 Windows 系统的信息并执行命令。
- Windows 默认的命令行工具包括 `ping`、`ipconfig`、`tracert` 和 `netstat`。
- 可以使用 `Rundll32` 命令来实现[快捷命令的 Windows 使用](http://www.thewindowsclub.com/rundll32-shortcut-commands-windows)。

### 11.3 Cygwin 注意事项

- 注意 Cygwin 的安装目录可以启动运行脚本的 Unix 命令。
- 使用 `mintty` 使用你的命令行终端。
- 要启动 Windows 服务，可以来使用 `/dev/clipboard`（✨ 原笔记此处疑为笔误，一般用 `/dev/clipboard` 访问剪贴板）。
- 使用 `cygstart` 可以用来启动一个文件。
- 要启动 Windows 的路径，可以使用 `regtool`。
- 注意 Windows 的文件夹结构 `C:\` 在 Cygwin 中使用 `/cygdrive/c` 来访问，而且 Cygwin 的 `/` 就是 Windows 中的 `C:\cygwin`。要比较 Cygwin 和 Windows 的路径可以使用 `cygpath`。这个在需要将 Windows 命令写入脚本时很是有用。
- 可以使用 `wmic`，你就可以从命令行执行大量 Windows 系统配置命令，并生成脚本。
- 要在 Windows 中获取 Unix 的命令和函数，再一个就是使用 [Cash](https://github.com/dthree/cash)。需要注意的，这个命令行中包括的 Unix 命令和命令行数据并不多。（✨ 原笔记此段转写较乱，已按原意整理。）
- 要在 Windows 中查看 GNU 的安装信息（比如 GCC）的再一个方案是使用 [MinGW](http://www.mingw.org/) 并与一起的 [MSYS](http://www.mingw.org/wiki/msys) 等工具，已经包含了 bash、gawk、make、grep 等命令。注意 MSYS 补充的功能不是 Cygwin 的部分。MinGW 在安装时包含了 Unix 工具的 Windows 端口。

### 11.4 在 Windows 下使用 PowerShell

> ✨ 整理补充：原笔记标题"在Windows下使用powershell，可以`.ps1`来做对应对应"转写混乱，本节按原意整理为"使用 PowerShell（`.ps1` 脚本）做对应的命令操作"。

**学习资源**

- [PowerShell cookbook](https://github.com/DodgeV/the-art-of-command-line/blob/master/books/Windows%20PowerShell%20Cookbook.pdf)
- [Microsoft powershell](https://www.bilibili.com/video/av15458578) & [Microsoft 学编程视频教程](https://docs.microsoft.com/zh-cn/powershell/scripting/learn/ps101/02-help-system?view=powershell-6)

**Unix 命令 ↔ PowerShell 命令对应表**

| Unix / CMD | PowerShell |
| --- | --- |
| `echo 'hello world'` | `write-host 'hello world'` |
| `cd\` | `cd\` |
| `cd` | `set-location` |
| `ls` | `get-childitem` |
| `mkdir` | `md` |
| `get-alias` | `gal -Definition Get-Process` |
| `ipconfig` | `ipconfig /all` |
| `mstsc`、`ping` | `mstsc`、`ping` |
| `copy` | `xcopy` |
| `notepad;calc;mspaint` | `notepad;calc;mspaint` |
| `man` / `update-help` | `help` |
| 帮助 | `Get-Help g*ser*` |
| 帮助（详情） | `Get-Help Get-Service -Detailed` |
| 帮助（在线） | `Get-Help Get-Service -Online` |
| 帮助（窗口） | `Get-Help Get-Service -ShowWindow` |
| 查找进程 | `Get-Process -Name f*` |
| 查找服务 | `Get-Service -Name bits,bfe` |
| 动词 | `Get-Verb [Imeasure]` |
| 查找命令 | `Get-Command -Verb get` |
| `clear` | `cls`=`clear-host`=`clear` |
| 关机 | `shutdown -s -f -t 3` |

---

## 12. 免责声明与授权条款

### 免责声明

尽管你小心翼翼，但你的代码出问题还是难以避免的。如果你的代码出现问题，你将"有能力"在 Bash 中使用一条命令来解决问题。（✨ 原笔记此句转写不清，疑为"你通常能在 Bash 中用一条命令解决"的表述。）

### 授权条款

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

本文采用知识共享 [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/)。授权。
