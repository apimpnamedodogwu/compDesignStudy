#3D POINT MATRIX WALL
#import modules
import rhinoscriptsyntax as rs
import random as rnd
ptList = []
ptDict = {}
centreD = [] 
centreA  = []
centre = [] 
centreB = []
centreC = []
centre = []


def PointMatrix(IMAX,JMAX,KMAX):

    #set up empty list

    
    #loop to generate point values as a product of the loop counter
    #save values in list
    for i in range(IMAX):
        for j in range(JMAX):
            for k in range(KMAX):
                #define x,y,z in terms of i,j,k
                x = i 
                y = j
                z = k 
                #save point values in dictionary
                point = (x,y,z)
                ptDict[(i,j,k)] = point
                #print out dictionary key:value pairs
                # print (i,j,k), ':', point
                #render point in rhinospace
                # rs.AddPoint(point)
    
    for i in range(IMAX):
        for j in range(JMAX):
            for k in range(KMAX):
                 if i > 0 and j > 0 and k > 0:
                    ####  CREATE GEOMETRY  ####
            
                    # Create the back bone structure (framework)
                    curveBack = rs.AddCurve((ptDict[(i-1,j,k-1)], ptDict[(i,j,k-1)],
                                ptDict[(i,j,k)], ptDict[(i-1,j,k)], ptDict[(i-1,j,k-1)]),1)
                    # rs.AddSrfPt((ptDict[(i-1,j,k-1)], ptDict[(i,j,k-1)],
                    #             ptDict[(i,j,k)], ptDict[(i-1,j,k)]))
                    
                    centreForCurveBack = rs.CurveMidPoint(curveBack)
                    pattenrForBack = rs.AddCurve((ptDict[(i-1,j,k-1)], centreForCurveBack, ptDict[(i,j,k-1)], 
                                 centreForCurveBack, ptDict[(i,j,k)], centreForCurveBack, ptDict[(i-1,j,k)], centreForCurveBack, ptDict[(i-1,j,k-1)]))

                    # Create the front bone structure (framework)
                    curveFront = rs.AddCurve((ptDict[((i-1, j-1, k-1))], ptDict[(i, j-1, k-1)], ptDict[(i, j-1, k)], 
                                ptDict[(i-1, j-1, k)], ptDict[(i-1, j-1, k-1)]), 1)
                    centreForCurveFront = rs.CurveMidPoint(curveFront)
                    patternForFront = rs.AddCurve((ptDict[(i-1, j-1, k-1)], centreForCurveFront, ptDict[(i, j-1, k-1)], centreForCurveFront, 
                                 ptDict[(i, j-1, k)], centreForCurveFront, ptDict[(i-1, j-1, k)], centreForCurveFront, ptDict[(i-1, j-1, k-1)]))
                    
                    profile = rs.AddLine(centreForCurveBack, centreForCurveFront)
                    
                    rs.HideObject(curveBack)
                    rs.HideObject(curveFront)
                    rs.HideObject(pattenrForBack)
                    rs.HideObject(patternForFront)
                    rs.HideObject(profile)

                    crvs = [pattenrForBack, patternForFront]
                    profile = [profile]
                    rs.AddSweep2(crvs, profile)
                    
            
    

# def midPt(pt01, pt02):
# #   clear all data being held in point variable
#     point = None
#     point = [(pt01[0] + pt02[0])/2, (pt01[1] + pt02[1])/2, (pt01[2] + pt02[2])/2]
#     return point



def main():
    
    #get values from user
    imax = rs.GetInteger('maximum number x', 5)
    jmax = rs.GetInteger('maximum number y', 2)
    kmax = rs.GetInteger('maximum number z', 5)
    
    #call function
    rs.EnableRedraw(False)
    PointMatrix(imax,jmax,kmax)
    rs.EnableRedraw(True)

main()