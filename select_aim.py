#选择目标
#   当识别到两个目标(同时识别到前哨站与基地)时，选择前哨站
#   当识别到一个目标时，选择该目标(只剩基地)
def select_aim(aims):
    if len(aims) > 1:
        for aim in aims:
            if aim.class_id == "outpost":
                return aim
    elif len(aims) == 1:
        return aims[0]

#计算当前朝向与目标朝向的偏移量
def calculated_offset(frame, aim):
    #获取窗口宽高
    window_width = frame.shape[1]
    window_height = frame.shape[0]

    #获取窗口中心点坐标
    window_center = (window_width / 2, window_height / 2)
    
    #计算目标中心点坐标
    x = aim.x + aim.w / 2
    y = aim.y + aim.h / 2
    aim_center = (x, y)

    #计算偏移量(目标在窗口中心点左边为正，右边为负)
    offset = window_center[0] - aim_center[0]
    return offset


