import rhinoscriptsyntax as rs

def midPt(pt01, pt02):
#   clear all data being held in point variable
    point = None
    point = [(pt01[0] + pt02[0])/2, (pt01[1] + pt02[1])/2, (pt01[2] + pt02[2])/2]
    return point

def point_matrix(imax, jmax, kmax):
    ptDict = {}

    for i in range(imax):
            for j in range(jmax):
                for k in range(kmax):
                    #define x,y,z in terms of i,j,k
                    x = i #+ (i*i)#* 5 #+ (rnd.random()*3)#
                    y = j #* 3 #+ (rnd.random()*5)
                    z = k #+ (k*k)#* 5 #+ (rnd.random()*3)#
                    #save point values in dictionary
                    point = (x,y,z)
                    ptDict[(i,j,k)] = point
                    
        
        #loop through dictionary to create spheres
    for i in range(imax):
            for j in range(jmax):
                for k in range(kmax):
                    if i > 0 and j > 0 and k > 0:
                        ####  CREATE GEOMETRY  ####
                        #CREATE BACK CURVE
                        backCurve = rs.AddCurve((ptDict[(i-1,j,k-1)], ptDict[(i,j,k-1)],
                        ptDict[(i,j,k)], ptDict[(i-1,j,k)], ptDict[(i-1,j,k-1)]),1)
                        centreForBackCurve = rs.CurveMidPoint(backCurve)

                        #find the centre of the indivual frames of the back curve
                        centreA = midPt(ptDict[(i-1,j-1, k-1)], ptDict[(i, j-1, k-1)])
                        rs.AddPoint(centreA)
                        centreB = midPt(ptDict[(i,j-1,k-1)], ptDict[(i, j-1, k)])
                        rs.AddPoint(centreB)
                        centreC = midPt(ptDict[(i,j-1, k)], ptDict[(i-1, j-1, k)])
                        rs.AddPoint(centreC)
                        centreD = midPt(ptDict[(i-1,j-1, k)], ptDict[(i-1, j-1, k-1)])
                        rs.AddPoint(centreD)

                        frontPattern = rs.AddCurve((centreD, centreForBackCurve, centreA,
                                                    centreA, centreForBackCurve, centreB,
                                                    centreB, centreForBackCurve, centreC,
                                                    centreC, centreForBackCurve, centreD))
                        rs.ReverseCurve(frontPattern)

                        




def main():
    
    #get values from user
    imax = rs.GetInteger('maximum number x', 5)
    jmax = rs.GetInteger('maximum number y', 2)
    kmax = rs.GetInteger('maximum number z', 5)
    
    #call function
    # rs.EnableRedraw(False)
    point_matrix(imax,jmax,kmax)
    # rs.EnableRedraw(True)

main()