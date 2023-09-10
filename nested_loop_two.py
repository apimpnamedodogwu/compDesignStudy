import rhinoscriptsyntax as rs
ptList = []
curveGUID = rs.GetObject('select a closed planar curve', rs.filter.curve)
for i in range(10):
    for j in range(10):
        x = i
        y = j
        z = 0
        rs.AddPoint((x,y,z))
#        rs.AddTextDot((x,y,z), (x,y,z))
        ptList.append((x,y,z))
for i in range(len(ptList)):
#    print i, ':', ptList[i]
#    rs.AddTextDot(i, ptList[i])
#    print(ptList[i])
    centroid = rs.CurveAreaCentroid(curveGUID)[0]
#copy curve to current point in list (ptList[i])
    translation = (ptList[i][0] - centroid[0], ptList[i][1] - centroid[1], ptList[i][2] - centroid[2])
    curveGUID = rs.CopyObject(curveGUID, translation)
#rotate using i as an angle multiplier
    curveGUID = rs.RotateObject(curveGUID, ptList[i], i/50)
    print i/50

