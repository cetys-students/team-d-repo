from AltIMU_v3 import AltIMUv3
from filters import LowPassFilter, HighPassFilter
import time
import RPi.GPIO as GPIO
import math
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
# Setup Altimu
altimu = AltIMUv3()
altimu.enable()

# Initialize a low pass filter with a default value and a bias of 80%
low_pass_filter = LowPassFilter([0.0, 0.0, 1.0], 0.8)

while True:
    accel = altimu.get_accelerometer_cal()
    gyro = altimu.get_gyro_cal()
    time.sleep(0.1)
    if accel[2]<-1:
        if gyro[2]>30 or gyro[2]<-30:
            GPIO.output(7,True)
    if accel[2]>0.95:
        GPIO.output(7,True)
    if accel[1]>.7:
        GPIO.output(7,True)
    
    else:
        GPIO.output(7,False)
        
    if resultado>.98:
        GPIO.output(10,False)
    else:
        GPIO.output(10,True)
    
