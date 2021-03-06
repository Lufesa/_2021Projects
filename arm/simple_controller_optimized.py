
# Import libraries
import pigpio
import time

pi = pigpio.pi()





try:
    while True:
        data = float(str(input('Enter angle between 0 & 180: ')))
        data2 = data.split(', ')
        if data2[0] == "A":
            print("First motor turning\n")
            angle = float(data2[1])
            if (angle<0) or (angle>180):
                print("Wrong angle value inputed \n")  
            else:
                pi.set_servo_pulsewidth(17, angle*(2460-500)/180.0 + 500)
                print("Angle value changed to " + data2[1] + "\n") 

        elif data2[0] == "B":
            print("Second motor turning\n")
            angle = float(data2[1])
            if (angle<0) or (angle>180):
                print("Wrong angle value inputed \n")  
            else:
                pi.set_servo_pulsewidth(18, angle*(2430-510)/180.0 + 510)
                print("Angle value changed to " + data2[1] + "\n") 
        elif data2[0] == "C":
            print("Third motor turning\n")
            angle = float(data2[1])
            if (angle<0) or (angle>180):
                print("Wrong angle value inputed \n")  
            else:
                pi.set_servo_pulsewidth(27, angle*(2500-500)/180.0 + 500)
                print("Angle value changed to " + data2[1] + "\n") 
        elif data2[0] == "D":
            print("Fourth motor turning\n")
            angle = float(data2[1])
            if (angle<150) or (angle>180):
                print("Wrong angle value inputed \n")  
            else:
                pi.set_servo_pulsewidth(22, angle*(2500-1500)/180.0 + 1500)
                print("Angle value changed to " + data2[1] + "\n") 
        else:
            print("Not recognized this input : " + data2[0]+"\n")

finally:
    # Clean things up at the end
    pi.stop()
    print("Done ! Should be clean now")
