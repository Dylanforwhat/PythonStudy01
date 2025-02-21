import pandas as pd
a = 'd:/pandas/'
b = pd.read_excel(a)
b = b.groupby(b.姓名.str[0])[['语文','数学']].sum() #按姓名首字母分组，对数学和语文成绩进行合计聚合

b = b.groupby(b.time.dt.year)[['语文','数学']].sum() #按年份分组，对数学和语文成绩进行合计聚合