import rhinoscriptsyntax as rs
curve = rs.GetObject('select a curve', rs.filter.curve)
points = rs.CurveEditPoints(curve)
listOfPoints = []
for point in points:
    listOfPoints.append(point)
for aPoint in range(len(listOfPoints)):
    print aPoint, '=', listOfPoints[aPoint]
    rs.AddTextDot(aPoint, listOfPoints[aPoint])
