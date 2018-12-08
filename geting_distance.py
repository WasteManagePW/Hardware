"""
Program for finding distance to next object
"""
# Libraries
import RPi.GPIO as GPIO
import time
 
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
# set GPIO Pins
GPIO_TRIGGER = 18 # 18th Pin will be for waking up the measure
GPIO_ECHO = 24    # 24th Pin will be for getting a result
 
# seting GPIO Pins for direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    """
    This function will be activated to measure distance
    It will return the amount of centimeters from object
    """
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # after 0.01ms set Trigger to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()

    # saving time of turning on the measure
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # saving time of getting a result
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime

    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because the wave took the distance back and forth
    distance = (TimeElapsed * 34300) / 2

    # giving the result
    return distance
 
if __name__ == '__main__':
    try: #if in this part gives an error, the program is not collapsing, but goes forward
        while True:
            dist = distance()
            print (f"Measured Distance = {dist} cm") # showing the distance on terminal
            time.sleep(0.5) # wait for half a second
 
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup() # releasing the Pins
