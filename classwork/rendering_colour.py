#RENDERING COLOR

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
                x = i * 5
                y = j * 5
                z = k * 10 + (rnd.random()*10)
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
                ####  CREATE GEOMETRY  ####
                radius = randomRadius()
                sphere = rs.AddSphere(ptDict[(i,j,k)], radius)
                rs.ObjectColor(sphere, (255/IMAX*i, 255-(255/JMAX)*j,255/KMAX*k))
                mat_index = rs.AddMaterialToObject(sphere)
                rs.MaterialColor(mat_index, (255/IMAX*i, 255-(255/JMAX)*j,255/KMAX*k))
                
                
def randomRadius():
    #clear variable
    radius = None
    #generate random integer within a range - use as radius
    radius = 5*rnd.random()
    #limit radius values using a conditional statement
    if radius > 4:
        radius = 4
    elif radius < .5:
        radius = .5
    else:
        radius = radius
    #return the radius value
    return radius
            
def main():
    
    #get values from user
    imax = rs.GetInteger('maximum number x', 5)
    jmax = rs.GetInteger('maximum number y', 5)
    kmax = rs.GetInteger('maximum number z', 5)
    
    #attrPt = rs.GetPoint('select attractor point')
    
    #call function
    rs.EnableRedraw(False)
    PointMatrix(imax,jmax,kmax)
    rs.EnableRedraw(True)
    
#call main() function to start program
main()

