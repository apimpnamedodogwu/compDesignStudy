#3D SURFACE MATRIX ATTRACTOR VECTOR

#import modules
import rhinoscriptsyntax as rs

def SurfacePoints(STRSRF, INTU, INTV, ATTRPTS):
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
            rs.AddPoint(point)
            ptMTX[(i,j)] = point
            
            #loop through attractor points to measure distances and
            #find index number of closest attractor point to the matrix point
            distance = []
            #loop through attractor points
            for n in range(len(ATTRPTS)):
                #find distance between attractor point and matrix point
                #save in a list
                distance.append(rs.Distance(point, ATTRPTS[n]))
            #sort list values from lowest to highest -- value in index slot [0]
            #will be the closest attractor point
            distance.sort()
            #loop through attractor points
            for n in range(len(ATTRPTS)):
                #if the distance value is equal to the one held in index [0]
                #then that attractor point, held in index slot [n] is the
                #closest one. Save it in variable attractorPt
                if rs.Distance(point, ATTRPTS[n]) == distance[0]:
                    #print n
                    attractorPt = ATTRPTS[n]
            
            #create vector from attractor point and matrix point
            vector = rs.VectorCreate(attractorPt, point)
            # vector = rs.SurfaceNormal(STRSRF, (u, v))

#            rs.AddPoint(vector)
#            rs.AddLine((0,0,0), vector)
            #find the length of the vector
            VecLength = rs.VectorLength(vector)
            #scale the vector
            vector = rs.VectorScale(vector, 3/VecLength)
            #add the vector to the point matrix point 
            vector = rs.PointAdd(vector,point)
            #draw a line to represent the vector
            rs.AddLine(point, vector)
            #save vector point in dictionary 
            srfNorm[(i,j)] = vector
            
                
    #LOOP TO CREATE GEOMETRY
    for i in range(INTU+1):
        for j in range(INTV+1):
            if i > 0 and j > 0:
                #create bottom curve
                crvBot = rs.AddCurve((ptMTX[(i,j)], ptMTX[(i-1,j)], 
                ptMTX[(i-1,j-1)], ptMTX[(i, j-1)], ptMTX[(i-1, j)], ptMTX[(i,j)]))
                #create top curve
                crvTop = rs.AddCurve((srfNorm[(i,j)], srfNorm[(i-1,j)],
                srfNorm[(i-1,j-1)], srfNorm[(i, j-1)], srfNorm[(i-1, j)], srfNorm[(i,j)]))
                #generate loft
                rs.AddLoftSrf((crvBot, crvTop))
                
def main():
    #collect data
    strSRF = rs.GetObject('select surface', rs.filter.surface)
    #attrPT = rs.GetPoint('select attractor point')
    attrPTs = rs.GetObjects('select attractor points', rs.filter.point)
    intU = rs.GetInteger('how many U intervals?', 8)
    intV = rs.GetInteger('how many V intervals?', 8)
    rs.HideObject(strSRF)
    #call function
    rs.EnableRedraw(False)
    SurfacePoints(strSRF, intU, intV, attrPTs)
    rs.EnableRedraw(True)
    
main()