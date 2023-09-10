import rhinoscriptsyntax as rs
import random as rnd



def point_matrix(imax, jmax, kmax, attrPt):
    ptDict = {}
    ptLst = []
    for i in range(imax):
        for j in range (jmax):
            for k in range(kmax):
                x = i * 5
                y = j * 5
                z = k * 10
                point = (x,y,z)
                ptDict[(i,j,k)] = point
                ptLst.append(point)
    #loop through the dictionary to create spheres
    for i in range(imax):
        for j in range(jmax):
            for k in range(kmax):
    #create the geometry
    #            radius = randomRadius()
                distance = rs.Distance(ptDict[(i,j,k)], attrPt)
                sphere = rs.AddSphere(ptDict[(i,j,k)], distance/2)
                rs.ObjectColor(sphere, (255/imax * i, 255-(255/jmax * j), 255/kmax * k))

def randomRadius():
    #clear variable
    radius = None
    #generate random integer within a range and use as radius
    radius = 5 * rnd.random()
    #limit the values of the radius
    if radius > 5:
        radius = 5
    elif radius < .5:
        radius = .5
    else:
        radius = radius
    return radius


def main():
    imax = rs.GetInteger("Maximu number for the x direction", 5)
    jmax = rs.GetInteger("Maximum number for the y direction", 5)
    kmax = rs.GetInteger("Maximum number for the z direction", 5)
    attrPt = rs.GetObject('select an attractor point', rs.filter.point)
    
    rs.EnableRedraw(False)
    point_matrix(imax, jmax, kmax, attrPt)
    rs.EnableRedraw(True)


main()