import rhinoscriptsyntax as rs
#Input rectangle
crvGUID = rs.GetObject('select a rectangle', rs.filter.curve)
#rs.HideObject(crvGUID)

#Find edit points
points = rs.CurveEditPoints(crvGUID)

#Find centroid
centroid = rs.CurveAreaCentroid(crvGUID)[0]

#Create points in Rhino space
rs.AddPoints(points)
rs.AddPoint(centroid)

#Label points
rs.AddTextDot('points[0]', points[0])
rs.AddTextDot('points[1]', points[1])
rs.AddTextDot('points[2]', points[2])
rs.AddTextDot('points[3]', points[3])
rs.AddTextDot('centroid', centroid)

##CREATE GEOMETRY##
#Pseudo Code
#
##draw line from points[0], centroid, points[1]
rs.AddCurve((points[0], centroid, points[1]))

#draw line from points[1], centroid, points[2]
rs.AddCurve((points[1], centroid, points[2]))

#draw line from points[2], centroid, points[3]
rs.AddCurve((points[2], centroid, points[3]))

#draw line from points[3], centroid, points[0]
rs.AddCurve((points[3], centroid, points[0]))

#Construct a closed curve from corner points
curve = rs.AddCurve(points)

#Scale curve using a centroid as origin
rs.ScaleObject(curve, centroid, (.5, .5, .5))