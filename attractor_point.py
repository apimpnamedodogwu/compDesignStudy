import rhinoscriptsyntax as rs
ptList = []
attrPt = rs.GetObject('select an attractor point', rs.filter.point)
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
#create transformation in geometry
#measure distance between attractor point and current point of the list
    distance = rs.Distance(ptList[i], attrPt)
    print distance
#create circle using distance value as radius
    rs.AddCircle(ptList[i], distance/20)