import rhinoscriptsyntax as rs

#input point data
pt01 = rs.GetObject("select TO point", rs.filter.point)
pt02 = rs.GetObject("select FROM point", rs.filter.point)
pt03 = rs.GetObject("select point to ADD to", rs.filter.point)

#render input vector in rhinospace
rs.AddLine(pt01, pt02)

#create a vector from 2 input points
vector = rs.VectorCreate(pt01, pt02)

#unitize vector (set equal to one unit of measure)
vector = rs.VectorUnitize(vector)
print vector

#determine vector magnitude after unitizing by using rs.VectorScale()
vector = rs.VectorScale(vector, 3)

#render vector point in space
rs.AddPoint(vector)

#render vector line in rhinospace
rs.AddLine((0,0,0),vector)

#add vector to an input point in space
newPt = rs.PointAdd(pt03, vector)
rs.AddPoint(newPt)

#render vector line from input point to newPt
rs.AddLine(pt03,newPt)