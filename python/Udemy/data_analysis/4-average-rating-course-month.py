import justpy as jp
import pandas

data=pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Month"]=data["Timestamp"].dt.strftime("%Y-%m")
month_average_course=data.groupby(["Month", "Course Name"])["Rating"].mean().unstack()
def_chart = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating for a particular in a month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Rating'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ''
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.75
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""


def app():
    web_page = jp.QuasarPage()
    h1 = jp.QDiv(a=web_page, text="Analysis of Course Reviews", classes="text-h4 text-center q-pa-md text-weight-bolder")
    p1 = jp.QDiv(a=web_page, text="This graph represents course review analysis", classes="text-subtitle2 text-left q-pa-md weight-lighter")
    high_chart = jp.HighCharts(a=web_page, options=def_chart)
    high_chart.options.title.text="Average Rating for a particular course in a month"
    high_chart.options.xAxis.categories = list(month_average_course.index)
    high_chart_plot_data = [{"name" : var1, "data" : [var2 for var2 in month_average_course[var1]]} for var1 in month_average_course.columns]
    high_chart.options.series= high_chart_plot_data
    return web_page


jp.justpy(app)
