from object_detection_with_timestamps import df
from bokeh.plotting import figure
from bokeh.io import output_file, show

x = df["Entry"]
y = df["Exit"]
f = figure(plot_width=500, plot_height=500, x_axis_type="datetime", sizing_mode="scale_width")
f.title.text="Motion Graph"
f.title.text_color="Gray"
f.title.text_font="comic sans"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color=None
f.yaxis.ticker.desired_num_ticks = 1
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Entry Time/Date"
f.yaxis.axis_label="Exit Time/date"
q = f.quad(left=x, right=y, top=1, bottom=0, color="green")
output_file("graph.html")
show(f)
