import pandas as pd
a = 'd:/pandas/duquwenjian.txt'
b = pd.read_csv(a,header = None,names = ['性别','姓名','年龄','手机','地址','日期'],index_col = '日期',nrows = 3)
print(b)