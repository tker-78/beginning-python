from urllib.request import urlopen
from reportlab .graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF
from datetime import datetime
import pandas as pd
import json

URL = 'https://services.swpc.noaa.gov/json/solar-cycle/predicted-solar-cycle.json'

class SunSpot():
    def __init__(self,
                 date: datetime,
                 number: float,
                 high: float,
                 low: float,
                 flux: float,
                 flux_high: float,
                 flux_low: float):
        self.date = date
        self.number = number
        self.high = high
        self.low = low
        self.flux = flux
        self.flux_high = flux_high
        self.flux_low = flux_low



if __name__ == '__main__':
    file = urlopen(URL)
    data = file.readlines()[0].decode('utf-8')
    js = json.loads(data)

    sunspot_list = []
    for i in range(len(js)):
        obj = SunSpot(datetime.strptime(js[i]["time-tag"], "%Y-%m"),
                      js[i]["predicted_ssn"],
                      js[i]["high_ssn"],
                      js[i]["low_ssn"],
                      js[i]["predicted_f10.7"],
                      js[i]["high_f10.7"],
                      js[i]["low_f10.7"]
                      )
        sunspot_list.append(obj)

    drawing = Drawing(400, 200)
    lp = LinePlot()
    lp.x = 50
    lp.y = 50
    lp.height = 125
    lp.width = 300
    date = [int(x.date.year) for x in sunspot_list]
    number = [x.number for x in sunspot_list]
    high = [x.high for x in sunspot_list]
    low = [x.low for x in sunspot_list]

    lp.data = [list(zip(date, number)),
               list(zip(date, high)),
               list(zip(date, low))]
    drawing.add(lp)
    renderPDF.drawToFile(drawing, 'report.pdf', 'Sunspots')









