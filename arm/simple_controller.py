
# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Setting up the pins
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

#Setting up the servos
servoA = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz
servoB = GPIO.PWM(12,50) # pin 11 for servo1, pulse 50Hz
servoC = GPIO.PWM(13,50) # pin 11 for servo1, pulse 50Hz
servoD = GPIO.PWM(15,50) # pin 11 for servo1, pulse 50Hz


# Initiate PWM running, with value of 0 (pulse off)
servoA.start(0)
servoB.start(0)
servoC.start(0)
servoD.start(0)

try:
    while True:
        data = str(input('Enter angle between 0 & 180: '))
        data2 = data.split(', ')
        if data2[0] == "A":
            print("First motor turning\n")
            angle = float(data2[1])
            if (angle<0) or (angle>180):
                print("Wrong angle value inputed \n")  
            else:
                servoA.ChangeDutyCycle(2+(angle/18))
                print("Angle value changed to " + data2[1] + "\n") 

        elif data2[0] == "B":
            print("Second motor turning\n")
            angle = float(data2[1])
            if (angle<0) or (angle>180):
                print("Wrong angle value inputed \n")  
            else:
                servoB.ChangeDutyCycle(2+(angle/18))
                print("Angle value changed to " + data2[1] + "\n") 
        elif data2[0] == "C":
            print("Third motor turning\n")
            angle = float(data2[1])
            if (angle<0) or (angle>180):
                print("Wrong angle value inputed \n")  
            else:
                servoC.ChangeDutyCycle(2+(angle/18))
                print("Angle value changed to " + data2[1] + "\n") 
        elif data2[0] == "D":
            print("Fourth motor turning\n")
            angle = float(data2[1])
            if (angle<150) or (angle>180):
                print("Wrong angle value inputed \n")  
            else:
                servoA.ChangeDutyCycle(2+(angle/18))
                print("Angle value changed to " + data2[1] + "\n") 
        else:
            print("Not recognized this input : " + data2[0]+"\n")

finally:
    # Clean things up at the end
    servoA.stop()
    servoB.stop()
    servoC.stop()
    servoD.stop()
    GPIO.cleanup()
    print("Done !")
