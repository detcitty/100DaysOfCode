# v0 : km per hour
# https://www.codewars.com/kata/566be96bb3174e155300001b/train/python


def max_ball(v0):
    # your code
    # convert v0 to m/hr

    v_meter = v0 * 1000
    t = 0
    height = 0
    g = 9.81

    t_list = []
    height_list = []

    theory_max_height = v_meter / g

    while(height < theory_max_height):
        height = v_meter*t - 0.5 * g*t*t
        t_list.append(t)
        height_list.append(height)

        t = t*1.1



    # height = v0*t - 0.5 * g*t*t
    # 0 = v - g*t
    # t = v/g
    #t_max_height = v_meter / g

    return(max(height_list))

max_ball(37)
