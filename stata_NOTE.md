# stata笔记🌍

- [基本](#基础)
- [常用命令](#常用命令)
- [编译型语言](#编译型语言)
- [横截面分析](#横截面分析)
- [时间序列模型](#时间序列模型)
- [面板数据](#面板数据)
- [免责声明](#免责声明)
- [参考资源](#参考资源)

------

## 基本
* stata允许第三方插件
* 三种文件：数据文件、do文件、log文件
> + stata自己的数据文件后缀名为`.dta`,支持导入其他格式如`.xls` `.xlsx` `.csv`
> + 可重复性是科学研究的核心，而分析日志(log file)是可重复性的核心，除此而外还有do文件
> + do文件记录命令可通过按钮或`Ctrl+D`重复执行，建议将命令保存在do文件中
> + log文件可以记录分析过程:`File`==>`Log`==>`Begin`
> + 或直接输入命令`log using log_file_name [,[append|replace] [text|smcl] name(logname)]`
> > + `log_file_name`是log文件的名字
> > + `append`若文件存在，附加在文件上
> > + `replace`若文件存在，替换这个文件，若文件不存在则都会创造新文件，若文件已经存在而未指定则会报错
> > + `smcl`为stata默认的log文件格式，可以保存各种颜色，可以转换为`.log`
> > + `text`为单色，便于在文本编辑器中打开
> > + `name(log_for_sb)`打开不同的log文件给不同的合作者
> > + `log close [logname]`若没有起名字就不用加文件名
> > + `log close_all`关闭所有log文件，包括起名字没起名字
>
> + 读取的时候`File`==>`Log`==>`view`

## 常用命令
#### Some useful Stata commands
* `ssc install XXX`   //access routines from the SSC Archive
* `help commands`    //online help on a specific command
* `findit`    //online references on a keyword or topic
* `log`    //log output to an external file
* `tsset`   // define the time indicator for timeseries or panel data
* `compress`   // economize on space used by variables
* `quietly`   // do not show the results of a command
* `update query`   // see if Stata is up to date
* `adoupdate`   // see if user-written commands are up to date

#### Data manipulation commands
* 可以通过命令的方式录入数据集
```
input X1 X2 ...
1 2 3
end
save XXX,replace    // 如路径下已经存在XXX同名数据集，要指定replace(慎用)
```
* 也可以通过菜单窗口的方式录入数据
> + `edit`打开窗口写入数据，如果内存有数据，可对数据进行修改
* 还可以使用自带的auto横截面数据,命令可用`use`
> + `sysuse "D:\stata\auto.dta"`
* 还可以通过复制粘贴创建新的数据集
* 还可以导入excel格式的数据
> + `import excel "energy.xls", sheet("stata") firstrow clear`
* 还可以导入文本格式的数据
> + `import delimited diamonds.csv,clear`
* `describe,short`只显示头部
* `describe [variable]`全部显示或显示变量名
* `list in 1/10`查看此数据集的前10行
* `rename 时间 var1`将时间变量重命名为var1
* `rename (var1 var2 var3 var4 var5 var6) (year total coal oil gas clean)`也可以一次性完成
* `generate volume = x*y*z`通过算式创造一个新的变量
* `replace`    // modify an existing variable
* `renvars`    // rename a set of variables
* `sort`    // change the sort order of the dataset
* `drop`    // drop certain variables and/or observations
* `keep`    // keep only certain variables and/or observations
* `append`    // combine datasets by stacking
* `merge`    // merge datasets (one-to-one or match merge)
* `encode`    // generate numeric variable from categorical variable
* `recode`    // recode categorical variable
* `destring`    // convert string variables to numeric
* `foreach`    // loop over elements of a list, performing a block of code
* `forvalues`    // loop over a numlist, performing a block of code
* `local`    // define or modify a local macro (scalar variable)
* `insheet`    // load a text file in tab- or comma-delimited format
* `infile`    // load a text file in space-delimited format or as defined in a dictionary
* `outfile`    // write a text file in space- or comma-delimited format
* `outsheet`    // write a text file in tab- or comma-delimited format
* `contract`    // make a dataset of frequencies
* `collapse`    // make a dataset of summary statistics
* `tab`    // abbreviation for tabulate   // 1- and 2-way tables
* `table`    // tables of summary statistics

#### Statistical commands
* `count if price > 10000`
* `count if missing`
* `isid mpg`    //变量mpg能否独特的区分每一行
* `isid price make`
* `unique mpg weight`    //需要先安装unique，检测数据集中weight和mpg都不一样的数据个数
* `codebook [var] [if] [in] [,option]`    //提供变量的一些信息,各种分位
* `codebook price if price > 5000`
* `codebook price in 10/20`   #/#
* `codebook price in 10` #
* `codebook price in 10/l`       #/l  10分位到末尾
* `codebook price in f/10`       f/#  开头到10分位
* summarize [var] [if] [in] [weight] [,option]  // 也可以简写为sum或summ
* summarize price,detail   //提供额外的统计量 
* correlate    // correlation matrices
* `ci means [varlist] [if] [in] [weight] [,options]`计算几个连续变量平均值的置信区间，平均值可以简写为`mean`
* `cii means #obs #mean #sd [,level(#)]`也可以指定有多少个观测值，平均值是多少，标准差是多少，置信水平默认为95%，可以更改
* `ci mean mpg price, level(90)`置信水平改为90%
* `cii mean 166 19509 4379, level(95)`指定166个变量，平均值为19509，标准差为4379，置信水平95%
* 分类变量的置信区间
> + `ci proportions [varlist] [if] [in] [weight] [,prop_options options]`可以简写为`prop`,但只能用于二分类变量
> + `proportion varlist [if] [in] [weight] [,options]`多分类变量的置信区间，同样可以简写为``
> + `prop foreign rep78`计算多个变量时，会默认去掉缺失值,造成变量个数变少
> + `prop foreign rep78,miss`不去掉缺失值
* 查看变量的相关性
* `pwcorr [varlist] [if] [in] [weight] [,pwcorr_options]`可以简写为`pwrr`
* `pwrr price headroom mpg displacement`
* `pwrr price headroom mpg displacement,sig`将P值标出来
* `pwrr price headroom mpg displacement,star(0.05)`将P值<0.05的相关系数标上star
* 绘制相关性散点图矩阵
* `graph matrix varlist [if] [in] [weight] [,options]`画出完全对称的散点图矩阵
* `graph matrix varlist,half`只画一半
* `ttest`    // perform 1-, 2-sample and paired t-tests
* `anova`    // 1-, 2-, n-way analysis of variance
* `regress`    // least squares regression
* `predict`    // generate fitted values, residuals, etc.
* `test`    // test linear hypotheses on parameters
* `lincom`    // linear combinations of parameters
* `cnsreg`    // regression with linear constraints
* `testnl`    // test nonlinear hypothesis on parameters
* `margins`    // marginal effects (elasticities, etc.)
* `ivregress`    // instrumental variables regression
* `prais`    // regression with AR(1) errors
* `sureg`    // seemingly unrelated regressions
* `reg3`    // three-stage least squares
* `qreg`    // quantile regression

#### Drawing commands
* `histogram varname [if] [in] [weight] [, [continuous_opts | discrete_opts] options]`柱状图
> + varname:不是varlist，因此只能有一个变量
> + 可简写为`hist`
> + 默认是`hist price, den`，也可改为`hist price, freq`等
> + `hist price, freq bin(5)`改变宽度
> + 增加密度曲线`hist price, freq bin(5) normal`
> + 通过`foreigh`变量分组`hist price, by(foreign)`
* `graph box  yvars [if] [in] [weight] [, options]`箱子是竖着的
* `graph hbox yvars [if] [in] [weight] [, options]`箱子是横着的
> + `graph box price, over(foreigh)`根据foreign分组
* `graph matrix X1 ... Xn, half`绘制矩阵散点图
* `graph twoway connect Y year || lfit Y year`绘制时间序列曲线并拟合一条直线
* `vioplot price, over(foreigh)`小提琴图，根据foreign分组 
* `set scheme s1mono`stata重启前设置为s1mono主题,重启后为s2color主题
* `set scheme s1mono, perm`stata永久设置为s1mono主题
* `twoway plot varlist [if] [in] [, twoway_options]`
> + `plot`可以是scatter,line,connected,area,bar等
> + `varlist`中最后一个是x，前面不管多少个全是y
> + `if`定义自变量的范围，`in`定义所取观测值的范围，`twoway_options`定义坐标范围、标题、注释等
> + `twoway line y1 y2 ... x`绘制折线图
> + `twoway connected y1 y2 ... x`绘制带数据标记点的折线图
> + `twoway dropline y1 y2 ... x`绘制垂直线图
> + `twoway spike y1 y2 ... x`绘制脉冲图,如果被挡住,可以选择将y和x换一下位置
> + `twoway spike y1 y2 x,scheme(s2color)`或者换一个主题颜色
> + `twoway area y1 y2 ... x`绘制面积图,如果被挡住,可以选择将y和x换一下位置
> + `twoway lowess y1 y2 ... x`绘制LOWESS图,相对于散点图更平滑,如果被挡住,可以选择将y和x换一下位置
> + `lowess y1 y2 ... x`也可直接加上散点
> + `twoway scatter y1 y2 y3 ... x`绘制散点图的进阶形式，也可以只有一个y
> + `twoway scatter varlist, msymbol(D) mcolor(blue) msize(medium)`
> + `msymbol`改变形状（`help symbolstyle`）
> + `mcolor`改变颜色（`help colorstyle`）
> + `msize`改变大小（`help markersizestyle`）
> + `twoway scatter mpg weight, by(foreign)`通过foreign分组，分绘两个图
> + `twoway (scatter mpg weight if foreign == 0)(scatter mpg weight if foreign == 1), legend(label(1 "Domestic") label(2 "Foreign"))`也可以将分绘的两个图合并为一个图


#### Limited dependent variable estimation commands
* `logit, logistic`    // logit model, logistic regression
* `probit`    // binomial probit model
* `tobit`    // one- and two-limit Tobit model
* `cnsreg`    // Censored normal regression (generalized Tobit)
* `ologit, oprobit`    // ordered logit and probit models
* `mlogit`    // multinomial logit model
* `poisson`    // Poisson regression
* `heckman`    // selection model
* `truncreg depvar[indepvars] [if] [in] [weight] [, options]`
* `truncreg y x1 x2 x3 , ll(#)  ul(#)`   // 其中选择项ll(#)表示lower limit，左侧断尾，ul(#)表示uppper limit，右侧断尾，如果同时使用这两个选择项，表示双侧断尾。

#### Time series estimation commands
* `arima`    // Box–Jenkins models, regressions with ARMA errors
* `arfima`    // Box–Jenkins models with long memory errors
* `arch`    // models of autoregressive conditional heteroskedasticity
* `dfgls`    // unit root tests
* `corrgram`   // correlogram estimation
* `var`    // vector autoregressions (basic and structural)
* `irf`    // impulse response functions, variance decompositions
* `vec`    // vector error–correction models (cointegration)
* `sspace`    // state-space models
* `dfactor`    // dynamic factor models
* `ucm`    // unobserved-components models
* `rolling`   // prefix permitting rolling or recursive estimation over subsets

#### Panel data estimation commands
* `xtreg,fe`    // fixed effects estimator
* `xtreg,re`    // random effects estimator
* `xtgls`    // panel-data models using generalized least squares
* `xtivreg`    // instrumental variables panel data estimator
* `xtlogit`    // panel-data logit models
* `xtprobit`    // panel-data probit models
* `xtpois`    // panel-data Poisson regression
* `xtgee`    // panel-data models using generalized estimating equations
* `xtmixed`    // linear mixed (multi-level) models
* `xtabond`    // Arellano-Bond dynamic panel data estimator


## 横截面分析
#### 回归分析

```
use nerlove.dta,clear
reg lntc lnpf lnpk  lnpl
reg lntc lnpf lnpk  lnpl ,noc
predict yhat    			   //  拟合被解释变量GDP
predict e,residual             //  计算残差
rvfplot
tobit depvar [indepvars] [if] [in] [weight] ,ll[(#)] ul[(#)] [options]
//归并回归用到的命令，ll[(#)]表示left-censoringlimit， ul[(#)]表示right-censoring limit
tobit y c x1 x2x3，ll(#)  ul(#)
//其中选择项ll(#)表示左侧归并，ul(#)表示右侧归并，如果同时选择这两个，表示左右双边规定，即介于两个值之间。
```

#### 参数检验
* `regress lntc lnpk  lnpl`
* `test lnpk=0.5`                      //检验系数
* `test lnpk=lnpl`
* `estat hettest`                     //异方差BP检验
* `estat imtest,white`                //异方差white检验
* `estat vif`                         //多重共线性检验

#### 带约束条件检验
* `cons  1 lnpk+lnpl=1`
* `cons  2 lnpk+lnpl=1.6`
* `cnsreg lntc lnpk  lnpl,constraints(1)`  //有约束的回归
* `cnsreg lntc lnpk  lnpl,constraints(2)`  //有约束的回归
* `bootstrap, reps(200):regress lntc lnpk  lnpl`   //bootstrap 方法的回归
* `bootstrap _b :regress lntc lnpk  lnpl`        //bootstrap 方法的回归

#### 稳健回归
* `regress lntc lnpk  lnpl`
* `estimates  store model1`
* `reg lntc lnpk  lnpl,robust`
* `estimates store model2`
* `esttab model*  using huigui.rtf,r2 ar2 nogap replace`

## 时间序列模型
#### 时间序列声明

```
use 时间序列数据.dta, clear
tsset year   //时间序列声明
```

#### 单位根检验

```
use 时间序列数据.dta, clear
dfuller d.m,lag(2)`                //ADF检验
dfuller m,nocon regress`           //ADF检验
dfuller m,trend regress
pperron m,lag(2)`                  //PP检验    
pperron m,nocon regress
pperron d.m,regress
dfgls m`                          //DF-GLS检验
kpss  m,notrend`                   //KPSS检验
```

#### ECM单位根检验
* `reg m s g` 
* `estimates  store model1`
* `predict ecm,residual`
* `reg d.m d.s d.g ecm`   //ECM模型

#### VAR模型

```
varsoc m s g ,maxlag(5)
var m s g ,lags(1/4)
varstable,graph
vargranger
irf create myrif,set(myrif) replace
irf graph irf
```

#### VECM模型
* `vecrank m s g,lags(4)`
* `varsoc m s g,maxlag(5)`
* `vec m s g,lags(4)` 
* `reg m s g` 
* `vecstable,graph`

## 面板数据
#### 面板声明
````
use FDI.dtar, clear
xtset country year  
//其中"country"代表实体或小组(i)，“year”表示时间变量(t)。
//注意事项：如果在使用xtset后出现
````

## 免责声明
除去特别小的工作，你编写的代码应当方便他人阅读。能力往往伴随着责任，你 有能力 在 Bash 中玩一些奇技淫巧并不意味着你应该去做！:)

## 参考资源
+ [医咖会Stata系列教程](https://space.bilibili.com/44532954/video)
+ [Stata 统计分析软件 教程](https://www.bilibili.com/video/av36991912)
+ [用stata做统计分析](https://www.bilibili.com/video/BV1b5411Y7QM?p=20)&[资料](https://github.com/DodgeV/learning-programming/tree/master/books/stata/stata%E6%95%99%E7%A8%8B%E8%B5%84%E6%96%99)
