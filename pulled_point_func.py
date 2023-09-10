import rhinoscriptsyntax as rs

def pullPt(pt01, pt02, val01, val02):
    #   clear all data being held in point variable
    point = None
#    calculate pulled point 
    point = [(pt01[0] * val01 + pt02[0] * val02) / (val01 + val02), (pt01[1] * val01 + pt02[1] * val02) / (val01 + val02), (pt01[2] * val01 + pt02[2] * val02) / (val01 + val02)]
    return point


def main():
    pt01 = rs.GetPoint("select point one")
    pt02 = rs.GetPoint("select pint two")
    val01 = rs.GetReal("input pull value for point one", 10)
    val02 = rs.GetReal("input pull value for point two", 10)
#    rs.AddPoint(pullPt(pt01, pt02, val01, val02))

#loop to create points with varying pull values
    for i in range(10):
        newPt = rs.AddPoint(pullPt(pt01, pt02, i, val02))
        rs.AddTextDot(i,newPt)

main()