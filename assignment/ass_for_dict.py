import rhinoscriptsyntax as rs
import random as rnd
imax = rs.GetInteger("input a number here for the x direction", 10)
jmax = rs.GetInteger("input a number here for the y direction", 10)
ptDict = {}


for i in range(imax):
    for j in range(jmax):
        x = i * 5 
        y = j * 5 
        z = 0
#        rs.AddPoint(x,y,z)
        ptDict[(i,j)] = (x,y,z)

for i in range(imax):
    for j in range(jmax):
        if i > 0 and j > 0:
            diagonal = rs.AddLine(ptDict[(i-1,j-1)], ptDict[(i, j)])
            centre = rs.CurveMidPoint(diagonal)
            
            constLineA = rs.AddLine(ptDict[(i-1,j-1)], ptDict[(i, j-1)])
            centreA = rs.CurveMidPoint(constLineA)
            rs.DeleteObject(constLineA)

            
            constLineB = rs.AddLine(ptDict[(i,j-1)], ptDict[(i, j)])
            centreB = rs.CurveMidPoint(constLineB)
            rs.DeleteObject(constLineB)
            
            constLineC = rs.AddLine(ptDict[(i,j)], ptDict[(i-1, j)])
            centreC = rs.CurveMidPoint(constLineC)
            rs.DeleteObject(constLineC)
            
            constLineD = rs.AddLine(ptDict[(i-1,j)], ptDict[(i-1, j-1)])
            centreD = rs.CurveMidPoint(constLineD)
            rs.DeleteObject(constLineD)
            
            rs.AddCurve((ptDict[(i-1,j-1)], centre, centreA))
            rs.AddCurve((ptDict[(i-1,j-1)], centre, centreD))
            rs.AddCurve((ptDict[(i-1,j-1)], centre, centreB))
            rs.AddCurve((ptDict[(i-1,j-1)], centre, centreC))            