from ad8232 import AD8232
import utime

heartSensor = AD8232(analogPin = 5, LO1Pin=2, LO2Pin=14)  #构造ad8232对象

while True:   
    if heartSensor.value(LO = 1) == 1 or heartSensor.value(LO = 2) == 1: #导联脱落检测
        print("!")    
    else:
        heartSensorData = heartSensor.read()  #读取ADC值
        print(heartSensorData)
        utime.sleep(0.1)