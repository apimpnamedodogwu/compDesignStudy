import rhinoscriptsyntax as rs

#Collect curves
crves = rs.GetObjects('select curves', rs.filter.curve)
#print crves

#Identify index number of curves and label them
midPts = []
midPts.append(rs.CurveMidPoint(crves[0]))
midPts.append(rs.CurveMidPoint(crves[1]))
midPts.append(rs.CurveMidPoint(crves[2]))

rs.AddTextDot(0, midPts[0])
rs.AddTextDot(1, midPts[1])
rs.AddTextDot(2, midPts[2])

#Generate points from curves using DivideCurve
pts = rs.DivideCurve(crves[0], 5, True, True)
#print pts

#Label points withntheir list index value
rs.AddTextDot(0, pts[0])
rs.AddTextDot(1, pts[1])
rs.AddTextDot(2, pts[2])
rs.AddTextDot(3, pts[3])
rs.AddTextDot(4, pts[4])
rs.AddTextDot(5, pts[5])

#Extract edit points of a curve
editPts = rs.CurveEditPoints(crves[0])
#print len(editPts)

#Label points in curves
rs.AddTextDot(0, editPts[0])
rs.AddTextDot(1, editPts[1])
rs.AddTextDot(2, editPts[2])
rs.AddTextDot(3, editPts[3])
rs.AddTextDot(4, editPts[4])
rs.AddTextDot(5, editPts[5])

#Explode curves into segments
crvSeg = rs.ExplodeCurves(crves[2], True)
print crvSeg

#Identify index number of curves and label them
midPts = []
midPts.append(rs.CurveMidPoint(crvSeg[0]))
midPts.append(rs.CurveMidPoint(crvSeg[1]))
midPts.append(rs.CurveMidPoint(crvSeg[2]))
midPts.append(rs.CurveMidPoint(crvSeg[3]))
midPts.append(rs.CurveMidPoint(crvSeg[4]))

rs.AddTextDot(0, midPts[0])
rs.AddTextDot(1, midPts[1])
rs.AddTextDot(2, midPts[2])
rs.AddTextDot(3, midPts[3])
rs.AddTextDot(4, midPts[4])