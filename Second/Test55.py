from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

# 柱状图对象
bar = Bar()
# x轴数据
bar.add_xaxis(["China","America","England"])
# y轴数据
bar.add_yaxis("GDP",[30,20,10],label_opts= LabelOpts(position="right"))# 标签最右侧显示
# 反转xy轴
bar.reversal_axis()

# 绘图
bar.render("BarTest.html")