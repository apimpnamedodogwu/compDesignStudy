#3D POINT MATRIX WALL
#import modules
import rhinoscriptsyntax as rs
import random as rnd

def PointMatrix(IMAX,JMAX,KMAX):

    #set up empty list
    ptList = []
    ptDict = {}
    
    #loop to generate point values as a product of the loop counter
    #save values in list
    for i in range(IMAX):
        for j in range(JMAX):
            for k in range(KMAX):
                #define x,y,z in terms of i,j,k
                x = i + (i*i)#* 5 #+ (rnd.random()*3)#
                y = j * 3 #+ (rnd.random()*5)
                z = k + (k*k)#* 5 #+ (rnd.random()*3)#
                #save point values in dictionary
                point = (x,y,z)
                ptDict[(i,j,k)] = point
                #print out dictionary key:value pairs
                #print (i,j,k), ':', point
                #render point in rhinospace
                #rs.AddPoint(point)
        
    #loop through dictionary to create spheres
    for i in range(IMAX):
        for j in range(JMAX):
            for k in range(KMAX):
                if i > 0 and j > 0 and k > 0:
                    ####  CREATE GEOMETRY  ####
                    #CREATE BACK CURVE
                    crvBack = rs.AddCurve((ptDict[(i-1,j,k-1)], ptDict[(i,j,k-1)],
                    ptDict[(i,j,k)], ptDict[(i-1,j,k)], ptDict[(i-1,j,k-1)]),1)
                    #CREATE FRONT CURVE
                    #create construction surface to find grid of points
                    srf = rs.AddSrfPt((ptDict[(i-1,j-1,k-1)], ptDict[(i,j-1,k-1)], 
                    ptDict[(i,j-1,k)], ptDict[(i-1,j-1,k)]))
                    #rebuild surface to create 4 x 4 grid (9 quadrants)
                    rs.RebuildSurface(srf, (3,3), (4,4))
                    #extract points from grid
                    pts = rs.SurfacePoints(srf)
                    #call function to reveal order of points
                    # numberPoints(pts)
                    #delete construction surface
                    rs.DeleteObject(srf)
                    #generate random integer between 1 and 9 to select quadrant
                    quadNum = rnd.randint(1,9)
                    #use quadNum to create front rectangle and sweep profile
                    if quadNum == 1:
                        crvFront = rs.AddCurve((pts[0],pts[4],pts[5],pts[1],pts[0]),1)
                        profile = rs.AddLine(ptDict[(i-1,j,k-1)], pts[0])
                    if quadNum == 2:
                        crvFront = rs.AddCurve((pts[1],pts[5],pts[6],pts[2],pts[1]),1)
                        profile = rs.AddLine(ptDict[(i-1,j,k-1)], pts[1])
                    if quadNum == 3:
                        crvFront = rs.AddCurve((pts[2],pts[6],pts[7],pts[3],pts[2]),1)
                        profile = rs.AddLine(ptDict[(i-1,j,k-1)], pts[2])
                    if quadNum == 4:
                        crvFront = rs.AddCurve((pts[4],pts[8],pts[9],pts[5],pts[4]),1)
                        profile = rs.AddLine(ptDict[(i-1,j,k-1)], pts[4])
                    if quadNum == 5:
                        crvFront = rs.AddCurve((pts[5],pts[9],pts[10],pts[6],pts[5]),1)
                        profile = rs.AddLine(ptDict[(i-1,j,k-1)], pts[5])
                    if quadNum == 6:
                        crvFront = rs.AddCurve((pts[6],pts[10],pts[11],pts[7],pts[6]),1)
                        profile = rs.AddLine(ptDict[(i-1,j,k-1)], pts[6])
                    if quadNum == 7:
                        crvFront = rs.AddCurve((pts[8],pts[12],pts[13],pts[9],pts[8]),1)
                        profile = rs.AddLine(ptDict[(i-1,j,k-1)], pts[8])
                    if quadNum == 8:
                        crvFront = rs.AddCurve((pts[9],pts[13],pts[14],pts[10],pts[9]),1)
                        profile = rs.AddLine(ptDict[(i-1,j,k-1)], pts[9])
                    if quadNum == 9:
                        crvFront = rs.AddCurve((pts[10],pts[14],pts[15],pts[11],pts[10]),1)
                        profile = rs.AddLine(ptDict[(i-1,j,k-1)], pts[10])
                        
                    #translate curve variables into lists for use in rs.AddSweep2() function
                    crvs = [crvBack,crvFront]
                    profile = [profile]
                    #use sweep two rail to create surface geometry
                    rs.AddSweep2(crvs, profile)
                    
def numberPoints(points):
    for i in range(len(points)):
        #rs.AddPoint(points[i])
        rs.AddTextDot(i, points[i])
            
def main():
    
    #get values from user
    imax = rs.GetInteger('maximum number x', 5)
    jmax = rs.GetInteger('maximum number y', 2)
    kmax = rs.GetInteger('maximum number z', 5)
    
    #call function
    #rs.EnableRedraw(False)
    PointMatrix(imax,jmax,kmax)
    #rs.EnableRedraw(True)
    
#call main() function to start program
main()

