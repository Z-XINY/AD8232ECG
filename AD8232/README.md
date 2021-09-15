# 心电图监测仪

## 案例展示

  读取心电数据, 将其以心电图方式输出在屏幕上, 并计算心率

![project](https://gitee.com/xinyuan-zhu/waffle-nano-v1-sensor-lib/raw/master/AD8232/img/project.jpg)

## 物理连接

### 传感器选择

   传感器选择如下图所示的型号为AD8232的心电图监测传感器模块

![ad8232](https://gitee.com/xinyuan-zhu/waffle-nano-v1-sensor-lib/raw/master/AD8232/img/ad8232.jpg)

### 传感器接线

  传感器与Waffle Nano 之间的接线方式如下表所示，且未在下表中显示的引脚均处于悬空不连状态

| Waffle Nano | 传感器 |
| ----------- | ------ |
| 3V3         | 3.3V   |
| G02         | LO+    |
| G14         | LO-    |
| G05         | OUTPUT |
| GND         | GND    |

## 传感器库使用

  可以获取[ad8232.py](https://gitee.com/blackwalnutlabs/waffle-nano-v1-sensor-lib/blob/master/AD8232/code/ad8232.py),将此库通过[Waffle Maker](https://wafflenano.blackwalnut.tech/ide/index.html#/editor) 的文件上传功能将此库上传到`Waffle Nano`

  我们在可以在主函数中使用以下代码导入此库

```python
from ad8232 import AD8232
```

  在对象构造函数中，我们需要传入三个引脚数字，分别是ADC引脚，以及两个可设置模式为输入的引脚

```python
heartSensor = AD8232(analogPin = 5, LO1Pin = 2, LO2Pin = 14) #构造心电传感器对象
```

  使用心电传感器对象的`read()`方法读取出整型数据

```
heartSensorValue = heartSensor.read() #从心电传感器中获取数据
```

​		关于此库相关细节说明详见代码注释

## 测试代码

  可以获取[main.py](https://gitee.com/blackwalnutlabs/waffle-nano-v1-sensor-lib/blob/master/AD8232/code/main.py)函数，将其内容复制到[Waffle Maker](https://wafflenano.blackwalnut.tech/ide/index.html#/editor) 编辑器上传输给`Waffle Nano`,   即可使用该传感器。

  相关细节说明详见代码注释