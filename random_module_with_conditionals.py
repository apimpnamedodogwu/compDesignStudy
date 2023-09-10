import rhinoscriptsyntax as rs
import random as rnd
ptList = []
# input values for imax and jmax
imax = rs.GetInteger('input number in x direction', 10)
jmax = rs.GetInteger('input number in y direction', 10)
for i in range(imax):
    for j in range(jmax):
        print rnd.random()
        x = i * 5 + rnd.random()
        y = j * 5 + rnd.random()
        z = 0
        rs.AddPoint((x,y,z))
        ptList.append((x,y,z))
for i in range(len(ptList)):
#    create geometry transformation
#generate random integer and use as radius
    radius = 5 * rnd.random()
#    radius = rnd.randint(1,5)
#limit radius values using conditional statement
    if radius > 4:
        radius = 4
    elif radius < .25:
        radius = .25
    else:
        radius = radius
    rs.AddCircle(ptList[i], 2)