"""
演示 python pymysql库的基本操作
"""
from pymysql import Connection
# 构建到MySQL的链接对象
conn = Connection(
    host = "localhost", # 主机名
    port = 3306,
    user = "root",
    password = "Qwlxz3348185",# 密码要写对
    autocommit=True  # 不用每次commit确认，自动确认
)
# 执行非查询性质sql语句
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("world")
# 执行sql
cursor.execute("insert into student values(6,'xiaofa',44,'nan')")
# 通过commit确认
conn.commit()
# 关闭连接
conn.close()