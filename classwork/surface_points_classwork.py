#SURFACE POINTS

#import modules
import rhinoscriptsyntax as rs

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
            u = Udomain[0] + stepU * i
            v = Vdomain[0] + stepV * j
            
            #evaluate surface
            point = rs.EvaluateSurface(STRSRF, u, v)
            rs.AddPoint(point)
            ptMTX[(i,j)] = point
            
    #LABEL POINTS ON SURFACE WITH (i,j) KEYS
    for i in range(INTU+1):
        for j in range(INTV+1):
            rs.AddTextDot((i,j),ptMTX[(i,j)])

def main():
    #collect data
    strSRF = rs.GetObject('select surface', rs.filter.surface)
    intU = rs.GetInteger('how many U intervals?', 8)
    intV = rs.GetInteger('how many V intervals?', 8)
    #rs.HideObject(strSRF)
    #call function
    SurfacePoints(strSRF, intU, intV)
    
main()