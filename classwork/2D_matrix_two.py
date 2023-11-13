import rhinoscriptsyntax as rs
import random as rnd
imax = rs.GetInteger("input a number here for the x direction", 10)
jmax = rs.GetInteger("input a number here for the y direction", 10)
ptDict = {}
crveList = []

for i in range(imax):
    for j in range(jmax):
        x = i + (i * i) #+ (rnd.random()* 3)
        y = j + (j * j) #+ (rnd.random()* 3)
        z = 0
        rs.AddPoint(x,y,z)
        ptDict[(i,j)] = (x,y,z)

#for i in range(5):
#    for j in range(5):
#        print i,j, ':', ptDict[(i,j)]
#        rs.AddTextDot((i,j), ptDict[(i,j)])

#loop through the dictionary to create a geometry
for i in range(imax):
    for j in range(jmax):
#       check that the values are greater than 0 and then make a closed curve
        if i > 0 and j > 0:
            rs.AddCurve((ptDict[(i,j)], ptDict[(i-1,j)], ptDict[(i-1,j-1)], ptDict[(i,j-1)], ptDict[(i,j)],))
#       make and L-shaped curve next
#            crveList.append(rs.AddCurve((ptDict[(i,j)],ptDict[(i-1,j)],ptDict[(i-1,j-1)],), 1))

#for i in range(len(crveList)):
#    midPt = rs.CurveMidPoint(crveList[i])
#    rs.RotateObject(crveList[i], midPt, i)
