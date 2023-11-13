import rhinoscriptsyntax as rs
import random as rnd


def midPt(pt01, pt02):
#   clear all data being held in point variable
    point = None
    point = [(pt01[0] + pt02[0])/2, (pt01[1] + pt02[1])/2, (pt01[2] + pt02[2])/2]
    return point

def pointMatrix(imax, jmax):
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
                print centre
                
    #           Find the mid points of the bone structure 
                centreA = midPt(ptDict[(i-1,j-1)], ptDict[(i, j-1)])
                centreB = midPt(ptDict[(i,j-1)], ptDict[(i, j)])
                centreC = midPt(ptDict[(i,j)], ptDict[(i-1, j)])
                centreD = midPt(ptDict[(i-1,j)], ptDict[(i-1, j-1)])

    #           Create the pattern
                rs.AddCurve((ptDict[(i-1,j-1)], centre, centreA))
                rs.AddCurve((ptDict[(i-1,j-1)], centre, centreD))
                rs.AddCurve((ptDict[(i-1,j-1)], centre, centreB))
                rs.AddCurve((ptDict[(i-1,j-1)], centre, centreC))  

    #           Mirror the pattern
                rs.AddCurve((ptDict[(i,j)], centre, centreC))
                rs.AddCurve((ptDict[(i,j)], centre, centreB))
                rs.AddCurve((ptDict[(i,j)], centre, centreD))
                rs.AddCurve((ptDict[(i,j)], centre, centreA)) 
            

def main():
    imax = rs.GetInteger("input a number here for the x direction", 10)
    jmax = rs.GetInteger("input a number here for the y direction", 10) 
    pointMatrix(imax, jmax)
    #rs.AddPoint(midPt(pt01, pt02))

main()