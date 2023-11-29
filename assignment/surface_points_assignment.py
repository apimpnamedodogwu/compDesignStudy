import rhinoscriptsyntax as rs
import random as rnd

def surface_points(surface, intU, intV):
    ptMTX = {}

    uDomain = rs.SurfaceDomain(surface, 0)
    vDomain = rs.SurfaceDomain(surface, 1)


    stepU = (uDomain[1] - uDomain[0]) / intU
    stepV = (vDomain[1] - vDomain[0]) / intV

    for i in range (intU + 1):
        for j in range (intV + 1):
             u = uDomain[0] + stepU * i
             v = vDomain[0] + stepV * j

             point = rs.EvaluateSurface(surface, u, v)  
             ptMTX[(i, j)] = point              
    

    for i in range (intU + 1):
        for j in range (intV + 1):
            if i > 0 and j > 0:
                centroid = midPt(ptMTX[(i, j)], ptMTX[(i-1, j-1)])
                # rs.AddPoint(centroid)

                centreA = midPt(ptMTX[(i-1,j-1)], ptMTX[(i, j-1)])
                centreB = midPt(ptMTX[(i,j-1)], ptMTX[(i, j)])
                centreC = midPt(ptMTX[(i,j)], ptMTX[(i-1, j)]) 
                centreD = midPt(ptMTX[(i-1,j)], ptMTX[(i-1, j-1)])

                curves = []
                curves.append(rs.AddCurve((ptMTX[(i-1, j-1)], centroid, centreA)))
                curves.append(rs.AddCurve((centreA, centroid, ptMTX[(i, j-1)])))
                curves.append(rs.AddCurve(( ptMTX[(i, j-1)], centroid, centreB)))
                curves.append(rs.AddCurve(( centreB, centroid, ptMTX[(i, j)])))
                curves.append(rs.AddCurve(( ptMTX[(i, j)], centroid, centreC)))
                curves.append(rs.AddCurve(( centreC, centroid, ptMTX[(i-1, j)])))
                curves.append(rs.AddCurve(( ptMTX[(i-1, j)], centroid, centreD)))
                curves.append(rs.AddCurve(( centreD, centroid, ptMTX[(i-1, j-1)])))
                
                

                outerCurve = rs.JoinCurves(curves, True)

                #create inner curve
                innerCrv = rs.AddCurve((ptMTX[(i-1,j-1)], ptMTX[(i,j-1)], ptMTX[(i,j)],
                ptMTX[(i-1,j)], ptMTX[(i-1,j-1)]))
                #scale inner curve with centroid
                rs.ScaleObject(innerCrv, centroid, (.4,.4,.4))

                rs.ReverseCurve(outerCurve)
                rs.ReverseCurve(innerCrv)
                #find start point
                startPt = rs.CurveStartPoint(innerCrv)
                # rs.AddPoint(startPt)
                #create profile line
                profile = rs.AddLine(startPt, ptMTX[(i,j-1)])
                
                #put curves in lists
                rails = [outerCurve, innerCrv]
                profile = [profile]
                
                #use 2 rail sweep to create surfaces
                rs.AddSweep2(rails, profile)
                
                


def midPt(pt01, pt02):
#   clear all data being held in point variable
    point = None
    point = [(pt01[0] + pt02[0])/2, (pt01[1] + pt02[1])/2, (pt01[2] + pt02[2])/2]
    return point


def main():
    surface = rs.GetObject("Select a surface", rs.filter.surface)
    intU = rs.GetInteger("How many U (X) intervals?", 8)
    intV = rs.GetInteger("How many V (Y) intervals?", 8)
    rs.HideObject(surface)

    rs.EnableRedraw(False)
    surface_points(surface, intU, intV)
    rs.EnableRedraw(True)

main()