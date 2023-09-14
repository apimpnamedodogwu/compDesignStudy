#PLANES ON A CURVE
#import modules
import rhinoscriptsyntax as rs

crvGUID = rs.GetObject('select a curve', rs.filter.curve)

#pts = rs.DivideCurve(crvGUID, 8, True, True)

#find domain of curve
domain = rs.CurveDomain(crvGUID)
print domain

#find plane perpendicular to curve normal at a specific parameter
plane = rs.CurvePerpFrame(crvGUID, 15)
print plane

#create a circle at the plane
#rs.AddCircle(plane, 2)

#find step value for plane location based on interval and curve domain
interval = 8
step = (domain[1] - domain[0])/interval
print step

circles = []
#loop to create planes and circles along curve
for i in range(interval + 1):
    plane = rs.CurvePerpFrame(crvGUID, i*step)
#    rs.AddCircle(plane, 2)
#    rs.AddCircle(plane, 4/(i+1))
    circles.append(rs.AddCircle(plane, 4/(i+1)))
    
#loft circles
rs.AddLoftSrf(circles)