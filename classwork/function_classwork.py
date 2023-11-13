import rhinoscriptsyntax as rs
import random as rnd



def pointMatrix(imax, jmax):
    ptDict = {}
    crveList = []
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
                crveList.append(rs.AddCurve((ptDict[(i,j)], ptDict[(i-1,j-1)], ptDict[(i-1,j)], ptDict[(i,j-1)], ptDict[(i,j)])))
    
    for i in range(len(crveList)):
        midPt = rs.CurveMidPoint(crveList[i])
        rs.ScaleObject(crveList[i],midPt,(.8,.8,.8))
        rs.RotateObject(crveList[i], midPt, i)

def main():
    imax = rs.GetInteger("input a number here for the x direction", 10)
    jmax = rs.GetInteger("input a number here for the y direction", 10)
    pointMatrix(imax, jmax)

main() 
