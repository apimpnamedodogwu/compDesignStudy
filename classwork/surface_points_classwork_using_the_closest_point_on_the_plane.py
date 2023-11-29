#2D SURFACES EXAMPLE THREE

#import modules
import rhinoscriptsyntax as rs
import random as rnd

def SurfacePoints(STRSRF, INTU, INTV):
    #create empty dictionary
    ptMTX = {}
    planePt = {}
    
    #find domain of surface
    Udomain = rs.SurfaceDomain(STRSRF,0)
    Vdomain = rs.SurfaceDomain(STRSRF,1)
    #print domain values
    print 'Udomain: ', Udomain
    print 'Vdomain: ', Vdomain
    
    #calculate step values
    stepU = (Udomain[1] - Udomain[0])/INTU
    stepV = (Vdomain[1] - Vdomain[0])/INTV
    #print step values
    print 'stepU: ', stepU
    print 'stepV: ', stepV
    
    #PLOT POINTS ON SURFACE
    for i in range(INTU+1):
        for j in range(INTV+1):
            #define u and v in terms of step values and i and j
            u = Udomain[0] + stepU * i #+ (rnd.random()*2)
            v = Vdomain[0] + stepV * j #+ (rnd.random()*2)
            
            #evaluate surface
            point = rs.EvaluateSurface(STRSRF, u, v)
            #rs.AddPoint(point)
            ptMTX[(i,j)] = point
            
    #FIND PLANAR POINT 
    for i in range(INTU+1):
        for j in range(INTV+1):
            if i > 0 and j > 0:
                #find a plane from 3 matrix points
                # origin, x-axis, and y-axis
                plane = rs.PlaneFromPoints(ptMTX[(i-1,j-1)], ptMTX[(i,j-1)],
                ptMTX[(i-1,j)])
                #find the closest point on the plane using the 4th matrix point
                point = rs.PlaneClosestPoint(plane, ptMTX[(i,j)])
                #render point in rhinospace
                rs.AddPoint(point)
                #save planar point in a dictionary
                planePt[(i,j)] = point
            
    ####  CREATE GEOMETRY  ####
    for i in range(INTU+1):
        for j in range(INTV+1):
            if i > 0 and j > 0:
                #create 4 point surfaces
                rs.AddSrfPt((planePt[(i,j)], ptMTX[(i-1,j)], ptMTX[(i-1,j-1)],
                ptMTX[(i,j-1)]))
                #create infill triangles
                rs.AddSrfPt((ptMTX[(i,j)], planePt[(i,j)], ptMTX[(i,j-1)]))
                rs.AddSrfPt((ptMTX[(i,j)], ptMTX[(i-1,j)], planePt[(i,j)]))
                
                
def main():
    #collect data
    #strSRF = rs.GetObject('select surface', rs.filter.surface)
    strSRFs = rs.GetObjects('select surfaces', rs.filter.surface)
    intU = rs.GetInteger('how many U intervals?', 8)
    intV = rs.GetInteger('how many V intervals?', 8)
    #rs.HideObject(strSRF)
    #call function
    #rs.EnableRedraw(False)
    #SurfacePoints(strSRF, intU, intV)
    #rs.EnableRedraw(True)
    
    #call function with multiple surfaces
    rs.EnableRedraw(False)
    for strSRF in strSRFs:
        rs.HideObject(strSRF)
        #call function
        SurfacePoints(strSRF, intU, intV)
    rs.EnableRedraw(True)
    
main()