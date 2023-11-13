import rhinoscriptsyntax as rs
import random as rnd



def point_matrix(imax, jmax, kmax):
    ptDict = {}
    ptLst = []
    for i in range(imax):
        for j in range (jmax):
            for k in range(kmax):
                x = i * 5 + (rnd.random() * 5)
                y = j * 5
                z = k * 5 + (rnd.random() * 5)
                point = (x,y,z)
                ptDict[(i,j,k)] = point
                ptLst.append(point)
    #loop through the dictionary to create spheres
    for i in range(imax):
        for j in range(jmax):
            for k in range(kmax):
    #create the geometry
                if i > 0 and j > 0 and k > 0:
    #create back curve
#                    crvBack = rs.AddCurve((ptDict[(i, j, k)], ptDict[(i-1, j, k)], ptDict[(i-1, j, k-1)], ptDict[(i, j, k-1)], ptDict[(i, j, k)]))
                    crvBack = rs.AddSrfPt((ptDict[(i,j,k)], ptDict[(i-1,j,k)], ptDict[(i-1,j-1,k-1)]))
    #create front curve
#                    crvFront = rs.AddCurve((ptDict[(i, j-1, k)], ptDict[(i-1, j-1, k)], ptDict[(i-1, j-1, k-1)], ptDict[(i, j-1, k-1)], ptDict[(i, j-1, k)]))
                    crvFront = rs.AddSrfPt((ptDict[(i, j, k-1)], ptDict[(i-1, j, k-1)], ptDict[(i, j-1, k-1)]))
                    
    #scale front curve with found mid point
#                    origin = midPt(ptDict[(i-1, j-1, k-1)], ptDict[(i, j-1, k)])
#                    scaleFact = rnd.random()
#                    crvFront = rs.ScaleObject(crvFront, origin, (scaleFact, scaleFact, scaleFact))
    #loft curves to create cones
#                    rs.AddLoftSrf((crvBack, crvFront))
                    

#                radius = randomRadius()
#                sphere = rs.AddSphere(ptDict[(i,j,k)], radius)
#                rs.ObjectColor(sphere, (255/imax * i, 255-(255/jmax * j), 255/kmax * k))

def midPt(pt01, pt02):
    #clear all data being held in point variable
    point = None
    point = [(pt01[0] + pt02[0])/2, (pt01[1] + pt02[1])/2, (pt01[2] + pt02[2])/2]
    return point

#def randomRadius():
#    #clear variable
#    radius = None
#    #generate random integer within a range and use as radius
#    radius = 5 * rnd.random()
#    #limit the values of the radius
#    if radius > 5:
#        radius = 5
#    elif radius < .5:
#        radius = .5
#    else:
#        radius = radius
#    return radius


def main():
    imax = rs.GetInteger("Maximu number for the x direction", 5)
    jmax = rs.GetInteger("Maximum number for the y direction", 2)
    kmax = rs.GetInteger("Maximum number for the z direction", 5)

    rs.EnableRedraw(False)
    point_matrix(imax, jmax, kmax)
    rs.EnableRedraw(True)


main()