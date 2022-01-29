from object_detection_with_timestamps import df
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df["Entry_string"] = df["Entry"].dt.strftime("%d-%m-%Y::%I:%M:%S %p")
df["Exit_string"] = df["Exit"].dt.strftime("%d-%m-%Y::%I:%M:%S %p")
column_data_source = ColumnDataSource(df)
hover = HoverTool(tooltips=[("Entry", "@Entry_string"), ("Exit", "@Exit_string")])

f = figure(plot_width=500, plot_height=500, x_axis_type="datetime", sizing_mode="stretch_width")
f.title.text="Motion Graph"
f.title.text_color="Gray"
f.title.text_font="comic sans"
f.title.text_font_style="bold"
f.yaxis.ticker.desired_num_ticks=1
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Entry Time/Date"
f.yaxis.axis_label="Exit Time/date"
f.add_tools(hover)
q = f.quad(left="Entry", right="Exit", top=1, bottom=0, color="green", source=column_data_source)
output_file("graph.html")
show(f)
