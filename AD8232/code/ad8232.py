from machine import ADC, Pin
class AD8232:
    def __init__(self,analogPin,LO1Pin,LO2Pin):
        self.adc = ADC(Pin(analogPin))
        self.adc.equ(ADC.EQU_MODEL_8)
        self.LO1Pin = Pin(LO1Pin, Pin.IN)
        self.LO2Pin = Pin(LO2Pin, Pin.IN)
    def value(self,LO = 1):
        if LO == 1:
            return self.LO1Pin.value() #返回LO+,LO-电平值
        elif LO == 2:
            return self.LO2Pin.value()
    def read(self):
        data = self.adc.read() #读取心电数据
        return data
    