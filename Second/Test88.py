"""
演示 python pymysql库的基本操作
"""
from pymysql import Connection

# 构建到MySQL的链接对象
conn = Connection(
    host = "localhost", # 主机名
    port = 3306,
    user = "root",
    password = "Qwlxz3348185" # 密码要写对
)

# 执行非查询性质sql语句
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("world")
# 对游标对象使用sql语句
# cursor.execute("create table test_pymysql(id int);")

# 执行查询性质sql语句 fetchall() 得到一个元组
cursor.execute("select * from student")
results = cursor.fetchall()
for e in results:
    print(e)
conn.close()