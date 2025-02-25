import pandas as pd
a = 'd:/pandas/转换.xlsx'
b = pd.read_excel(a,'Sheet1')
上月 = b.销售金额.shift()
环比 = b.销售金额 - 上月
b['环比增长'] = 环比
