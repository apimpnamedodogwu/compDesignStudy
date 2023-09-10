import rhinoscriptsyntax as rs
pointList = []
curveGUID = rs.GetObject('select a closed planar curve', rs.filter.curve)
attrPt = rs.GetObject('select point', rs.filter.point)
for i in range(10):
    for j in range (10):
        x = i
        y = j
        z = 0
        rs.AddPoint((x,y,z))
        pointList.append((x,y,z))
for i in range(len(pointList)):
    centroid = rs.CurveAreaCentroid(curveGUID)[0]
    distance = rs.Distance(pointList[i], attrPt)
    translation = (pointList[i][0] - centroid[0], pointList[i][1] - centroid[1], pointList[i][2] - centroid[2])
    curveGUID = rs.CopyObject(curveGUID, translation)
    rs.RotateObject(curveGUID, pointList[i], distance)