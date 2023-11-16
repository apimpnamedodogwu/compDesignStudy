#3D SURFACE MATRIX ATTRACTOR PINCH

#import modules
import rhinoscriptsyntax as rs

def SurfacePoints(STRSRF, INTU, INTV, ATTRPT):
    #create empty dictionary
    ptMTX = {}
    srfNorm = {}
    
    #find domain of surface
    Udomain = rs.SurfaceDomain(STRSRF,0)
    Vdomain = rs.SurfaceDomain(STRSRF,1)
    
    #calculate step values
    stepU = (Udomain[1] - Udomain[0])/INTU
    stepV = (Vdomain[1] - Vdomain[0])/INTV
    
    #PLOT POINTS ON SURFACE
    for i in range(INTU+1):
        for j in range(INTV+1):
            #define u and v in terms of step values and i and j
            u = Udomain[0] + stepU * i
            v = Vdomain[0] + stepV * j
            
            #evaluate surface
            point = rs.EvaluateSurface(STRSRF, u, v)
            #rs.AddPoint(point)
            ptMTX[(i,j)] = point
            
            #CALCULATE NEW POINT POSITIONS USING DISTANCE AND PULLED POINT FUNCTION
            #measure distance between attractor point and point in matrix
            distance = rs.Distance(ATTRPT, point)
            if i == 0 or i == INTU:
                ptMTX[(i,j)] = ptMTX[(i,j)]
            elif j == 0 or j == INTV:
                ptMTX[(i,j)] = ptMTX[(i,j)]
            else:
                ptMTX[(i,j)] = PullPt(ATTRPT, ptMTX[(i,j)], 1, distance/8)
            #replace the matrix point with the closest point on the surface.
            closestPt = rs.BrepClosestPoint(STRSRF, ptMTX[(i,j)])
            ptMTX[(i,j)] = closestPt[0]
            #render new points in rhinospace
            rs.AddPoint(ptMTX[(i,j)])
            
            #find surface normal(vector) at parameter
            vecNorm = rs.SurfaceNormal(STRSRF, closestPt[1])
            #print vecNorm
            vecNorm = rs.PointAdd(vecNorm,ptMTX[(i,j)])
            srfNorm[(i,j)] = vecNorm
            rs.AddPoint(vecNorm)
            rs.AddLine(ptMTX[(i,j)], vecNorm)
                
    #LOOP TO CREATE GEOMETRY
    for i in range(INTU+1):
        for j in range(INTV+1):
            if i > 0 and j > 0:
                #create bottom curve
                crvBot = rs.AddCurve((ptMTX[(i,j)], ptMTX[(i-1,j)], 
                ptMTX[(i-1,j-1)], ptMTX[(i,j-1)], ptMTX[(i,j)]))
                #create top curve
                crvTop = rs.AddCurve((srfNorm[(i,j)], srfNorm[(i-1,j)],
                srfNorm[(i-1,j-1)], srfNorm[(i,j-1)], srfNorm[(i,j)]))
                #generate loft
                rs.AddLoftSrf((crvBot, crvTop))
                
def PullPt(PT01,PT02,VAL01,VAL02):
    #clear all data being held in point variable
    point = None
    #calculate pulled point
    point = [(PT01[0]*VAL01 + PT02[0]*VAL02) / (VAL01 + VAL02),
    (PT01[1]*VAL01 + PT02[1]*VAL02) / (VAL01 + VAL02),
    (PT01[2]*VAL01 + PT02[2]*VAL02) / (VAL01 + VAL02)]
    #return pulled point
    return point
                
def main():
    #collect data
    strSRF = rs.GetObject('select surface', rs.filter.surface)
    attrPT = rs.GetPoint('select attractor point')
    intU = rs.GetInteger('how many U intervals?', 8)
    intV = rs.GetInteger('how many V intervals?', 8)
    rs.HideObject(strSRF)
    #call function
    rs.EnableRedraw(False)
    SurfacePoints(strSRF, intU, intV, attrPT)
    rs.EnableRedraw(True)
    
main()