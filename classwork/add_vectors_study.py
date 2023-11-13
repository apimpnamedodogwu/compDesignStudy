import rhinoscriptsyntax as rs


def AddVector(vecdir, base_point=[0,0,0]):
       tip_point = rs.PointAdd(base_point, vecdir)
       line = rs.AddLine(base_point, tip_point)
       if line: return rs.CurveArrows(line, 2)


def vectorfield():
    cloud_id = rs.GetObject("Input pointcloud", 2, True, True)
    if cloud_id is None: return
 
    listpoints = rs.PointCloudPoints(cloud_id)
    base_point = rs.GetPoint("Vector field base point")
    if base_point is None: return
 
    for point in listpoints:
        vecbase = rs.VectorCreate(point, base_point)
        vecdir = rs.VectorCrossProduct(vecbase, (0,0,1))
        if vecdir:
            vecdir = rs.VectorUnitize(vecdir)
            vecdir = rs.VectorScale(vecdir, 2.0)
            AddVector(vecdir, point)

def smoothingvector(point, prev_point, next_point, s):
    pm = (prev_point+next_point)/2.0
    va = rs.VectorCreate(pm, point)
    vm = rs.VectorScale(va, s)
    return vm

# def smoothcurve(curve_id, s):
#     curve_points = rs.CurvePoints(curve_id)
#     new_curve_points = []
 
#     for i in range(1, len(curve_points)-1):
#         vm = smoothingvector(curve_points[i], curve_points[i-1], curve_points[i+1], s)
#         new_curve_points.append( rs.PointAdd(curve_points[i], vm) )
 
#     knots = rs.CurveKnots(curve_id)
#     degree = rs.CurveDegree(curve_id)
#     weights = rs.CurveWeights(curve_id,0)
#     newcurve_id = rs.AddNurbsCurve(new_curve_points, knots, degree, weights)
#     if newcurve_id: rs.DeleteObject(curve_id)
#     return newcurve_id

def smoothcurve(curve_id, s):
    curve_points = rs.CurvePoints(curve_id)
    new_curve_points = []

    # Get the degree of the original curve
    degree = rs.CurveDegree(curve_id)
 
    for i in range(1, len(curve_points) - 1):
        vm = smoothingvector(curve_points[i], curve_points[i - 1], curve_points[i + 1], s)
        new_curve_points.append(rs.PointAdd(curve_points[i], vm))

    # Calculate the number of knots based on the degree and control points
    num_knots = len(new_curve_points) + degree - 1

    # Generate an initial list of knots with proper values
    knots = [i / (num_knots - 1) for i in range(num_knots)]

    # Generate weights for the new curve (in this case, all weights are set to 1)
    weights = [1.0] * len(new_curve_points)

    # Add the first and last knots to make it a closed curve if the original curve was closed
    if rs.IsCurveClosed(curve_id):
        knots += [1.0]

    newcurve_id = rs.AddNurbsCurve(new_curve_points, knots, degree, weights)

    if newcurve_id:
        rs.DeleteObject(curve_id)

    return newcurve_id



def iterativeshortencurve():
    curve_id = rs.GetObject("Open curve to smooth", 4, True)
    if curve_id is None or rs.IsCurveClosed(curve_id): return
 
    min = rs.Distance(rs.CurveStartPoint(curve_id), rs.CurveEndPoint(curve_id))
    max = rs.CurveLength(curve_id)
    goal = rs.GetReal("Goal length", 0.5*(min+max) , min, max)
    if goal is None: return
 
    while rs.CurveLength(curve_id)>goal:
        rs.EnableRedraw(False)
        curve_id = smoothcurve(curve_id, 0.1)
        rs.EnableRedraw(True)
        if curve_id is None: break

def main():
     vectorfield()
     AddVector((2,2,2))
     iterativeshortencurve()
    

main()