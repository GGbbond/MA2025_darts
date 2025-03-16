import cv2
from camera import *
from detect import *
from select_aim import *
import serial
import serial.tools.list_ports
import struct

if __name__ == '__main__':
	
    #打开电脑摄像头
    # cap = cv2.VideoCapture(0)

    #神经网络置信度
    scores_threshold = 0.5
    
    ser = serial.Serial("/dev/ttyUSB0", 115200)    # 打开/dev/ttyUSB0，将波特率配置为115200，其余参数使用默认值
    if ser.isOpen():                        # 判断串口是否成功打开
        print("打开串口成功。")
        print(ser.name)    # 输出串口号
    else:
        print("打开串口失败。")

    cam, pData, nDataSize, stFrameInfo = open_camera()
    cv2.namedWindow("raw_img", cv2.WINDOW_NORMAL)

	
    while True:
        cv2.resizeWindow("raw_img", 600, 480)
        frame = export_frame(cam, pData, nDataSize, stFrameInfo)
        # ret, frame = cap.read()
        aims = detect(model_path, frame, scores_threshold)
        print("aims_len : ", len(aims))
        if len(aims) > 0:
            print("one")
            aim = select_aim(aims)
            offset = calculated_offset(frame, aim)
            Target_identified = 1
        else:
            offset = 0.0
            Target_identified = 0
        data = struct.pack('ff', Target_identified, offset)
        write_len = ser.write(data)

        

        print("aims_len : ", len(aims))
        cv2.imshow("raw_img", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 关闭设备与销毁句柄
    close_and_destroy_device(cam)
    ser.close()
    # cap.release()
    cv2.destroyAllWindows()