import rhinoscriptsyntax as rs
import random as rnd
ptList = []

# input values for imax and jmax
imax = rs.GetInteger('input number in x direction', 10)
jmax = rs.GetInteger('input number in y direction', 10)


for i in range(imax):
    for j in range(jmax):
        x = i * 5
        y = j * 5
        z = 0
        rs.AddPoint((x,y,z))
        ptList.append((x,y,z))
#       create random index selection
#rndIndex = rnd.randint(0,99)
#rndIndex = rnd.randint(0,imax * jmax - 1)


#for i in range(len(ptList)):
##    create geometry transformation
#    if ptList[i] != ptList[rndIndex]:
#        rs.AddLine(ptList[rndIndex], ptList[i])


for i in range(len(ptList)):
    for j in range(len(ptList)):
##        create geometry
        if ptList[i] != ptList[j]:
            rs.AddLine(ptList[i], ptList[j])