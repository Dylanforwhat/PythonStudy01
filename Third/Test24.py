import pymysql
import pandas as pd
a = pymysql.connect(host = 'localhost',user = 'root',password = 'Qwlxz3348185',database = 'powernode',charset = 'utf8')
b = pd.read_sql('select * from emp',con = a)
print(b)
