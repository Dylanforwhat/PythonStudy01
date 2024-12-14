"""
时间轴图表
pyecharts 提供Timeline()时间线功能
时间线就是一个一维的x轴，轴上每个点都是一个图表对象
"""
from pyecharts.charts import Bar,Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts

bar1 = Bar()
bar1.add_xaxis(["China", "America", "England"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))  # 标签最右侧显示
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["China", "America", "England"])
bar2.add_yaxis("GDP", [40, 34, 14], label_opts=LabelOpts(position="right"))  # 标签最右侧显示
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["China", "America", "England"])
bar3.add_yaxis("GDP", [60, 54, 30], label_opts=LabelOpts(position="right"))  # 标签最右侧显示
bar3.reversal_axis()

# 设置时间线
timeline = Timeline(
    {"theme":ThemeType.LIGHT} # 主题设置
)
timeline.add(bar1,"season1")
timeline.add(bar2,"season2")
timeline.add(bar3,"season3")

# 自动播放设置
timeline.add_schema(
    play_interval=1000, # 时间间隔 毫秒
    is_timeline_show=True,# 是否在自动播放的时候显示时间线
    is_auto_play=True,# 是否自动播放
    is_loop_play=True# 是否循环播放
)



timeline.render("TimelineTest.html")
