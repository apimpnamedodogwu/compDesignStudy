import rhinoscriptsyntax as rs
import random as rnd
originPoint = rs.GetObject('select a point', rs.filter.point)
radius = rnd.randint(6, 15)
circle = rs.AddCircle(originPoint, radius)
rs.HideObject(circle)

#divide the curve into segements to construct and use the points to cinstruct further geometry
circlePoints = rs.DivideCurve(circle, 8, False, True)

#label the points of the circle
rs.AddTextDot('pt[0]', circlePoints[0])
rs.AddTextDot('pt[1]', circlePoints[1])
rs.AddTextDot('pt[2]', circlePoints[2])
rs.AddTextDot('pt[3]', circlePoints[3])
rs.AddTextDot('pt[4]', circlePoints[4])
rs.AddTextDot('pt[5]', circlePoints[5])
rs.AddTextDot('pt[6]', circlePoints[6])
rs.AddTextDot('pt[7]', circlePoints[7])

#create a sqaure around the centre of the circle
squareGUID = rs.AddCurve((circlePoints[3], circlePoints[5], circlePoints[7], circlePoints[1], circlePoints[3]), 1)
scaledSquare = rs.ScaleObject(squareGUID, originPoint, (.4, .4, .4))

#extract the points from the scaled square to be used in constructing further geometry
scaledSquarePoints = rs.CurveEditPoints(scaledSquare)

#label the points of the square
#rs.AddTextDot('sqr[0]', scaledSquarePoints[0])
#rs.AddTextDot('sqr[1]', scaledSquarePoints[1])
#rs.AddTextDot('sqr[2]', scaledSquarePoints[2])
#rs.AddTextDot('sqr[3]', scaledSquarePoints[3])

#for the center square
rs.AddCurve((scaledSquarePoints[0], originPoint, scaledSquarePoints[1]), 1)
rs.AddCurve((scaledSquarePoints[3], originPoint, scaledSquarePoints[2]), 1)

##for the triangles around the center square
#triangleOne = rs.AddCurve((circlePoints[2], scaledSquarePoints[0], scaledSquarePoints[3], circlePoints[2]), 1)
#triangleOneCentre = rs.AddPoint(rs.CurveAreaCentroid(triangleOne)[0])
#rs.HideObject(triangleOneCentre)
#innerCircleOne = rs.ScaleObject(rs.AddCircle(triangleOneCentre, 4), triangleOneCentre, (.5, .5, .5))
#
#triangleTwo = rs.AddCurve((circlePoints[4], scaledSquarePoints[0], scaledSquarePoints[1], circlePoints[4]), 1)
#triangleTwoCentre = rs.AddPoint(rs.CurveAreaCentroid(triangleTwo)[0])
#rs.HideObject(triangleTwoCentre)
#innerCircleTwo = rs.ScaleObject(rs.AddCircle(triangleTwoCentre, 4), triangleTwoCentre, (.5, .5, .5))
#
#
#triangleThree = rs.AddCurve((circlePoints[6], scaledSquarePoints[1], scaledSquarePoints[2], circlePoints[6]), 1)
#triangleThreeCentre = rs.AddPoint(rs.CurveAreaCentroid(triangleThree)[0])
#rs.HideObject(triangleThreeCentre)
#innerCircleThree = rs.ScaleObject(rs.AddCircle(triangleThreeCentre, 4), triangleThreeCentre, (.5, .5, .5))
# 
#triangleFour = rs.AddCurve((circlePoints[0], scaledSquarePoints[3], scaledSquarePoints[2], circlePoints[0]), 1)
#triangleFourCentre = rs.AddPoint(rs.CurveAreaCentroid(triangleFour)[0])
#rs.HideObject(triangleFourCentre)
#innerCircleFour = rs.ScaleObject(rs.AddCircle(triangleFourCentre, 4), triangleFourCentre, (.5, .5, .5))


