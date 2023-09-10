import rhinoscriptsyntax as rs
ptList = []
crvGUID = rs.GetObject('select a closed curve', rs.filter.curve)

for i in range(10):
    for j in range(10):
        #define x in terms of i
        #define y in terms of j
        x = i
        y = j
        z = 0
        rs.AddPoint(x, y, z)
        ptList.append((x, y, z))
#To loop through the point list and print out index number and values
for k in range(len(ptList)):
    print k, ':', ptList[k]
    rs.AddTextDot(k, ptList[k])
centroid = rs.CurveAreaCentroid(crvGUID)[0]
#Copy curve to the current point in the list (ptList[i])
#translation = (ptList[k][0] - centroid[0], ptList[k][1] - centroid[1], ptList[k][2] - centroid[2]) 
#crvGUID =  rs.CopyObject(crvGUID, translation)
#Rotate line using k as an angle multiplier
#crvGUID = rs.RotateObject(crvGUID, ptList[k], k)