# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show a MsCombi 2D chart where data is passed as object.
# The `chart` method is defined to load chart data
def chart(request):

    datasource = {}
    datasource["chart"] = {
        "caption": "Actual Revenues, Targeted Revenues & Profits",
        "subcaption": "Last year",
        "xaxisname": "Month",
        "yaxisname": "Amount (In USD)",
        "numberprefix": "$",
        "theme": "ocean"
    }
    datasource["categories"] = [{
        "category": [
            {"label": "Jan"},
            {"label": "Feb"},
            {"label": "Mar"},
            {"label": "Apr"},
            {"label": "May"},
            {"label": "Jun"},
            {"label": "Jul"},
            {"label": "Aug"},
            {"label": "Sep"},
            {"label": "Oct"},
            {"label": "Nov"},
            {"label": "Dec"}
        ]
    }]

    datasource["dataset"] = [{
            "seriesname": "Actual Revenue",
            "data": [
                {"value": "16000"},
                {"value": "20000"},
                {"value": "18000"},
                {"value": "19000"},
                {"value": "15000"},
                {"value": "21000"},
                {"value": "16000"},
                {"value": "20000"},
                {"value": "17000"},
                {"value": "25000"},
                {"value": "19000"},
                {"value": "23000"}
            ]
        }, {
            "seriesname": "Projected Revenue",
            "renderas": "line",
            "showvalues": "0",
            "data": [
                {"value": "15000"},
                {"value": "16000"},
                {"value": "17000"},
                {"value": "18000"},
                {"value": "19000"},
                {"value": "19000"},
                {"value": "19000"},
                {"value": "19000"},
                {"value": "20000"},
                {"value": "21000"},
                {"value": "22000"},
                {"value": "23000"}
            ]
        }, {
            "seriesname": "Profit",
            "renderas": "area",
            "showvalues": "0",
            "data": [
                {"value": "4000"},
                {"value": "5000"},
                {"value": "3000"},
                {"value": "4000"},
                {"value": "1000"},
                {"value": "7000"},
                {"value": "1000"},
                {"value": "4000"},
                {"value": "1000"},
                {"value": "8000"},
                {"value": "2000"},
                {"value": "7000"}
            ]
        }
    ]

    # Create an object for the mscombi2d chart using the FusionCharts class constructor
    mscombi2dChart = FusionCharts("mscombi2d", "ex1", "100%", 400, "chart-1", "json", datasource)
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    pyramidChart = FusionCharts("pyramid", "ex2", "70%", "385", "chart-2", "json", 
    """{
        "chart": {
            "bgcolor": "FFFFFF",
            "caption": "Revenue distribution for 2017",
            "basefontcolor": "333333",
            "decimals": "0",
            "numbersuffix": "M",
            "numberprefix": "$",
            "pyramidyscale": "40",
            "chartbottommargin": "0",
            "captionpadding": "0",
            "showborder": "0"
        },
        "data": [
            {
                "value": "17",
                "name": "Products",
                "color": "008ee4"
            },
            {
                "value": "21",
                "name": "Services",
                "color": "6baa01"
            },
            {
                "value": "20",
                "name": "Consultancy",
                "color": "f8bd19"
            },
            {
                "value": "5",
                "name": "Others",
                "color": "e44a00"
            }
        ]
    }""")

    # Create an object for the funnel chart using the FusionCharts class constructor
    funnelChart = FusionCharts("funnel", "ex3", "70%", "385", "chart-3", "json", 
    """{
        "chart": {
            "bgcolor": "FFFFFF",
            "caption": "Conversion - 2017",
            "decimals": "1",
            "basefontsize": "11",
            "issliced": "0",
            "ishollow": "1",
            "labeldistance": "8",
            "showBorder": "0"
        },
        "data": [
            {
                "label": "Website Visits",
                "value": "385634"
            },
            {
                "label": "Downloads",
                "value": "145631",
                "color": "008ee4"
            },
            {
                "label": "Interested to Participate",
                "value": "84564",
                "color": "f8bd19"
            },
            {
                "label": "Contracts finalized",
                "value": "50654",
                "color": "6baa01"
            },
            {
                "label": "Adquired",
                "value": "25342",
                "color": "e44a00"
            }
        ]
    }""")

    pie3d = FusionCharts("pie3d", "ex4" , "80%", "400", "chart-4", "json", 
    # The data is passed as a string in the `dataSource` as parameter.
    """{ 
            "chart": {
            "caption": "Age profile of website visitors",
            "subcaption": "Last Year",
            "startingangle": "120",
            "showlabels": "0",
            "showlegend": "1",
            "enablemultislicing": "0",
            "slicingdistance": "15",
            "showpercentvalues": "1",
            "showpercentintooltip": "0",
            "plottooltext": "Age group : $label Total visit : $datavalue",
            "theme": "ocean"
            },
            "data": [
                {"label": "Teenage", "value": "1250400"},
                {"label": "Adult", "value": "1463300"},
                {"label": "Mid-age", "value": "1050700"},
                {"label": "Senior", "value": "491000"}
            ]
    }""")
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'index.html', {'mscombi2dChart' : mscombi2dChart.render(), 'pyramidChart' : pyramidChart.render(),
            'funnelChart' : funnelChart.render(), 'pie3d': pie3d.render()})