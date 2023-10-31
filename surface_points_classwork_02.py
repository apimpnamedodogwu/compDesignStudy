#2D SURFACES EXAMPLE TWO

#import modules
import rhinoscriptsyntax as rs
import random as rnd

def SurfacePoints(STRSRF, INTU, INTV):
    #create empty dictionary
    ptMTX = {}
    
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
            u = Udomain[0] + stepU * i + (rnd.random()*2)
            v = Vdomain[0] + stepV * j + (rnd.random()*2)
            
            #evaluate surface
            point = rs.EvaluateSurface(STRSRF, u, v)
            #rs.AddPoint(point)
            ptMTX[(i,j)] = point
            
#    #LABEL POINTS ON SURFACE WITH (i,j) KEYS
#    for i in range(INTU+1):
#        for j in range(INTV+1):
#            rs.AddTextDot((i,j),ptMTX[(i,j)])
            
    ####  CREATE GEOMETRY  ####
    for i in range(INTU+1):
        for j in range(INTV+1):
            if i > 0 and j > 0:
                #find mid point to use as centroid
                centroid = MidPt(ptMTX[(i,j)], ptMTX[(i-1,j-1)])
                rs.AddPoint(centroid)
                curves = []
                #create outer curves in a list 
                curves.append(rs.AddCurve((ptMTX[(i,j)], centroid, ptMTX[(i,j-1)])))
                curves.append(rs.AddCurve((ptMTX[(i,j-1)], centroid, ptMTX[(i-1,j-1)])))
                curves.append(rs.AddCurve((ptMTX[(i-1,j-1)], centroid, ptMTX[(i-1,j)])))
                curves.append(rs.AddCurve((ptMTX[(i-1,j)], centroid, ptMTX[(i,j)])))
                #join curves deleting original curves
                outerCrv = rs.JoinCurves(curves, True)
                
                #create inner curve
                innerCrv = rs.AddCurve((ptMTX[(i,j)], ptMTX[(i,j-1)], ptMTX[(i-1,j-1)],
                ptMTX[(i-1,j)], ptMTX[(i,j)]))
                #scale inner curve with centroid
                rs.ScaleObject(innerCrv, centroid, (.4,.4,.4))
                #find start point
                startPt = rs.CurveStartPoint(innerCrv)
                rs.AddPoint(startPt)
                #create profile line
                profile = rs.AddLine(startPt, ptMTX[(i,j-1)])
                
                #put curves in lists
                rails = [outerCrv, innerCrv]
                profile = [profile]
                
                #use 2 rail sweep to create surfaces
                rs.AddSweep2(rails, profile)
                
                
def MidPt(PT01, PT02):
    
    #clear all data being held in point variable
    point = None
    #calculate mid-point position from input point data
    point = [(PT01[0] + PT02[0]) / 2,(PT01[1] + PT02[1]) / 2,
    (PT01[2] + PT02[2]) / 2,]
    #return mid-point to main() function where MidPt() function was called
    return point
    
def main():
    #collect data
    strSRF = rs.GetObject('select surface', rs.filter.surface)
    intU = rs.GetInteger('how many U intervals?', 8)
    intV = rs.GetInteger('how many V intervals?', 8)
    rs.HideObject(strSRF)
    #call function
    rs.EnableRedraw(False)
    SurfacePoints(strSRF, intU, intV)
    rs.EnableRedraw(True)
    
main()