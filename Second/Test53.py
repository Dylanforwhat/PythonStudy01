from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line = Line()
line.add_xaxis(["China", "America", "England"])  # 折线图x轴
line.add_yaxis("GDP", [30, 20, 10])  # 折线图y轴

# 设置全局配置项set_global_opts来设置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP data", pos_left="center", pos_bottom="1%"),  # 标题
    legend_opts=LegendOpts(is_show=True),       # 图例
    toolbox_opts=ToolboxOpts(is_show=True),     # 工具箱
    visualmap_opts=VisualMapOpts(is_show=True)  # 视觉映射
)

line.render()  # render代码生成图像
