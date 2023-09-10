import rhinoscriptsyntax as rs
import random as rnd

ptList = []
curve = rs.GetObject('select a closed curve', rs.filter.curve)
imax = rs.GetInteger('input number here for the x direction', 10)
jmax = rs.GetInteger('input number here for the y direction', 10)
default = 5


if imax > 10 or imax < 1:
    imax = default
if jmax > 10 or jmax < 1:
    jmax = default


for i in range(imax):
    for j in range(jmax):
        x = i * (5 + rnd.random())
        y = j * (5 + rnd.random())
        z = 0
        ptList.append((x, y, z))

#The pattern to be generated if selected curve is a circle
if rs.IsCircle(curve):
    centre = rs.CircleCenterPoint(curve)
    for i, pt in enumerate(ptList):
        radius = 5 * rnd.random()
        if radius > 10:
            radius = 10
        elif radius < .25:
            radius = .25
        else:
            radius = radius

#            Generate transformation
        transformed_circle = rs.CopyObject(curve, [0, 0, 0])
        scale_factor = radius / 10
        rs.ScaleObject(transformed_circle, centre, [scale_factor, scale_factor, scale_factor])
        rotation_angle = i * 45
        rs.RotateObject(transformed_circle, centre, rotation_angle)
    rs.HideObject(curve)

#The pattern to be generated otherwise
else:
    for i in range(len(ptList)):
        centroid = rs.CurveAreaCentroid(curve)[0]
        scaledCurve = rs.ScaleObject(curve, centroid, (.4, .4, .4), True)
        rs.RotateObject(scaledCurve, centroid, i)
    rs.HideObject(curve)




