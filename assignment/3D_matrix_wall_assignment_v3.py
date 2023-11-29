import rhinoscriptsyntax as rs
pt_dict = {}

def mid_point(pt01, pt02):
#   clear all data being held in point variable
    point = None
    point = [(pt01[0] + pt02[0])/2, (pt01[1] + pt02[1])/2, (pt01[2] + pt02[2])/2]
    return point

def point_matrix(imax, jmax, kmax):
    for i in range(imax):
        for j in range(jmax):
            for k in range(kmax):
                x = i + (i*i)
                y = j * 3
                z = k + (k*k)
                point = (x,y,z)
                pt_dict[(i, j, k)] = point
    
    for i in range(imax):
        for j in range(jmax):
            for k in range(kmax):
                if i > 0 and j > 0 and k > 0:
                    curve_back = rs.AddCurve((pt_dict[(i-1,j,k-1)], pt_dict[(i,j,k-1)],
                                pt_dict[(i,j,k)], pt_dict[(i-1,j,k)], pt_dict[(i-1,j,k-1)]),1)
                    rs.AddSrfPt((pt_dict[(i-1,j,k-1)], pt_dict[(i,j,k-1)],
                                pt_dict[(i,j,k)], pt_dict[(i-1,j,k)]))
                    rs.HideObject(curve_back)
                    
                    
                    centre_a_back = mid_point(pt_dict[(i-1, j, k-1)], pt_dict[(i, j, k-1)])
                    # rs.AddPoint(centre_a_back)
                    centre_b_back = mid_point(pt_dict[(i, j, k-1)], pt_dict[(i, j, k)])
                    # rs.AddPoint(centre_b_back)
                    centre_c_back = mid_point(pt_dict[(i, j, k)], pt_dict[(i-1, j, k)])
                    # rs.AddPoint(centre_c_back)
                    centre_d_back = mid_point(pt_dict[(i-1, j, k)], pt_dict[(i-1, j, k-1)])
                    # rs.AddPoint(centre_d_back)

                    centre_line = rs.AddLine(centre_d_back, centre_b_back)
                    centre = rs.CurveMidPoint(centre_line)
                    rs.HideObject(centre_line)
                    # rs.AddPoint(centre)

                    back_pattern = rs.AddCurve((centre_a_back, centre, centre_b_back,
                                               centre_b_back, centre, centre_c_back,
                                          centre_c_back, centre, centre_d_back,
                                          centre_d_back, centre, centre_a_back))
                    
                    
                    curve_front = rs.AddCurve((pt_dict[(i-1,j-1,k-1)], pt_dict[(i,j-1,k-1)],
                                              pt_dict[(i,j-1,k)], pt_dict[(i-1,j-1,k)], pt_dict[(i-1,j-1,k-1)]),1)
                    rs.HideObject(curve_front)
                    
                    centre_a_front = mid_point(pt_dict[(i-1,j-1, k-1)], pt_dict[(i, j-1, k-1)])
                    # rs.AddPoint(centre_a_front)
                    centre_b_front = mid_point(pt_dict[(i,j-1,k-1)], pt_dict[(i, j-1, k)])
                    # rs.AddPoint(centre_b_front)
                    centre_c_front = mid_point(pt_dict[(i,j-1, k)], pt_dict[(i-1, j-1, k)])
                    # rs.AddPoint(centre_c_front)
                    centre_d_front = mid_point(pt_dict[(i-1,j-1, k)], pt_dict[(i-1, j-1, k-1)])
                    # rs.AddPoint(centre_d_front)

                    centre_line = rs.AddLine(centre_d_front, centre_b_front)
                    centre = rs.CurveMidPoint(centre_line)
                    rs.HideObject(centre_line)
                    # rs.AddPoint(centre)

                    front_pattern = rs.AddCurve((centre_a_front, centre, centre_b_front,
                                               centre_b_front, centre, centre_c_front,
                                          centre_c_front, centre, centre_d_front,
                                          centre_d_front, centre, centre_a_front))
                    

                    rs.ReverseCurve(front_pattern)
                    rs.ReverseCurve(back_pattern)
                    start_pt_front = rs.CurveStartPoint(front_pattern)
                    end_pt_back = rs.CurveEndPoint(back_pattern)
                    
                    profile = rs.AddLine(start_pt_front, end_pt_back)
                    curves = [front_pattern, back_pattern]
                    profile = [profile]
                    rs.AddSweep2(curves, profile)

                    rs.HideObject(back_pattern)
                    rs.HideObject(front_pattern)
                    rs.HideObject(profile)


def main():
    
    #get values from user
    imax = rs.GetInteger('maximum number x', 5)
    jmax = rs.GetInteger('maximum number y', 2)
    kmax = rs.GetInteger('maximum number z', 5)
    
    #call function
    rs.EnableRedraw(False)
    point_matrix(imax,jmax,kmax)
    rs.EnableRedraw(True)
    
#call main() function to start program
main()