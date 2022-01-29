import justpy as jp
import pandas
from datetime import datetime


data=pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Week"]=data["Timestamp"].dt.strftime("%m-%U")
week_average=data.groupby(["Week"]).mean()
def_chart = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Week/Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating by Week'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Weekly Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""


def app():
    web_page = jp.QuasarPage()
    h1 = jp.QDiv(a=web_page, text="Analysis of Course Reviews", classes="text-h4 text-center q-pa-md text-weight-bolder")
    p1 = jp.QDiv(a=web_page, text="This graph represents course review analysis", classes="text-subtitle2 text-left q-pa-md weight-lighter")
    high_chart = jp.HighCharts(a=web_page, options=def_chart)
    high_chart.options.title.text="Average Rating by Week"
    high_chart.options.xAxis.categories=list(week_average.index)
    high_chart.options.series[0].data=list(week_average["Rating"])
    return web_page


jp.justpy(app)
