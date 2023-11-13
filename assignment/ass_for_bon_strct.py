import rhinoscriptsyntax as rs
import random as rnd
curveId = rs.GetObject("Select a square", rs.filter.curve)
points = rs.CurveEditPoints(curveId)
centroid = rs.CurveAreaCentroid(curveId)[0]
#rs.AddPoints(points)
#rs.AddPoint(centroid)
#rs.AddTextDot('points[0]', points[0])
#rs.AddTextDot('points[1]', points[1])
#rs.AddTextDot('points[2]', points[2])
#rs.AddTextDot('points[3]', points[3])
#rs.AddTextDot('centroid', centroid)
rs.AddCurve((points[0], centroid, points[3]), 1)
rs.AddCurve((points[1], centroid, points[2]), 1)
curve = rs.AddCurve(points)
rs.ScaleObject(curve, centroid, (.5, .5, .5))

