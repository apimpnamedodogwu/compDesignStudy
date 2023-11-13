#PLANE FROM 3 POINTS
#import modules
import rhinoscriptsyntax as rs

#select points to make a plane
origin = rs.GetPoint('select origin point')
xAxis = rs.GetPoint('select x axis point')
yAxis = rs.GetPoint('select y axis point')

plane = rs.PlaneFromPoints(origin, xAxis, yAxis)

#print out plane data
print plane

#rs.AddPoint(0.894427190999916,-0.447213595499958,0)

print 'origin: ', plane[0]
print 'x axis: ', plane[1]
print 'y axis: ', plane[2]
print 'z axis: ', plane[3]

#create geometry on plane (circle, ellipse, rectangle, arc, cone, cylinder...)
rs.AddRectangle(plane, 4, 3)
rs.AddCircle(plane, 3)
rs.AddCylinder(plane, 5, 2)
