import rhinoscriptsyntax as rs

def midPt(pt01, pt02):
#   clear all data being held in point variable
    point = None
    point = [(pt01[0] + pt02[0])/2, (pt01[1] + pt02[1])/2, (pt01[2] + pt02[2])/2]
    return point

def main():
    pt01 = rs.GetPoint("select point one")
    pt02 = rs.GetPoint("select point two")  
    print midPt(pt01, pt02)
    rs.AddPoint(midPt(pt01, pt02))

main()