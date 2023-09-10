import rhinoscriptsyntax as rs

def point_matrix(imax, jmax, kmax):
    ptDict = {}
    ptLst = []
    for i in range(imax):
        for j in range (jmax):
            for k in range(kmax):
                x = i * 5
                y = j * 5
                z = k * 5
                point = (x,y,z)
                ptDict[(i,j,k)] = point
                print (i,j,k), ":", point
                rs.AddPoint(point)
                ptLst.append(point)
#    for i in range(len(ptLst)):
#        rs.AddTextDot(i, ptLst[i])
#        
    for i in range(imax):
        for j in range(jmax):
            for k in range(kmax):
                rs.AddTextDot((i,j,k), ptDict[(i,j,k)])

def main():
    imax = rs.GetInteger("input a number here for the x direction", 5)
    jmax = rs.GetInteger("input a number here for the y direction", 2)
    kmax = rs.GetInteger("input a number here for the z direction", 5)
    point_matrix(imax, jmax, kmax)

main()