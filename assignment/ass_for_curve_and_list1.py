import rhinoscriptsyntax as rs

crves = rs.GetObject('select a curve', rs.filter.curve)
pts = rs.CurveEditPoints(crves)
origin = rs.CurveAreaCentroid(crves)[0]
rs.AddPoint(origin)
rs.ScaleObject(crves, origin, (.8, .8, .8), True)

