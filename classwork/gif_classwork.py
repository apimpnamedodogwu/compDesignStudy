import rhinoscriptsyntax as rs
import random as rnd
num_of_frames = rs.GetInteger('Number of frames to output', 10)

for frame in range(num_of_frames):
    ptDict = {}
    crveList = []
    
    for i in range(10):
        for j in range(10):
            x = i * 5 + (rnd.random()* frame/5)
            y = j * 5 + (rnd.random()* frame/5)
            z = 0
            ptDict[(i,j)] = (x,y,z)
    
    #loop through the dictionary to create a geometry
    for i in range(10):
        for j in range(10):
    #       check that the values are greater than 0 and then make a closed curve
            if i > 0 and j > 0:
                crveList.append(rs.AddCurve((ptDict[(i,j)], ptDict[(i-1,j)], ptDict[(i-1,j-1)], ptDict[(i,j-1)], ptDict[(i,j)]), 1))


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


