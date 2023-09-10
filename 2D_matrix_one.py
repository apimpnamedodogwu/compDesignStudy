import rhinoscriptsyntax as rs
#ptLst = []
ptDict = {}
for i in range(5):
    for j in range(5):
        x = i
        y = j
        z = 0
        rs.AddPoint(x,y,z)
#        ptLst.append((x,y,z))
#       save point values in a dictionary using (i,j) as a key
        ptDict[(i,j)] = (x,y,z)
#for i in range(len(ptLst)):
#    rs.AddTextDot(i, ptLst[i])

for i in range(5):
    for j in range(5):
        print i,j, ':', ptDict[(i,j)]
        rs.AddTextDot((i,j), ptDict[(i,j)])

