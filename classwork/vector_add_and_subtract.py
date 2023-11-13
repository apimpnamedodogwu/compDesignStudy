import rhinoscriptsyntax as rs

#input point data
vec01 = rs.GetObject("select vector 01", rs.filter.point)
vec02 = rs.GetObject("select vector 02", rs.filter.point)

#render vector lines in rhinospace
rs.AddLine((0,0,0), vec01)
rs.AddLine((0,0,0), vec02)

#find the angle between two vectors
angle = rs.VectorAngle(vec01,vec02)
print angle

#add vectors
newVec = rs.VectorAdd(vec01,vec02)
print newVec

#subtract vectors
#newVec = rs.VectorSubtract(vec01,vec02)

#render newVec and vector line in rhinospace
rs.AddPoint(newVec)
rs.AddLine((0,0,0), newVec)