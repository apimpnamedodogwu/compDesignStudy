import rhinoscriptsyntax as rs
ptList = [] 
line = rs.GetObject('select a curve to transform', rs.filter.curve)

for i in range(10):
    x = i * 5
    y = 0
    z = 0
    
    rs.AddPoint(x, y, z)
    rs.AddTextDot((x, y, z), (x, y, z))
    ptList.append((x, y, z))
    
for i in range(len(ptList)):
    print i, ':', ptList[i]
    rs.AddTextDot(i, ptList[i])
    
#find midpoint of line
    midPt = rs.CurveMidPoint(line)
#copy line to current point in list (ptList[i])
#translation = ptList[i] - midPt
    translation = (ptList[i][0] - midPt[0], ptList[i][1] - midPt[1], ptList[i][2] - midPt[2])
    line = rs.CopyObject(line, translation)
#rotate line using i as an angle multiplier
    line = rs.RotateObject(line, ptList[i], i)