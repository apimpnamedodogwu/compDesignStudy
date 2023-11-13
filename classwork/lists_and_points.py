import rhinoscriptsyntax as rs

#Collect the points
#GetObject returns a list
ptGUIDs = rs.GetObjects('Select some points', rs.filter.point)
print ptGUIDs

#Delete a point
#rs.DeleteObject(ptGUIDs[0])

#Label points withntheir list index value
rs.AddTextDot(0, ptGUIDs[0])
rs.AddTextDot(1, ptGUIDs[1])
rs.AddTextDot(2, ptGUIDs[2])
rs.AddTextDot(3, ptGUIDs[3])
rs.AddTextDot(4, ptGUIDs[4])

#Label points with their coordinates
#rs.AddTextDot(rs.PointCoordinates(ptGUIDs[0]), ptGUIDs[0])
#rs.AddTextDot(rs.PointCoordinates(ptGUIDs[1]), ptGUIDs[1])
#rs.AddTextDot(rs.PointCoordinates(ptGUIDs[2]), ptGUIDs[2])
#rs.AddTextDot(rs.PointCoordinates(ptGUIDs[3]), ptGUIDs[3])
#rs.AddTextDot(rs.PointCoordinates(ptGUIDs[4]), ptGUIDs[4])

#Create curves from collected points
#rs.AddLine(ptGUIDs[0], ptGUIDs[3])
#newCrve = rs.AddCurve(ptGUIDs)
newCrveTwo = rs.AddCurve((ptGUIDs[0], ptGUIDs[2], ptGUIDs[4]), 1)
newCrveThree = rs.AddCurve((ptGUIDs[0], ptGUIDs[3], ptGUIDs[4]), 1)

#Create a closed shape
newCrveThree = rs.AddCurve((ptGUIDs[0], ptGUIDs[3], ptGUIDs[4], ptGUIDs[0]), 1)