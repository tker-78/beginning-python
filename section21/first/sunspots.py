# 円を描く
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

d = Drawing(400, 200)
d.add(Circle(cx=100, cy=100, r=50, fillColor=None))
renderPDF.drawToFile(d, 'circle.pdf')