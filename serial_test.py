import serial
import serial.tools.list_ports
import struct
 
# # 获取所有串口设备实例。
# # 如果没找到串口设备，则输出：“无串口设备。”
# # 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
# ports_list = list(serial.tools.list_ports.comports())
# if len(ports_list) <= 0:
#     print("无串口设备。")
# else:
#     print("可用的串口设备如下：")
#     for comport in ports_list:
#         print(list(comport)[0], list(comport)[1])


ser = serial.Serial("/dev/ttyUSB0", 115200)    # 打开COM17，将波特率配置为115200，其余参数使用默认值
if ser.isOpen():                        # 判断串口是否成功打开
    print("打开串口成功。")
    print(ser.name)    # 输出串口号
else:
    print("打开串口失败。")

i = 0
angle_hex = [0, 0, 0]
angle_dec = [0, 0, 0]
while True:
    i = i + 1
    print("--------------",i,"--------------")
    yaw = 1.0
    pitch = 2.0
    roll = 3.0
    data = struct.pack('fff',yaw, pitch, roll)
    # 串口发送 ABCDEFG，并输出发送的字节数。
    write_len = ser.write(data)
    print("write_len : ",write_len)
    # print("串口发出{}个字节。".format(write_len))

    com_input = ser.read(1)
    if com_input.hex() == '5a':
        angle_hex = ser.read(3)
        a = angle_hex[1]
        a = a + 1
        print(a)
        # angle_dec[0] = int(angle_hex[0].hex(),16)
        # angle_dec[1] = int(angle_hex[1].hex(),16)
        # angle_dec[2] = int(angle_hex[2].hex(),16)

    # if com_input:   # 如果读取结果非空，则输出
    #         print(angle_dec)

ser.close()
if ser.isOpen():                        # 判断串口是否关闭
    print("串口未关闭。")
else:
    print("串口已关闭。")