# 📐 数学建模学习笔记（整理版）

> 本笔记由原 `README.md`（Math modeling）整理而来：**保留全部原始内容与链接**，按「方法论 → 知识储备 → 分工规划 → 论文写作 → 比赛资源 → 学习资源」重排逻辑，修正明显笔误，并为部分知识点补充简短说明（新增内容以「✨ 整理补充」标注）。
>
> 使用建议：备赛前期啃【方法论 + 知识储备】打基础，赛前重点过【分工规划 + 论文写作】练节奏，资源类按需查阅。

---

## 目录

1. [建模方法论](#一建模方法论)
2. [参赛知识储备](#二参赛知识储备)
3. [团队分工与时间规划](#三团队分工与时间规划)
4. [论文写作规范](#四论文写作规范)
5. [论文模板与提交](#五论文模板与提交)
6. [比赛信息与历年真题](#六比赛信息与历年真题)
7. [学习资源](#七学习资源)

---

## 一、建模方法论

> 数学建模与纯数学不同：它的方法是**归纳演绎**——数学只要推理正确结果就正确，而数学模型的演绎结果**必须接受实际检验**。核心流程 = 把实际问题抽象成数学模型 → 求解 → 用实际数据验证。

### 1.1 建模的总体思路

- **工具**：MATLAB（主力工具）
- **思维**：建立**最简变量关系（函数关系）**，用类比 / 创新寻找合适的数学结构

### 1.2 建立函数关系的四类方法

> 核心区别：**拟合 / 回归 / 逼近**不要求曲线过已知点，**插值**要求必须过已知点。

| 方法 | 特点 | 适用场景 |
|---|---|---|
| **观察法** | 结合初等数学，直接观察变量关系 | 数据具有比例关系时 |
| **拟合** | 调整曲线参数，使曲线与数据相符（数据处理方式，不特指某方法） | 有大量数据、趋势明显时 |
| **回归** | 重在研究两个或多个变量之间的**关系** | 需要分析变量相关性时 |
| **逼近** | 用简单函数逼近未知函数，不要求过已知点 | 函数复杂、只需近似时 |

### 1.3 拟合的近似准则（拟合原理）

> 三条准则的本质区别：**给哪些数据点更大的权重**。

1. **切比雪夫近似准则**：偏差的最大绝对值最小（给定模型 `y=f(x)` 和 m 个数据点 `(xi, yi)`，极小化整个集合的最大绝对偏差 `|yi−f(xi)|`）→ 对潜在有较大偏差的单个数据点给更大权重。
2. **极小化绝对偏差之和准则**：绝对偏差之和最小 → 给每个数据点**相同**权重。
3. **最小二乘准则**：绝对偏差平方和最小 → 按与中间某处的**远近**加权，与单个点的显著偏离有关。

### 1.4 插值（要求过已知点）

> 插值分**一维插值** / **二维插值**。插值函数（未知函数的近似函数）应满足：① 足够简单；② 计算方便；③ 足够好的性态（有足够高阶导数：**可导 优于 连续 优于 分段**）。

#### 从多项式中找插值函数（多项式插值法）

- **拉格朗日（Lagrange）插值法**
  - 思路：把复杂问题简化为求特解——构造只经过点 `(x0, 1)`、其余点 y 值都为 0 的基函数（左右已为 n 次，故系数为常数，代入 `(x0,1)` 解出），同理得到 n 个基函数。
  - 结论：拉格朗日插值多项式 = 对应节点的基函数 × 相应节点函数值 之和。
  - 两点确定一条直线 = 一次插值。
  - **缺点**：遗漏一个节点需全部重算，**不具继承性**。
- **牛顿（Newton）插值法**：为简便计算取等步长 h，引入差分（另有后差分、中心差分）。
- **Hermite 插值法**
- **分段线性插值法**
- **三次样条插值法**

#### 其他插值途径

- 从三角函数中找插值函数 → **三角插值法**
- **分段插值法**
- **有理插值法**

### 1.5 工具

- [📒 我的 MATLAB 笔记](https://github.com/DodgeV/learning-programming/blob/master/MATLAB_NOTE.md)

---

## 二、参赛知识储备

### 2.1 需要了解的基础学科

1. 数学分析（高等数学）
2. 高等代数（线性代数）
3. 概率与数理统计
4. 最优化理论（规划理论）
5. 图论
6. 组合数学
7. 微分方程稳定性分析
8. 排队论

> ✨ 整理补充：以上是数模赛的「八块地基」——其中**概率统计 + 最优化 + 图论**是出现频率最高的三大板块，建议优先吃透。

### 2.2 建模基础知识与常用软件工具

> 备赛第一阶段：补数学基础 + 熟悉软件。

1. **掌握建模必备的数学基础知识**（如初等数学、高等数学等），以及数学建模中常用但尚未学过的方法，如图论方法、优化中的若干方法、概率统计以及运筹学等方法。
2. **重点学习实用数学软件**（Mathematica、MATLAB、Lindo、Lingo、SPSS）的使用及一般性开发，尤其注意**同一数学模型可以用多个软件求解**。

**示例：贷款买房问题**——某人贷款 8 万元买房，每月还款 880.87 元，月利率 1%：
（1）已还贷整 6 年，想知道还欠银行多少钱；
（2）此人忘记贷款期限是多少年，请告诉他。
该问题可用 Mathematica、MATLAB、Lindo、Lingo 等多个软件包编程求解。

### 2.3 建模的过程与方法

- 数学建模是极具创造性和挑战性的活动，不可能用条条框框规定各模型如何具体建立。
- 一般涉及两个方面：**第一，将实际问题转化为理论模型；第二，对理论模型进行计算和分析**。简言之，就是建立数学模型来解决各种实际问题的过程。
- 可参考：姜启源《数学模型》，高等教育出版社。

### 2.4 常用算法（按竞赛题型选）

> 建模与计算是数模两大核心：模型建立后，**算法好坏直接影响运算速度与答案优劣**。常用软件：Mathematica、MATLAB、Maple、Lindo、Lingo、SPSS。

1. **蒙特卡罗算法**（随机性模拟算法，通过计算机仿真解决问题，也可用于检验模型正确性，**比赛必用**，常用 Mathematica / MATLAB 实现）
2. **数据拟合、参数估计、插值**等数据处理算法（处理大量数据的关键，用 MATLAB）
3. **线性规划、整数规划、多元规划、二次规划**等规划类（多数赛题属最优化问题，用 Lindo / Lingo）
4. **图论算法**（最短路、网络流、二分图等，用 Mathematica / Maple）
5. **动态规划、回溯搜索、分治、分支定界**等计算机算法（常用 Lingo）
6. **图像处理算法**（赛题多与图形相关，论文也需配图，用 MATLAB）
7. **最优化三大非经典算法**：模拟退火法、神经网络、遗传算法（解决较困难的最优化问题，实现较难需慎重，用 Lingo / MATLAB / SPSS）

#### 算法实现资源（GitHub）

> 想直接看代码实现的点这里：

- [数学建模相关算法 MATLAB 实现（HuangCongQing/Algorithms_MathModels）](https://github.com/HuangCongQing/Algorithms_MathModels)
- [经典算法（zhanwen/MathModel）](https://github.com/zhanwen/MathModel/tree/master/%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AE%97%E6%B3%95)
- [现代算法合集](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95)
  - [计算机仿真](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E8%AE%A1%E7%AE%97%E6%9C%BA%E4%BB%BF%E7%9C%9F)
  - [粒子群算法](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E7%B2%92%E5%AD%90%E7%BE%A4%E7%AE%97%E6%B3%95)
  - [马尔可夫链](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E9%A9%AC%E5%B0%94%E5%8F%AF%E5%A4%AB%E9%93%BE)
  - [蒙特卡洛法](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%B3%95)
  - [模拟退火法](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E6%A8%A1%E6%8B%9F%E9%80%80%E7%81%AB%E6%B3%95)
  - [神经网络](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C)
  - [小波分析](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E5%B0%8F%E6%B3%A2%E5%88%86%E6%9E%90)
  - [遗传算法](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E9%81%97%E4%BC%A0%E7%AE%97%E6%B3%95)

### 2.5 关于数模竞赛的几本好书

- ▲ 姜启源，《数学模型（第二版）》，高等教育出版社
- ▲ 姜启源、谢金星、叶俊，《数学建模（第三版）》，高等教育出版社
- ▲ 萧树铁等，《数学实验》，高等教育出版社
- ▲ 朱道元，《数学建模案例精选》，科学出版社
- ▲ 雷功炎，《数学模型讲义》，北京大学出版社
- ▲ 叶其孝等，《大学生数学建模竞赛辅导教材（一）~（四）》，湖南教育出版社
- ▲ 江裕钊、辛培清，《数学模型与计算机模拟》，电子科技大学出版社
- ▲ 杨启帆、边馥萍，《数学模型》，浙江大学出版社
- ▲ 赵静等，《数学建模与数学实验》，高等教育出版社、施普林格出版社
- ▲ 韩中庚，《数学建模方法与应用》，高等教育出版社
- ▲ 杨启帆，《数学建模案例集》，高等教育出版社

---

## 三、团队分工与时间规划

### 3.1 三人分工建议

- **建模手**：对建模、各类算法理论熟悉，了解问题背景后能建立模型、设计求解算法（各专业均可，能力可通过培训锻炼）。
- **编程手**：将算法编制成程序、求得数值解（对计算机要求高，适合信息/软件学院学生；很多队伍败在**建模与求解脱节**，两者必须紧密配合）。
- **写作手**：承担主要写作任务（最好来自不同专业，弥补赛题涉及的各领域专业知识）。

> ✨ 整理补充：一句话总结——**建模手定方向、编程手出结果、写作手讲故事**，三人要全程互相 sync，切忌各干各的。

### 3.2 三天时间规划（重要！）

> 原则：**第一天绝不熬夜**，为后面积蓄体力与精神；第三天只做小改，切勿大改（大改必致时间不够）。

| 时间 | 建模手 | 编程手 | 写作手 |
|---|---|---|---|
| **D1 08:00-12:00** | 队伍共同：收集/检索两道赛题资料，讨论选赛题，定进程计划 | 同左 | 针对题目检索资料，初步形成问题重述与分析框架 |
| **D1 12:00-16:00** | 设计任务一模型（多与编程手商讨，确保可编程实现） | 完成任务一编程；把模型讲给写作手，共同定方案 | 继续检索资料，完成问题重述与分析 |
| **D1 16:00-22:00** | 设计任务二模型 | 完成任务二编程，讲给写作手，共同定方案 | 初步搭好任务一、二写作框架（当晚不熬夜） |
| **D2 07:00-13:00** | 设计任务三模型 | 完成任务三编程，讲给写作手，共同定方案 | 继续任务一、二写作 |
| **D2 13:00-18:00** | 设计任务四模型 | 完成任务四编程，讲给写作手，共同定方案 | 初步完成任务三写作 |
| **D2 18:00-23:00** | 设计任务五模型 | 完成任务五编程，讲给写作手，共同定方案 | 初步完成任务四写作 |
| **D3 08:00-12:00** | 与编程手考虑模型改进（增加变量/修改函数，**切勿大改**） | 同左 | 完成任务五写作，产出最初完整稿 |
| **D3 12:00-20:00** | 用 MATLAB / Visio 画框图表现模型结果（一图胜千言） | 同左 | 商讨后完成修正模型写作；共同完成模型假设、符号说明、优缺点分析、参考文献 |
| **D3 21:00-07:00** | 支持排版与校对 | 同左 | **最终完成摘要**并排版设计全文（摘要决定能否获奖，须多次修改定稿） |

### 3.3 建模前的思考（动笔前先回答）

- 答卷需要回答哪几个问题 → 建模需要解决哪些问题
- 问题以怎样的方式回答 → 结果以怎样的形式表示
- 每个问题要列出哪些关键数据 → 建模需要计算哪些关键数据
- 每个量列一组还是多组数据 → 计算一组还是多组

### 3.4 答卷五原则

| 原则 | 追求 |
|---|---|
| 准确 | 科学性 |
| 条理 | 逻辑性 |
| 简洁 | 数学美 |
| 创新 | 研究应用目标之一 |
| 实用 | 建模 |

**三大意识**：
- **应用意识**：解决实际问题，结果、结论要符合实际；模型、方法、结果要易于理解、便于应用；站在应用者立场处理问题。
- **数学建模意识**：用数学方法解决问题，要有数学模型；问题模型的数学抽象方法要有普适性、科学性，不局限于本具体问题。
- **创新意识**：建模有特点，更合理、科学、有效、符合实际，更有普遍应用意义；不单纯为创新而创新。

---

## 四、论文写作规范

> 论文是竞赛成绩的唯一书面依据，直接决定获奖级别。按以下模板逐节写作即可。

### 写作能力怎么练

- 答卷（论文）是竞赛成绩结晶的书面形式，是评定成绩好坏、高低、获奖级别的**唯一依据**，写好论文在竞赛中极其重要，是参赛学生的必修课。
- 练法：
  1. 认真学习并掌握**全国大学生数学建模竞赛组委会最新制定的论文格式要求**，多阅读科技文献；
  2. 通过剖析历届优秀论文（如中国人民解放军信息工程学院李开锋、赵玉磊、黄玉慧 2004 年获全国一等奖论文《奥运场馆周边的 MS 网络设计方案》）总结建模论文的一般结构与写作要点，学习体会和摸索。

### 4.1 论文结构（逐节要点）

**一、摘要**（最核心，评委初审主要看摘要 + 全文结构）
- 内容：
  1. 用 1-2 句话说明原问题要解决的问题；
  2. 建立了什么模型（数学上属什么类型）、建模思想（思路）、模型特点；
  3. 算法思想（求解思路）与特色；
  4. 主要结果（数值结果、结论），回答题目全部"问题"；
  5. 模型优点、结果检验、模型检验、灵敏度分析、有无改进与推广。
- 要求：特色与创新之处必须在此强调；长度要合适；准确、简明、条理、清晰、突出特色与创新点。

**二、问题的提出**
- 用自己的语言阐述背景、条件、要求，重点列出"问题"（即要求）。
- 要求：不是题目的完整拷贝；根据自己的理解，清楚简明地阐述背景、条件和要求。

**三、条件假设**
- 内容：根据题目中的条件做假设；根据题目中的要求做假设。
- 要求：**合理性最重要**；假设合理且全面，但不要罗列大量无关假设，关键性假设不能缺；合理假设的作用 = **简化问题、明确问题、限定模型适用范围**。

**四、符号约定**（统一符号，避免歧义）

**五、问题分析**
1. 名词解释
2. 问题的背景分析
3. 问题分析

**六、模型建立**
- 抽象要求：
  - 模型主要类别：初等模型、微分方程模型、差分方程模型、概率模型、统计预测模型、优化模型、决策模型、图论模型等；
  - 常见建模目的（对应方法）：描述/解释现实世界各类现象 → 用机理型分析方法探索内在规律；预测事件是否发生或事物发展趋势 → 用数理统计或模拟方法；优化管理、决策或控制事物 → 需合理定义可量化的评价指标及评价方法；
  - 建模过程要点：模型的整体设计、合理假设、建立数学结构、建立数学表达式；
  - 模型要求：明确、合理、简洁、具有一般性（**切忌**用"凑"的方法只针对赛题特殊情况给出结果，缺乏一般性不是正确思路）；
  - 鼓励创新，欣赏独树一帜、标新立异，但要合理；
  - 避免罗列一堆模型却不做评价。
- 具体要求：
  - 基本模型：首先要有数学模型（数学公式、方案等），要求完整、正确、简明；
  - 简化模型：明确说明简化思想与依据，简化后的模型尽可能给出。

**七、模型求解**
- 每块内容包括：计算方法设计/选择、算法设计/选择、算法思想依据、步骤及实现、计算框图、所采用的软件名称。
- 写作要求：
  1. 需建立数学命题时，叙述符合数学命题表述规范，论证尽可能严密；
  2. 说明计算方法/算法的原理、思想、依据、步骤；采用现有软件时说明理由与软件名称；
  3. 计算过程中间结果可要可不要的，不要列出；
  4. 设法算出合理的数值结果；
  5. **最终数值结果的正确性或合理性是第一位的**；
  6. 对数值/模拟结果进行必要检验；结果不正确、不合理或误差大时，分析原因，修正/改进算法、计算方法或模型；
  7. 题目要求回答的问题、数值结果、结论须一一列出；
  8. 列数据问题：考虑是否需要列出多组数据或额外数据进行比较分析，为各种方案提供依据；
  9. 结果表示：要集中、一目了然、直观、便于比较（数值结果精心设计表格，可能的话用图形图表；求解方案用图示更好）；
  10. 必要时对问题解答作定性或规律性讨论，最后结论要明确。
- 附加要点：
  - 算法设计/选择：给出思想依据、步骤；
  - 引用或建立必要的数学命题和定理；
  - 不能给出精确解时，需给出**不止一种解法**并进行测试比较与评价——为说明算法好，要有参照：从最简单、最容易得到的算法开始，逐步改进，直到得到满意解；
  - 具体表现：对离散问题，最简单的解可能是随机选择，然后用你的算法得到的解与之比较。

**八、结果分析、结果检验、模型检验及修正、结果表示**
- 要求：
  1. 最终数值结果的正确性或合理性应当是第一位的；
  2. 对数值结果或模拟结果进行必要检验；结果不正确、不合理或误差大时分析原因，对算法、计算方法或模型进行修正、改进；
  3. 题目要求回答的问题、数值结果、结论需一一列出；
  4. 列数据问题：考虑是否列出多组数据或额外数据，进行分析比较为各种方案提供依据；
  5. 结果表示：集中、一目了然、直观、便于比较（数值结果精心设计表格，可能的话用图形图表；求解方案用图示最好）；
  6. 必要时对问题解答作定性或规律性讨论；
  7. 最后结论要明确。

**九、模型稳定性及灵敏度分析**
（检验模型对参数变化是否敏感，是加分项）

**十、模型评价**
1. 模型优点（突出）
2. 模型缺点（不回避）

**十一、模型改进**
> 提示：不要玩弄新数学术语。

**十二、参考文献**

**十三、附录**

### 4.2 写作建议

1. **小标题很重要**：只读各小标题就能知道整篇论文概要；多设标题，避免大段文字无标题（正文至少两级标题，如 1、1.1），每小节不要超过两段；
2. **善于用图表**；
3. **突出三要素：模型、算法、结果**。

### 4.3 论文评阅准则

1. 假设的合理性
2. 建模的创造性
3. 结果的合理性
4. 表述的清晰性

### 4.4 建模后续工作

- **论文检查**：模型的正确性、合理性、创新性；结果的正确性、合理性；文字表述清晰、分析精辟、摘要精彩。
- **分工的目的**：分工是为了抢时间。

---

## 五、论文模板与提交

### 5.1 模板下载

- [LaTex 论文模版（2019 年）](https://github.com/zhanwen/MathModel/blob/master/2019%E5%B9%B4%E8%AE%BA%E6%96%87%E6%A8%A1%E7%89%88/2019%E5%B9%B4Latex%E6%A8%A1%E7%89%88.zip)
- [Word 论文模版（已更新最新，2019 "华为杯"第十六届中国研究生数模竞赛规范）](https://github.com/zhanwen/MathModel/blob/master/2019%E5%B9%B4%E8%AE%BA%E6%96%87%E6%A8%A1%E7%89%88/%E2%80%9C%E5%8D%8E%E4%B8%BA%E6%9D%AF%E2%80%9D%E7%AC%AC%E5%8D%81%E5%85%AD%E5%B1%8A%E4%B8%AD%E5%9B%BD%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AE%BA%E6%96%87%E6%A0%BC%E5%BC%8F%E8%A7%84%E8%8C%83.doc)
- [如何编译 Latex 文件（LaTex 模版使用方式）](https://github.com/zhanwen/MathModel/tree/master/2019%E5%B9%B4%E8%AE%BA%E6%96%87%E6%A8%A1%E7%89%88/latex_note.md)

### 5.2 论文提交（MD5 文件校验）

- [MD5 文件校验和使用说明](https://github.com/zhanwen/MathModel/blob/master/MD5%E6%96%87%E4%BB%B6%E6%A0%A1%E9%AA%8C%E5%92%8C%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E/%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md)

---

## 六、比赛信息与历年真题

### 6.1 比赛官网

> [更新/添加比赛官网地址（点击进入汇总页）](https://cpipc.chinadegrees.cn/)

- [“华为杯”中国研究生数学建模竞赛](https://cpipc.chinadegrees.cn/cw/hp/4)
- [数学建模竞赛](https://cpipc.chinadegrees.cn/cw/hp/4)
- [电子设计竞赛](https://cpipc.chinadegrees.cn/cw/hp/6)
- [人工智能创新大赛](https://cpipc.chinadegrees.cn/cw/hp/2c9088a5696cbf370169a3f8101510bd)
- [机器人创新设计大赛](https://cpipc.chinadegrees.cn/cw/hp/2c9088a5696cbf370169a3f8934810be)

### 6.2 国赛试题（研究生数学建模竞赛历年试题）

- [2019](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2019%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2018](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2018%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2017](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2017%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2016](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2016%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2015](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2015%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2014](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2014%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2013](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2013%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2012](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2012%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2011](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2011%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2010](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2010%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2009](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2009%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2008](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2008%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2007](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2007%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2006](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2006%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2005](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2005%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2004](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2004%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)

### 6.3 国赛优秀论文（历年，按题号分）

**2018 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：关于跳台跳水体型系数设置的建模分析](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：光传送网建模与价值评估](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：对恐怖袭击事件记录数据的量化分析](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：基于卫星高度计海面高度异常资料获取潮汐调和常数方法及应用](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)
- [E 题：多无人机对组网雷达的协同干扰](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/E)
- [F 题：航站楼扩增评估](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/F)

**2017 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：无人机在抢险救灾中的优化运用](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：面向下一代光通信的 VCSEL 激光器仿真模型](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：航班恢复问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：基于监控视频的前景目标提取](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)
- [E 题：多波次导弹发射中的规划问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/E)
- [F 题：地下物流系统网络](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/F)

**2016 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：多无人机协同任务规划](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：具有遗传性疾病和性状的遗传位点分析](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：基于无线通信基站的室内三维定位问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：军事行动避空侦察的时机和路线选择](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)
- [E 题：粮食最低收购价政策问题研究](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/E)

**2015 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：水面舰艇编队防空和信息化战争评估模型](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：数据的多流形结构分析](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：移动通信中的无线信道"指纹"特征建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：面向节能的单/多列车优化决策问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)
- [E 题：数控加工刀具运动的优化控制](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/E)
- [F 题：旅游路线规划问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/F)

**2014 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：小鼠视觉感受区电位信号(LFP)与视觉刺激之间的关系研究](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：机动目标的跟踪与反跟踪](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：无线通信中的快时变信道建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：人体营养健康角度的中国果蔬发展战略研究](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)
- [E 题：乘用车物流运输计划问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/E)

**2013 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：变循环发动机部件法建模及优化](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：功率放大器非线性特性及预失真模型](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：微蜂窝环境中无线接收信号的特性分析](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：空气中 PM2.5 问题的研究](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)
- [E 题：中等收入定位与人口度量模型研究](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/E)
- [F 题：可持续的中国城乡居民养老保险体系的数学模型研究](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/F)

**2012 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2012%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：基因识别问题及其算法实现](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2012%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：基于卫星无源探测的空间飞行器主动段轨道估计与误差分析](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2012%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：有杆抽油系统的数学建模及诊断](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2012%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：基于卫星云图的风失场(云导风)度量模型与算法探讨](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2012%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)

**2011 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2011%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：基于光的波粒二象性一种猜想的数学仿真](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2011%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：吸波材料与微波暗室问题的数学建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2011%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：小麦发育后期茎杆抗倒性的数学模型](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2011%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：房地产行业的数学建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2011%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)

**2010 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2010%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：确定肿瘤的重要基因信息](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2010%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：与封堵渍口有关的重物落水后运动过程的数学建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2010%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：神经元的形态分类和识别](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2010%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：特殊工件磨削加工的数学建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2010%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)

**2009 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2009%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：我国就业人数或城镇登记失业率的数学建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2009%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：枪弹头痕迹自动比对方法的研究](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2009%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：多传感器数据融合与航迹预测](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2009%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：110 警车配置及巡逻方案](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2009%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)

**2008 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2008%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：汶川地震中唐家山堪塞湖泄洪问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2008%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：城市道路交通信号实时控制问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2008%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：货运列车的编组调度问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2008%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)（原笔记中链接为空，待补）
- [D 题：中央空调系统节能设计问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2008%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)（原笔记中链接为空，待补）

**2007 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2007%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：建立食品卫生安全保障体系数学模型及改进模型的若干理论问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2007%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：械臂运动路径设计问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2007%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：探讨提高高速公路路面质量的改进方案](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2007%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：邮政运输网络中的邮路规划和邮车调运](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2007%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)

**2006 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2006%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：Ad Hoc 网络中的区域划分和资源分配问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2006%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：确定高精度参数问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2006%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：维修线性流量阀时的内筒设计问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2006%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：学生面试问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2006%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)

**2005 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2005%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：Highway Traveling time Estimate and Optimal Routing](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2005%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：空中加油](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2005%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：城市交通管理中的出租车规划](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2005%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：仓库容量有限条件下的随机存贮管理](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2005%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)

**2004 年优秀论文** [📁 合集](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2004%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
- [A 题：发现黄球并定位](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2004%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
- [B 题：使用下料问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2004%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
- [C 题：售后服务数据的运用](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2004%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
- [D 题：研究生录取问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2004%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)

### 6.4 美赛特等奖论文（历年）

- [2017](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2016](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2015](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2014](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2013](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2012](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2012%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2011](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2011%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2010](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2010%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2009](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2009%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2008](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2008%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2007](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2007%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2006](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2006%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2005](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2005%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2004](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2004%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)

---

## 七、学习资源

### 7.1 数模网站

> 交流、下载资料、查比赛动态。

- [MATLAB 技术论坛](http://www.matlabsky.com/)
- [MATLAB 中文论坛](https://www.ilovematlab.cn/)
- [数学中国](http://www.madio.net/portal.php)
- [全国大学生数学建模竞赛](http://www.mcm.edu.cn/)
- [数学建模网](https://www.shumo.com/home/)
- [Toolbox 大全（MATLAB File Exchange）](https://www.mathworks.com/matlabcentral/fileexchange/)

### 7.2 教材、课件与思维导图

- [国防科技大学（教材课件）](https://github.com/zhanwen/MathModel/tree/master/%E6%95%99%E6%9D%90%E5%8F%8A%E8%AF%BE%E4%BB%B6/%E5%9B%BD%E9%98%B2%E7%A7%91%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6)
- [浙江大学课件（PPT）](https://github.com/zhanwen/MathModel/tree/master/%E6%95%99%E6%9D%90%E5%8F%8A%E8%AF%BE%E4%BB%B6/%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6%E8%AF%BE%E4%BB%B6/PPT%E8%AF%BE%E4%BB%B6)
- [数学建模算法思维导图](https://github.com/zhanwen/MathModel/tree/master/Mind)

### 7.3 参考视频

> 按用途分类：**MATLAB 上手 → 数模系统课 → 算法与实战**。

#### MATLAB 工具类

- [机器学习及其 MATLAB 实现——从基础到实践【13 节全】](https://www.bilibili.com/video/BV1Xa411x7Ro) + [对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/MATLAB/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%8F%8A%E5%85%B6MATLAB%E5%AE%9E%E7%8E%B0)
- [Matlab 入门和在线性代数中的应用（zhanwen/MathModel 教程）](https://github.com/zhanwen/MathModel/tree/master/Matlab%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B)
- [数学建模比赛 MATLAB 教学【23P】](https://www.bilibili.com/video/BV1db411Y7uQ)
- [《MATLAB 函数查询及应用案例》](https://www.bilibili.com/video/BV1ry4y1C7fN) + [对应例子](https://github.com/DodgeV/learning-programming/blob/master/books/MATLAB/%E3%80%8AMATLAB%E5%87%BD%E6%95%B0%E6%9F%A5%E8%AF%A2%E5%8F%8A%E5%BA%94%E7%94%A8%E6%A1%88%E4%BE%8B%E3%80%8B.7z)
- [MATLAB 数据挖掘技术系列培训视频【6P】](https://www.bilibili.com/video/bv1Tp4y1y7G7) + [备用](https://www.bilibili.com/video/BV1NV411n7G7?p=66) + [对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/MATLAB/MATLAB%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98%E6%8A%80%E6%9C%AF%E7%B3%BB%E5%88%97%E5%9F%B9%E8%AE%AD%E8%AF%BE%E4%BB%B6_PDF%E7%89%88)
- [Matlab 基础教程](https://www.bilibili.com/video/BV1VJ411p7M6)
- [Matlab 最基础纯手写教程（Taylim）](https://www.bilibili.com/video/BV1q7411g7Dh)
- [Matlab 基础入门与算法实践（老教练）](https://www.bilibili.com/video/BV1FD4y1m78C) + [对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/MATLAB/Matlab%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E4%B8%8E%E7%AE%97%E6%B3%95%E5%AE%9E%E8%B7%B5)

#### 数学建模系统课程

- [走进数学之数学建模（中国大学 MOOC）](https://www.bilibili.com/video/BV1ux411G7k3)
- [数学建模·北航牛薇](https://www.bilibili.com/video/BV1d7411T7BK)
- [数学建模·厦门大学（MOOC）](http://www.icourse163.org/learn/XMU-1001556009)
- [科学计算与数学建模·中南大学（MOOC）](http://www.icourse163.org/learn/CSU-1001985002)
- [数学建模·华中农业大学（MOOC）](http://www.icourse163.org/learn/HZAU-1001658002)
- [数学模型·姜启源](https://www.bilibili.com/video/BV1VJ411w7r3/)
- [数学建模·清风](https://www.bilibili.com/video/BV1DW411s7wi)
- [数学模型·清华大学](https://www.bilibili.com/video/BV1Zx411y7Ah) + [对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/MATLAB/%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1_%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A683%E8%AE%B2)

#### 培训与实战

- [数学建模培训视频·小石老师【14 讲】](https://www.bilibili.com/video/BV1by4y1B7dk) + [对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/MATLAB/%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E5%9F%B9%E8%AE%AD%E8%A7%86%E9%A2%91-%E5%B0%8F%E7%9F%B3%E8%80%81%E5%B8%88-14%E8%AE%B2)
- [数学建模美赛/国赛 算法顶级培训（完）·老教练](https://www.bilibili.com/video/BV14b411v7dT) + [备用](https://www.bilibili.com/video/BV1e54y1e7cU) + [对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/MATLAB/%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E9%AB%98%E9%98%B631%E5%A0%82%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99)
- [【数学建模/零基础/教程】数学建模零基础快速入门教程（附代码）](https://www.bilibili.com/video/BV1Kb41167QZ)
- [数学建模清风第一次直播：传染病模型和微分方程拟合](https://www.bilibili.com/video/BV1Hi4y1t7uu)

---
