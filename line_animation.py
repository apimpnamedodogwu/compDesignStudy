import rhinoscriptsyntax as rs
import random as rnd
#rectangle = rs.GetObject("Select a rectangle", rs.filter.curve)
ptOne = rs.GetPoint("select first point", rs.filter.point)
ptTwo = rs.GetPoint("select first point", rs.filter.point)

num_of_frames = rs.GetInteger('Number of frames to output', 10)
for frame in range(num_of_frames):
    line = rs.AddLine(ptOne, ptTwo)
#    circle = rs.AddCircle((0,0,0),10)
#    set variable to animate & accelerate the animation as desired
    x = frame * 2
#    set x position for each frame
    rs.MoveObject(line, (x, 0, 0))
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
    rs.DeleteObject(line) 