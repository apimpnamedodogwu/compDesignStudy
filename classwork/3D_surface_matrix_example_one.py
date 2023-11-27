#3D SURFACE MATRIX EXAMPLE ONE

#import modules
import rhinoscriptsyntax as rs
import random as rnd

def SurfacePoints(STRSRF, INTU, INTV):
    #create empty dictionary
    ptMTX = {}
    srfNorm = {}
    
    #find domain of surface
    Udomain = rs.SurfaceDomain(STRSRF,0)
    Vdomain = rs.SurfaceDomain(STRSRF,1)
    
    #calculate step values
    stepU = (Udomain[1] - Udomain[0])/INTU
    stepV = (Vdomain[1] - Vdomain[0])/INTV
    
    #find list of expanding step values
    expStep = DivideExponentially((Vdomain[1] - Vdomain[0]), INTV)
    # print expStep
    
    #PLOT POINTS ON SURFACE
    for i in range(INTU+1):
        for j in range(INTV+1):
            #define u and v in terms of step values and i and j
            u = Udomain[0] + stepU * i #+(rnd.random())
            #v = Vdomain[0] + stepV * j #+(rnd.random())
            v = expStep[j]
            
            #evaluate surface
            point = rs.EvaluateSurface(STRSRF, u, v)
            #rs.AddPoint(point)
            ptMTX[(i,j)] = point
            
            #find surface normal(vector) at parameter
            vecNorm = rs.SurfaceNormal(STRSRF, (u, v))
            #print vecNorm
            #scale vector using j value
            vecNorm = rs.VectorScale(vecNorm, (1+j*j)/20)
            vecNorm = rs.PointAdd(vecNorm,point)
            srfNorm[(i,j)] = vecNorm
            #rs.AddPoint(vecNorm)
            #rs.AddLine(point, vecNorm)
            
    #call function to generate geometry - sending dictionaries of points
    GenerateGeometry(ptMTX, srfNorm, INTU, INTV) 
                
def GenerateGeometry(ptMTX, srfNorm, INTU, INTV):
    #LOOP TO CREATE GEOMETRY
    for i in range(INTU+1):
        for j in range(INTV+1):
            if i > 0 and j > 0:
                #CREATE BACK CURVE
                crvBack = rs.AddCurve((ptMTX[(i-1,j-1)], ptMTX[(i,j-1)], 
                ptMTX[(i,j)], ptMTX[(i-1,j)], ptMTX[(i-1,j-1)]),1)
                #CREATE FRONT CURVE
                #create construction surface to find grid of points
                srf = rs.AddSrfPt((srfNorm[(i-1,j-1)], srfNorm[(i,j-1)], 
                srfNorm[(i,j)], srfNorm[(i-1,j)]))
                #rebuild surface to create 4 x 4 grid (9 quadrants)
                rs.RebuildSurface(srf, (3,3), (4,4))
                #extract points from grid
                pts = rs.SurfacePoints(srf)
                #call function to reveal order of points
                #numberPoints(pts)
                #delete construction surface
                rs.DeleteObject(srf)
                #generate random integer between 1 and 9 to select quadrant
                quadNum = rnd.randint(1,9)
                #use quadNum to create front rectangle and sweep profile
                if quadNum == 1:
                    crvFront = rs.AddCurve((pts[0],pts[4],pts[5],pts[1],pts[0]),1)
                    profile = rs.AddLine(ptMTX[(i-1,j-1)], pts[0])
                if quadNum == 2:
                    crvFront = rs.AddCurve((pts[1],pts[5],pts[6],pts[2],pts[1]),1)
                    profile = rs.AddLine(ptMTX[(i-1,j-1)], pts[1])
                if quadNum == 3:
                    crvFront = rs.AddCurve((pts[2],pts[6],pts[7],pts[3],pts[2]),1)
                    profile = rs.AddLine(ptMTX[(i-1,j-1)], pts[2])
                if quadNum == 4:
                    crvFront = rs.AddCurve((pts[4],pts[8],pts[9],pts[5],pts[4]),1)
                    profile = rs.AddLine(ptMTX[(i-1,j-1)], pts[4])
                if quadNum == 5:
                    crvFront = rs.AddCurve((pts[5],pts[9],pts[10],pts[6],pts[5]),1)
                    profile = rs.AddLine(ptMTX[(i-1,j-1)], pts[5])
                if quadNum == 6:
                    crvFront = rs.AddCurve((pts[6],pts[10],pts[11],pts[7],pts[6]),1)
                    profile = rs.AddLine(ptMTX[(i-1,j-1)], pts[6])
                if quadNum == 7:
                    crvFront = rs.AddCurve((pts[8],pts[12],pts[13],pts[9],pts[8]),1)
                    profile = rs.AddLine(ptMTX[(i-1,j-1)], pts[8])
                if quadNum == 8:
                    crvFront = rs.AddCurve((pts[9],pts[13],pts[14],pts[10],pts[9]),1)
                    profile = rs.AddLine(ptMTX[(i-1,j-1)], pts[9])
                if quadNum == 9:
                    crvFront = rs.AddCurve((pts[10],pts[14],pts[15],pts[11],pts[10]),1)
                    profile = rs.AddLine(ptMTX[(i-1,j-1)], pts[10])
                    
                #translate curve variables into lists for use in rs.AddSweep2() function
                crvs = [crvBack,crvFront]
                profile = [profile]
                #use sweep two rail to create surface geometry
                module = rs.AddSweep2(crvs, profile)
                #delete curves
                rs.DeleteObjects(crvs)
                rs.DeleteObjects(profile)
                #add color to module
                rs.ObjectColor(module,(255/INTV*j, 255-(255/INTV)*j,255/INTV*j))
                mat_index = rs.AddMaterialToObject(module)
                rs.MaterialColor(mat_index, (255/INTV*j, 255-(255/INTV)*j,255/INTV*j))
                
def DivideExponentially(maxLength, Divisions):
    #set-up lists
    point = []
    yVal = []
    
    #create point where x is .72 of Vdomain and y and z are 0 (point[0])
    pt = ([(maxLength*.72), 0, 0])
    #rs.AddPoint(pt)
    point.append(pt)
    
    #create point where x and y are .12 of model curve length and z is 0 (point[1])
    pt = ([(maxLength*.12), (maxLength*.12), 0])
    #rs.AddPoint(pt)
    point.append(pt)
    
    #create point where y is model curve length and x and z are 0 (point[2])
    pt = ([0, maxLength, 0])
    #rs.AddPoint(pt)
    point.append(pt)
    
    #draw a curve between the three points (GRAPHcrvGUID)
    GRAPHcrvGUID = rs.AddCurve(point)
    
    #divide (GRAPHcrvGUID)
    GRAPHpoints = rs.DivideCurve(GRAPHcrvGUID, Divisions, True, True)
    
    #delete curve
    #rs.DeleteObject(GRAPHcrvGUID)
    
    #collect y values in a list
    for i in range(len(GRAPHpoints)):
        yVal.append(GRAPHpoints[i][1])
        
    return yVal
                
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