#3D POINT MATRIX CIRCLES
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
                x = i * 5 + (rnd.random()*5)
                y = j * 5 + (rnd.random()*5)
                z = k * 5 + (rnd.random()*5)
                #save point values in dictionary
                point = (x,y,z)
                ptDict[(i,j,k)] = point
                #print out dictionary key:value pairs
                #print (i,j,k), ':', point
                #render point in rhinospace
                rs.AddPoint(point)
        
    #loop through dictionary to create spheres
    for i in range(IMAX):
        for j in range(JMAX):
            for k in range(KMAX):
                if i > 0 and j > 0 and k > 0:
                    ####  CREATE GEOMETRY  ####
                    #CREATE BACK CIRCLE
                    origin = MidPt(ptDict[(i,j,k)], ptDict[(i-1,j,k-1)])
                    plane = rs.PlaneFromPoints(origin, ptDict[(i,j,k-1)],
                    ptDict[(i,j,k)])
                    radius = randomRadius(5)
                    circBack = rs.AddCircle(plane, radius)
                    
                    #CREATE FRONT CIRCLE
                    origin = MidPt(ptDict[(i-1,j-1,k-1)], ptDict[(i,j-1,k)])
                    plane = rs.PlaneFromPoints(origin, ptDict[(i,j-1,k-1)],
                    ptDict[(i,j-1,k)])
                    radius = randomRadius(8)
                    circFront = rs.AddCircle(plane, radius)
                    
                    #LOFT CIRCLES
                    cone = rs.AddLoftSrf((circBack, circFront))
                    rs.ObjectColor(cone, (255/IMAX*i, 255-(255/JMAX)*j,255/KMAX*k))
                    
def randomRadius(maxRadius):
    #clear variable
    radius = None
    #generate random integer within a range - use as radius
    radius = maxRadius*rnd.random()
    #limit radius values using a conditional statement
    if radius > maxRadius-1:
        radius = maxRadius-1
    elif radius < .5:
        radius = .5
    else:
        radius = radius
    #return the radius value
    return radius
                    
def MidPt(PT01, PT02):
    
    #clear all data being held in point variable
    point = None
    #calculate mid-point position from input point data
    point = [(PT01[0] + PT02[0]) / 2,(PT01[1] + PT02[1]) / 2,
    (PT01[2] + PT02[2]) / 2,]
    #return mid-point to main() function where MidPt() function was called
    return point
            
def main():
    
    #get values from user
    imax = rs.GetInteger('maximum number x', 5)
    jmax = rs.GetInteger('maximum number y', 2)
    kmax = rs.GetInteger('maximum number z', 5)
    
    #call function
    rs.EnableRedraw(False)
    PointMatrix(imax,jmax,kmax)
    rs.EnableRedraw(True)
    
#call main() function to start program
main()

