import rhinoscriptsyntax as rs
import random as rnd
num_of_frames = rs.GetInteger('Number of frames to output', 10)
#scale = .6
#rotateDegree = 0

for frame in range(num_of_frames):
    ptDict = {}
    crveList = []
    lineList = []
    scale = 0.25 * frame
    rotateDegree = -360 * frame / num_of_frames 
    for i in range(10):
        for j in range(10):
            x = i * 5 + (rnd.random()* frame / 5)
            y = j * 5 + (rnd.random()* frame / 5)
            z = 0
            ptDict[(i,j)] = (x,y,z)
            
            
            

    
    for i in range(10):
        for j in range(10):
            if i > 0 and j > 0:
                diagonal = rs.AddLine(ptDict[(i-1,j-1)], ptDict[(i, j)])
                centre = rs.CurveMidPoint(diagonal)
                rs.DeleteObject(diagonal)
    
    #           Find the mid points of the bone structure 
                constLineA = rs.AddLine(ptDict[(i-1,j-1)], ptDict[(i, j-1)])
                centreA = rs.CurveMidPoint(constLineA)
                lineList.append(constLineA)
#                rs.DeleteObject(constLineA)
    
                constLineB = rs.AddLine(ptDict[(i,j-1)], ptDict[(i, j)])
                centreB = rs.CurveMidPoint(constLineB)
                lineList.append(constLineB)
#                rs.DeleteObject(constLineB)
    
                constLineC = rs.AddLine(ptDict[(i,j)], ptDict[(i-1, j)])
                centreC = rs.CurveMidPoint(constLineC)
                lineList.append(constLineC)
#                rs.DeleteObject(constLineC)
    
                constLineD = rs.AddLine(ptDict[(i-1,j)], ptDict[(i-1, j-1)])
                centreD = rs.CurveMidPoint(constLineD)
                lineList.append(constLineD)
#                rs.DeleteObject(constLineD)
    
    #           Create the pattern and adding them to a list (to be deleted in other to clear the canvas)
                curveA = rs.AddCurve((ptDict[(i-1,j-1)], centre, centreA))
#                scaledCurveA = rs.ScaleObject(curveA, centre, [scale, scale, scale])
#                rotatedCurveA = rs.RotateObject(curveA, centre, rotateDegree)
                crveList.append(curveA)
                
                curveD = rs.AddCurve((ptDict[(i-1,j-1)], centre, centreD))
#                scaledCurveD = rs.ScaleObject(curveD, centre, [scale, scale, scale])
#                rotatedCurveD = rs.RotateObject(curveD, centre, rotateDegree)
                crveList.append(curveD)
                
                curveB = rs.AddCurve((ptDict[(i-1,j-1)], centre, centreB))
#                scaledCurveB = rs.ScaleObject(curveB, centre, [scale, scale, scale])
#                rotatedCurveB = rs.RotateObject(curveB, centre, rotateDegree)
                crveList.append(curveB)
                
                curveC = rs.AddCurve((ptDict[(i-1,j-1)], centre, centreC))
#                scaledCurveC = rs.ScaleObject(curveC, centre, [scale, scale, scale])
#                rotatedCurveC = rs.RotateObject(curveC, centre, rotateDegree)
                crveList.append(curveC)  
                
    #           Mirror the pattern
#                crveList.append(rs.AddCurve(, centre, centreC))
                curveC = rs.AddCurve((ptDict[(i,j)], centre, centreC))
#                scaledCurveC = rs.ScaleObject(curveC, centre, [scale, scale, scale])
#                rotatedCurveC = rs.RotateObject(curveC, centre, rotateDegree)
                crveList.append(curveC)
                
                curveB = rs.AddCurve((ptDict[(i,j)], centre, centreB))
#                scaledCurveB = rs.ScaleObject(curveB, centre, [scale, scale, scale])
#                rotatedCurveB = rs.RotateObject(curveB, centre, rotateDegree)
                crveList.append(curveB)
                
                curveD = rs.AddCurve((ptDict[(i,j)], centre, centreD))
#                scaledCurveD = rs.ScaleObject(curveD, centre, [scale, scale, scale])
#                rotatedCurveD = rs.RotateObject(curveD, centre, rotateDegree)
                crveList.append(curveD)
                
                curveA = rs.AddCurve((ptDict[(i,j)], centre, centreA))
#                scaledCurveA = rs.ScaleObject(curveA, centre, [scale, scale, scale])
#                rotatedCurveA = rs.RotateObject(curveA, centre, rotateDegree)
                crveList.append(curveA)
                
#                crveList.append(rs.AddCurve((ptDict[(i,j)], centre, centreB)))
#                crveList.append(rs.AddCurve((ptDict[(i,j)], centre, centreD)))
#                crveList.append(rs.AddCurve((ptDict[(i,j)], centre, centreA)))

#    specify local folder to output frames
    render_folder = "D:\\CompDesignTuts\\render\\"

    def render_step(render_folder, sequence_num):
#        captures screenshots of the scene frame
        file_name = str(int(sequence_num)).zfill(5)
        file_path = " " + render_folder + file_name + ".png"
        rs.Command("_-ViewCaptureToFile" + file_path + " Enter")
    
    render_step(render_folder, frame)
#    clear canavss for the next frame
#   you have to delete all the objects you are rendering except you wanna overlay the frames of your animation
    rs.DeleteObjects(crveList)
    rs.DeleteObjects(lineList)     