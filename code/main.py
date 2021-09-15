from ad8232 import AD8232 #导入AD8232库
from machine import Pin, SPI, I2C #导入通信以及引脚相关的库
import st7789 #导入屏幕驱动库
import utime

def InitialGestureRes(i2c):
    print(i2c.scan())  #115
    while True:
        i2c.write(115, b'\xEF')
        utime.sleep(0.01)
        flag = i2c.readfrom_mem(115, 0x00, 1)
        if flag ==[32]:
            break
    i2c.write(115, b'\xEF\x01')  #进入BANK1
    i2c.write(115, b'\x72\x01')  #使能工作
    i2c.write(115, b'\xEF\x00')  #进入BANK0
    print(i2c.readfrom_mem(115, 0x41, 1))   #获取当前哪些手势可以被识别
    i2c.write(115, b'\x41\x0C')  #设置为只有向左移动和向右移动可以被识别
    print(i2c.readfrom_mem(115, 0x41, 1))   #检测是否成功录入
    print(i2c.readfrom_mem(115, 0x43, 1))
    i2c.write(115, b'\xEF\x00')  #进入BANK0
    
def draw_start_enum():
    display.fill_rect(0, 0, 240,5,st7789.color565( 175,212, 253))
    display.fill_rect(0, 235, 240,5,st7789.color565( 175,212, 253))
    display.fill_rect(0, 0, 5,240,st7789.color565( 175,212, 253))
    display.fill_rect(235, 0, 5,240,st7789.color565( 175,212, 253))
    display.draw_string(12, 40, "Wear your lead patch", color=st7789.BLACK, bg=st7789.WHITE, size=2, vertical=False, rotate=st7789.ROTATE_0, spacing=1)
    display.draw_string(130, 140, "E C G", size=2, color=st7789.color565(0, 0, 0), bg=st7789.color565(255, 255, 255))
    display.fill_rect(70, 90, 5, 20, st7789.color565(239, 91, 91))
    display.fill_rect(75, 85, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(80, 80, 20, 5, st7789.color565(239, 91, 91))
    display.fill_rect(100, 85, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(105, 90, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(110, 85, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(115, 80, 20, 5, st7789.color565(239, 91, 91))
    display.fill_rect(135, 85, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(140, 90, 5, 20, st7789.color565(239, 91, 91))
    display.fill_rect(135, 110, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(130, 115, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(125, 120, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(120, 125, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(115, 130, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(110, 135, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(105, 140, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(100, 135, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(95, 130, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(90, 125, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(85, 120, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(80, 115, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(75, 110, 5, 5, st7789.color565(239, 91, 91))
    display.fill_rect(80, 85, 20, 5, st7789.color565(250, 142, 142))
    display.fill_rect(115, 85, 20, 5, st7789.color565(250, 142, 142))
    display.fill_rect(75, 90, 30, 5, st7789.color565(250, 142, 142))
    display.fill_rect(110, 90, 30, 5, st7789.color565(250, 142, 142))
    display.fill_rect(75, 95, 65, 5, st7789.color565(250, 142, 142))
    display.fill_rect(75, 100, 65, 5, st7789.color565(250, 142, 142))
    display.fill_rect(75, 105, 65, 5, st7789.color565(250, 142, 142))
    display.fill_rect(80, 110, 55, 5, st7789.color565(250, 142, 142))
    display.fill_rect(85, 115, 45, 5, st7789.color565(250, 142, 142))
    display.fill_rect(90, 120, 35, 5, st7789.color565(250, 142, 142))
    display.fill_rect(95, 125, 25, 5, st7789.color565(250, 142, 142))
    display.fill_rect(100, 130, 15, 5, st7789.color565(250, 142, 142))
    display.fill_rect(105, 135, 5, 5, st7789.color565(250, 142, 142))

    display.fill_rect(30, 180, 20, 2, st7789.color565(0, 0, 0))
    display.fill_rect(50, 176, 2, 4, st7789.color565(0, 0, 0))
    display.fill_rect(52, 172, 2, 4, st7789.color565(0, 0, 0))
    display.fill_rect(54, 168, 2, 4, st7789.color565(0, 0, 0))
    display.fill_rect(56, 164, 2, 4, st7789.color565(0, 0, 0))
    display.fill_rect(58, 168, 2, 4, st7789.color565(0, 0, 0))
    display.fill_rect(60, 172, 2, 4, st7789.color565(0, 0, 0))
    display.fill_rect(62, 176, 2, 4, st7789.color565(0, 0, 0))
    display.fill_rect(64, 180, 2, 4, st7789.color565(0, 0, 0))
    display.fill_rect(66, 184, 2, 4, st7789.color565(0, 0, 0))
    display.fill_rect(68, 188, 2, 4, st7789.color565(0, 0, 0))
    display.fill_rect(70, 192, 2, 4, st7789.color565(0, 0, 0))
    display.fill_rect(72, 186, 2, 6, st7789.color565(0, 0, 0))
    display.fill_rect(74, 180, 2, 6, st7789.color565(0, 0, 0))
    display.fill_rect(76, 174, 2, 6, st7789.color565(0, 0, 0))
    display.fill_rect(78, 168, 2, 6, st7789.color565(0, 0, 0))
    display.fill_rect(80, 162, 2, 6, st7789.color565(0, 0, 0))
    display.fill_rect(82, 156, 2, 6, st7789.color565(0, 0, 0))
    display.fill_rect(84, 150, 2, 6, st7789.color565(0, 0, 0))
    display.fill_rect(86, 156, 2, 6, st7789.color565(0, 0, 0))
    display.fill_rect(88, 162, 2, 6, st7789.color565(0, 0, 0))
    display.fill_rect(90, 168, 2, 6, st7789.color565(0, 0, 0))
    display.fill_rect(92, 174, 2, 6, st7789.color565(0, 0, 0))
    display.fill_rect(94, 180, 100, 2, st7789.color565(0, 0, 0))

    display.line(205,200, 215, 210, st7789.color565(95, 99, 104))
    display.line(205, 220, 215, 210, st7789.color565(95, 99, 104))
    display.line(204,200, 214, 210, st7789.color565(95, 99, 104))
    display.line(204,220, 214, 210, st7789.color565(95, 99, 104))
    display.line(203,200, 213, 210, st7789.color565(95, 99, 104))
    display.line(203,220, 213, 210, st7789.color565(95, 99, 104))

def start_button():
    display.line(205,200, 215, 210, st7789.color565(95, 99, 104))
    display.line(205, 220, 215, 210, st7789.color565(95, 99, 104))
    display.line(204,200, 214, 210, st7789.color565(95, 99, 104))
    display.line(204,220, 214, 210, st7789.color565(95, 99, 104))
    display.line(203,200, 213, 210, st7789.color565(95, 99, 104))
    display.line(203,220, 213, 210, st7789.color565(95, 99, 104))

def return_button():
    display.line(222,8, 212, 18, st7789.color565(95, 99, 104))
    display.line(222, 28, 212, 18, st7789.color565(95, 99, 104))
    display.line(223,8, 213, 18, st7789.color565(95, 99, 104))
    display.line(223,28, 213, 18, st7789.color565(95, 99, 104))
    display.line(224,8, 214, 18, st7789.color565(95, 99, 104))
    display.line(224,28, 214, 18, st7789.color565(95, 99, 104))

def draw_grid():
    grid_x = 0
    grid_y = 60
    for i in range(12):  #画竖线
        display.line(grid_x, 40, grid_x, 239, grid_clr)
        grid_x += 20
    for i in range(9):  #画直线
        display.line(0, grid_y, 239, grid_y, grid_clr)
        grid_y += 20
    display.line(0, 40, 239, 40, st7789.color565(80,183,193))   

def draw_heart():
    scale = 5
    x_offset= -2
    y_offset= 4
    display.fill_rect(8+x_offset, 10+y_offset, scale, 5, st7789.color565(239, 91, 91))
    display.fill_rect(13+x_offset, 5+y_offset, scale, 15, st7789.color565(239, 91, 91))
    display.fill_rect(18+x_offset, 10+y_offset, scale, 15, st7789.color565(239, 91, 91))
    display.fill_rect(23+x_offset, 5+y_offset, scale, 15, st7789.color565(239, 91, 91))
    display.fill_rect(28+x_offset, 10+y_offset, scale, 5, st7789.color565(239, 91, 91))

def fliter_adc(): #过滤0.01秒内的adc数据，取均值作为采样值
    size=0
    adc_data = [888]*60
    start = utime.ticks_ms()
    while True:
        if(size < 70):
            if heartSensor.value(LO = 1) != 1 and heartSensor.value(LO = 2) != 1: #判断电极片是否脱落
                adc_data[size] = heartSensor.read()
                size +=1

        if(utime.ticks_diff(utime.ticks_ms(),start)>=sample_time*1000):
            break
    
    if size > 5:
        aver = (sum(adc_data[0:size]) -  max(adc_data[0:size]) - min(adc_data[0:size])) / (size -2)
    else:
        aver = 888
    
    size =0
    return aver

def calcul_averBPM():  #计算当前与前3次心率平均值
    global  beatIndex, BPM,  beats
    beats[beatIndex] = BPM
    beatIndex = (beatIndex + 1) % 4
    return sum(beats)/4

def Rwave_detection(readData):
    #preReadData = readData
    #readData = fliter_adc()
    global preReadData
    global idx
    global num_filter, DATA_SIZE,mid,Flag,timeCount
    global data

    if readData - preReadData < num_filter:   #滤除突变噪声信号干扰
        data[idx] = readData                        #填充缓存数组
        idx += 1	

    if idx >= DATA_SIZE:
        idx = 0	                      # 数组填满，从头再填
        max_data = max(data)          # 通过缓存数组获取波峰、波谷值，并计算中间值作为判定参考阈值
        min_data = min(data)
        mid = (max_data + min_data) / 5 * 2.65  #该系数可微调，升高或降低阈值
        num_filter = (max_data - min_data) / 2

    pre_Flag = Flag	
    if readData > mid:
        Flag =  1
    else: 
        Flag =  0

    if pre_Flag == 0 and Flag == 1 and timeCount > 35 and readData - preReadData >= 5:
        return True
    else:
        return False

def calcul_BPM():
    global timeCount, rCount, BPM
    rCount += 1
    rCount %= 2
    if rCount == 1: #两次心跳的第一次
        timeCount=0   
    
    elif rCount == 0: # 两次心跳的第二次
        if timeCount > 35:
            IBI = timeCount * sample_time	#计算相邻两次心跳的时间，得到 IBI，可以加上计时器时间以获得更精准的值
            BPM = 60 / IBI                  # 通过 IBI 得到心率值 BPM
            if BPM > 170:                   #限制BPM最高显示值
                BPM = 170
            elif BPM < 30:                  #限制BPM最低显示值
                BPM = 30
            print(calcul_averBPM() , BPM)
        else:
            rCount = 1
        timeCount=0 

def draw_ECG():
    global heartSensorValue, height_new, height_old, line_clr
    y = int(heartSensorValue / 1200 * 240) - 100   
    height_new = 240 - y + 15

    if height_new <= 40:
        height_new = 180
    elif height_new > 239:
        height_new = 180
    display.line(x-1, height_old, x, height_new, line_clr)
    height_old = height_new

def draw_BPM():
    global heartRate_old, heartRate,BPM, str_x,str_y,BPM_strx,str_clr,str_heartRate_size,heartRateStr
    heartRate_old = heartRate
    heartRate = int(BPM)
    if heartRate != heartRate_old:
        if(heartRate < 100 and heartRate_old >= 100):
            display.fill_rect(str_x, str_y, 110, 26,st7789.color565(255, 255, 255))
            BPM_strx = 75

        if(heartRate_old < 100 and heartRate >= 100):
            display.fill_rect(str_x, str_y, 110, 26,st7789.color565(255, 255, 255))
            BPM_strx = 90
        
        if(heartRate < 100):
            BPM_strx = 75
        else:
            BPM_strx = 90    

        heartRateStr = str(heartRate)
        display.draw_string(str_x, str_y, heartRateStr,size=str_heartRate_size,color = str_clr)
        display.draw_string(BPM_strx, 16, "BPM",size=2,color = st7789.color565(113, 191, 255)) 
        heartRate_old = heartRate

def ScreenEdge_Detection():
    global x,heartRateStr,str_heartRate_size,str_clr,BPM_strx
    if x >= 240:
        x = 1
        display.fill(st7789.color565(255, 255, 255))
        draw_grid()
        draw_heart()
        display.draw_string(str_x, str_y, heartRateStr,size=str_heartRate_size,color = str_clr)
        display.draw_string(BPM_strx, 16, "BPM",size=2,color = st7789.color565(113, 191, 255)) 
        return_button()
    else:
        x += 1

def StartDetection():
    ges = i2c.readfrom_mem(115, 0x43, 1)
    if ges == [8]:
        display.fill_circle(207, 210, 18, st7789.color565(236, 236, 236))
        start_button()
        utime.sleep(0.1)
        print("start")
        return True
    else:
        return False

def ReturnDetection(): 
    ges = i2c.readfrom_mem(115, 0x43, 1)
    if ges == [4]:
        display.fill_circle(220, 18, 15, st7789.color565(236, 236, 236))
        return_button()
        utime.sleep(0.1)
        print("return")
        return True
    else:
        return False

def ReadDataAndDropDetection():
    global heartSensor
    global line_clr        
    if heartSensor.value(LO = 1) == 1 or heartSensor.value(LO = 2) == 1: #判断电极片是否脱落
        print("!")
        line_clr = st7789.color565(255, 0, 0) #电极片脱落后曲线颜色变为红色，心率数字颜色变为红色作为脱落提示
        return 875

    else:
        line_clr = st7789.color565(0, 0, 0)
        return fliter_adc()   #读取心电传感器数据

#--------------------------------------初始化驱动--------------------------------------------
heartSensor = AD8232(analogPin = 5, LO1Pin=2, LO2Pin=14) #构造心电传感器对象

spi = SPI(0, baudrate=40000000, polarity=1, phase=0, bits=8, endia=0, sck=Pin(6), mosi=Pin(8)) #构造spi对象
display = st7789.ST7789(spi, 240, 240, reset=Pin(11,func=Pin.GPIO, dir=Pin.OUT), dc=Pin(7,func=Pin.GPIO, dir=Pin.OUT)) #构造屏幕控制对象
display.init() #屏幕初始化

i2c = I2C(1, scl=Pin(1), sda=Pin(0), freq=400000)
InitialGestureRes(i2c)
#--------------------------------------------------------------------------------------------

#----------------------------初始化变量---------------------------------------
backgroud_clr = st7789.color565(255, 255, 255) #设置背景颜色为白色
line_clr = st7789.color565(0, 0, 0) #心电图显示用颜色
str_clr = st7789.color565(113, 191, 255) #心率显示用颜色
grid_clr = st7789.color565(255,225,225) #网格线颜色
heartSensorValue = 900
preReadData = 0	
mid = 0
DATA_SIZE = 100
idx = DATA_SIZE-2
num_filter = 400
rCount = 0
timeCount  =0
Flag = 0 #数据是否大于阈值
data = [888]*100
beats=[78] *4 
beatIndex = 0
sample_time = 0.01
BPM=76
BPM_strx = 75
heartSensorValue = 0
height_old = 120
height_new = 120
x = 1
str_x = 37
str_y = 8
str_heartRate_size = 3
heartRate = 0
heartRate_old = 100
heartRateStr = "60"
#---------------------------------------------------------------------------

if __name__ == "__main__":
    while True:
        #----------------绘制主菜单------------
        display.fill(backgroud_clr)
        draw_start_enum() 
        #-------------------------------------

        #--------------手势检测是否退出当前主菜单循环进入绘制界面---------
        while True:
            if StartDetection():
                break
        #--------------------------------------------------------------

        #-------------------------------初始化心电图绘制界面----------------------------------
        display.fill(backgroud_clr)
        draw_grid() 
        draw_heart()
        return_button()
        display.draw_string(str_x, str_y, heartRateStr,size=str_heartRate_size,color = str_clr)
        display.draw_string(BPM_strx, 16, "BPM",size=2,color = st7789.color565(113, 191, 255)) 
        #--------------------------------------------------------------------------------------

        #----------------------------绘制心电图并显示实时数据--------------------------------
        while True:
            preReadData = heartSensorValue
            heartSensorValue = ReadDataAndDropDetection() # 检测导联是否脱落并读取有效数据
            isRwave = Rwave_detection(heartSensorValue)   # 检测R波

            if isRwave:       # 寻找到“信号上升到振幅中间位置”的特征点
                calcul_BPM()  # 计算心率
            else:
                Flag = 0
            timeCount += 1

            draw_BPM()             # 输出心率至屏幕
            draw_ECG()             # 将心电数据转化为坐标，两点连线输出到屏幕
            ScreenEdge_Detection() # 检测图像是否绘制到屏幕边缘
            if ReturnDetection():   # 手势检测是否返回主菜单
                break
        #-----------------------------------------------------------------------------------
           