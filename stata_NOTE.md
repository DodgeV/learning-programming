## 常用命令
#### Some useful Stata commands
* ssc install XXX   //access routines from the SSC Archive
* help -search    //online help on a specific command
* findit    //online references on a keyword or topic
* log    //log output to an external file
* tsset   // define the time indicator for timeseries or panel data
* compress   // economize on space used by variables
* quietly   // do not show the results of a command
* update query   // see if Stata is up to date
* adoupdate   // see if user-written commands are up to date

#### Data manipulation commands
* sysuse "D:\stata\auto.dta", clear   //打开auto横截面数据
* use auto.dta    //load a Stata data set
* describe,short    //只显示头部
* describe [variable]    //全部显示或显示变量名
* generate    // create a new variable
* replace    // modify an existing variable
* rename    // rename variable
* renvars    // rename a set of variables
* sort    // change the sort order of the dataset
* drop    // drop certain variables and/or observations
* keep    // keep only certain variables and/or observations
* append    // combine datasets by stacking
* merge    // merge datasets (one-to-one or match merge)
* encode    // generate numeric variable from categorical variable
* recode    // recode categorical variable
* destring    // convert string variables to numeric
* foreach    // loop over elements of a list, performing a block of code
* forvalues    // loop over a numlist, performing a block of code
* local    // define or modify a local macro (scalar variable)
* save    // write the contents of memory to a Stata data set
* insheet    // load a text file in tab- or comma-delimited format
* infile    // load a text file in space-delimited format or as defined in a dictionary
* outfile    // write a text file in space- or comma-delimited format
* outsheet    // write a text file in tab- or comma-delimited format
* contract    // make a dataset of frequencies
* collapse    // make a dataset of summary statistics
* tab    // abbreviation for tabulate   // 1- and 2-way tables
* table    // tables of summary statistics

#### Statistical commands
* count if price > 10000
* count if missing
* isid mpg    //变量mpg能否独特的区分每一行
* isid price make
* unique mpg weight    //需要先安装unique，检测数据集中weight和mpg都不一样的数据个数
* codebook [var] [if] [in] [,option]    //提供变量的一些信息,各种分位
* codebook price if price > 5000
* codebook price in 10/20   #/#
* codebook price in 10 #
* codebook price in 10/l       #/l  10分位到末尾
* codebook price in f/10       f/#  开头到10分位
* summarize [var] [if] [in] [weight] [,option]  // 也可以简写为sum或summ
* summarize price,detail   //提供额外的统计量 
* correlate    // correlation matrices
* ttest    // perform 1-, 2-sample and paired t-tests
* anova    // 1-, 2-, n-way analysis of variance
* regress    // least squares regression
* predict    // generate fitted values, residuals, etc.
* test    // test linear hypotheses on parameters
* lincom    // linear combinations of parameters
* cnsreg    // regression with linear constraints
* testnl    // test nonlinear hypothesis on parameters
* margins    // marginal effects (elasticities, etc.)
* ivregress    // instrumental variables regression
* prais    // regression with AR(1) errors
* sureg    // seemingly unrelated regressions
* reg3    // three-stage least squares
* qreg    // quantile regression

#### Limited dependent variable estimation commands
* logit, logistic    // logit model, logistic regression
* probit    // binomial probit model
* tobit    // one- and two-limit Tobit model
* cnsreg    // Censored normal regression (generalized Tobit)
* ologit, oprobit    // ordered logit and probit models
* mlogit    // multinomial logit model
* poisson    // Poisson regression
* heckman    // selection model
* truncreg depvar[indepvars] [if] [in] [weight] [, options]
* truncreg y x1 x2 x3 , ll(#)  ul(#)   // 其中选择项ll(#)表示lower limit，左侧断尾，ul(#)表示uppper limit，右侧断尾，如果同时使用这两个选择项，表示双侧断尾。

#### Time series estimation commands
* arima    // Box–Jenkins models, regressions with ARMA errors
* arfima    // Box–Jenkins models with long memory errors
* arch    // models of autoregressive conditional heteroskedasticity
* dfgls    // unit root tests
* corrgram    // correlogram estimation
* var    // vector autoregressions (basic and structural)
* irf    // impulse response functions, variance decompositions
* vec    // vector error–correction models (cointegration)
* sspace    // state-space models
* dfactor    // dynamic factor models
* ucm    // unobserved-components models
* rolling   // prefix permitting rolling or recursive estimation over subsets

#### Panel data estimation commands
* xtreg,fe    // fixed effects estimator
* xtreg,re    // random effects estimator
* xtgls    // panel-data models using generalized least squares
* xtivreg    // instrumental variables panel data estimator
* xtlogit    // panel-data logit models
* xtprobit    // panel-data probit models
* xtpois    // panel-data Poisson regression
* xtgee    // panel-data models using generalized estimating equations
* xtmixed    // linear mixed (multi-level) models
* xtabond    // Arellano-Bond dynamic panel data estimator


## 横截面分析
#### 回归分析
* use nerlove.dta,clear
* reg lntc lnpf lnpk  lnpl 
* reg lntc lnpf lnpk  lnpl ,noc
* predict yhat                   //  拟合被解释变量GDP
* predict e,residual              //  计算残差
* rvfplot  
* tobit depvar [indepvars] [if] [in] [weight] ,ll[(#)] ul[(#)] [options]      //归并回归用到的命令，ll[(#)]表示left-censoringlimit， ul[(#)]表示right-censoring limit
* tobit y c x1 x2x3，ll(#)  ul(#)    //其中选择项ll(#)表示左侧归并，ul(#)表示右侧归并，如果同时选择这两个，表示左右双边规定，即介于两个值之间。

#### 参数检验
* regress lntc lnpk  lnpl
* test lnpk=0.5                      //检验系数
* test lnpk=lnpl
* estat hettest                     //异方差BP检验
* estat imtest,white                //异方差white检验
* estat vif                         //多重共线性检验

#### 带约束条件检验
* cons  1 lnpk+lnpl=1
* cons  2 lnpk+lnpl=1.6
* cnsreg lntc lnpk  lnpl,constraints(1)  //有约束的回归
* cnsreg lntc lnpk  lnpl,constraints(2)  //有约束的回归
* bootstrap, reps(200):regress lntc lnpk  lnpl   //bootstrap 方法的回归
* bootstrap _b :regress lntc lnpk  lnpl        //bootstrap 方法的回归

#### 稳健回归
* regress lntc lnpk  lnpl
* estimates  store model1
* reg lntc lnpk  lnpl,robust
* estimates store model2
* esttab model*  using huigui.rtf,r2 ar2 nogap replace

## 时间序列模型
#### 时间序列声明
* use 时间序列数据.dta, clear
* tsset year   //时间序列声明

#### 单位根检验
* use 时间序列数据.dta, clear
* dfuller d.m,lag(2)                //ADF检验
* dfuller m,nocon regress           //ADF检验
* dfuller m,trend regress
* pperron m,lag(2)                  //PP检验                   
* pperron m,nocon regress           
* pperron d.m,regress
* dfgls m                          //DF-GLS检验
* kpss  m,notrend                   //KPSS检验

#### ECM单位根检验
* reg m s g 
* estimates  store model1
* predict ecm,residual
* reg d.m d.s d.g ecm   //ECM模型

#### VAR模型
* varsoc m s g ,maxlag(5)
* var m s g ,lags(1/4)
* varstable,graph
* vargranger
* irf create myrif,set(myrif) replace
* irf graph irf

#### VECM模型
* vecrank m s g,lags(4)
* varsoc m s g,maxlag(5)
* vec m s g,lags(4) 
* reg m s g 
* vecstable,graph

## 面板数据
#### 面板声明
* use FDI.dtar, clear
* xtset country year   //在这种情况下"country"代表实体或小组(i)，“year”表示时间变量(t)。
* > 注意事项：如果在使用xtset后出现以下错误: varlist: country: string variable not allowed
* > 解决方案为：encode country, gen(country1)
* > 在xtset命令中使用“country1”而不是“country”   需要使用数值型类型
* xtdes
* xtline lngdp   //探索面板数据

#### 单位根检验
* xtunitroot llc lngdp,lags(2) trend
* xtunitroot llc d.lngdp,lags(2) trend
* xtunitroot ips lngdp
* xtunitroot ips d.lngdp

#### 协整检验
* xtwest lngdp lnfdi lni,lags(2)

#### 异方差检验
* xttest3 

#### 序列相关检验,适用于的长面板数据(20-30年以上)
* xtserial y x1

#### 混合回归/OLS回归
* reg lngdp lnfdi lnie
* reg lngdp lnfdi lnie,robust
* reg lngdp lnfdi lnie,vce(cluster id)

#### 固定效应
* xtreg lngdp lnfdi lnie lnex lnim  lnci lngp,fe
* xtreg lngdp lnfdi lnie lnex lnim  lnci lngp,fe,fe vce (cluster id)
* xi:xtreg lngdp lnfdi lnie lnex lnim  lnci lngp  i.id,vce(cluster id) //LSDV 考虑个体固定效应
* tab year,gen(year)
* xtreg lngdp lnfdi lnie lnex lnim  lnci lngp year2-year14,fe 
* xtreg lngdp lnfdi lnie lnex lnim  lnci lngp year2-year14,fe vce (cluster id)
* test year2=year3=year4=year5=0

#### 随机效应
* xtreg lngdp lnfdi lnie lnex lnim  lnci lngp,re mle
* xtreg lngdp lnfdi lnie lnex lnim  lnci lngp,vce (cluster id) 
* xtreg lngdp lnfdi lnie lnex lnim  lnci lngp,re mle    //随机效应的MLE参数估计方法

#### Hausman检验--随机和固定效应的检验
* xtreg lngdp lnfdi lnie lnex lnim  lnci lngp,re
* est store re
* xtreg lngdp lnfdi lnie lnex lnim  lnci lngp,fe
* est store fe
* hausman fe re
* est table re fe, b(%6.3f) star(0.1 0.05 0.01) 
* outreg2 [fe re] using daqinxueshu.doc,stats(coef,tstat) addstat(Ajusted R2,`e(r2_a)') replace

