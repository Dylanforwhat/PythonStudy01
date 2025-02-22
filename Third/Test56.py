import pandas as pd
import numpy as np
a = 'd:/pandas/xx.xlsx'
b = pd.read_excel(a)
c = pd.pivot_table(b,index = ['部门','销售人员'],values = ['数量','金额'],columns ='所属区域',aggfunc = [sum,np.mean] ) # values是定义列，columns是在values列的基础上再增加列的分类,aggfunc是采用什么方式聚合

d = pd.crosstab([b.dates.dt.month,b.所属区域],b.部门,margins = True) # margins 汇总小计  crosstab就是单纯计数用的


