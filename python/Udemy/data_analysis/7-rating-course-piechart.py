import justpy as jp
import pandas

data=pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
pie_slice = data.groupby(["Course Name"])["Rating"].count()

def_chart = """
{
    chart: {
    plotBackgroundColor: 'white',
    plotBorderWidth: 2.5,
    plotBorderColor: 'gray',
    plotShadow: false,
    type: 'pie'
    },
    title: {
        text: 'Browser market shares in January, 2018'
    },
    tooltip: {
        pointFormat: '<b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""


def app():
    web_page = jp.QuasarPage()
    h1 = jp.QDiv(a=web_page, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=web_page, text="This graph represents course reviews analysis",
                 classes="text-subtitle2 text-left q-pa-md weight-lighter")
    high_chart = jp.HighCharts(a=web_page, options=def_chart)
    high_chart.options.title.text = "Ratings for courses"
    high_chart_graph_data = [{"name": var1, "y": var2} for var1, var2 in zip(pie_slice.index, pie_slice)]
    high_chart.options.series[0].data = high_chart_graph_data

    return web_page


jp.justpy(app)
