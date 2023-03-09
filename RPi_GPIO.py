import RPi.GPIO as GPIO
import time
GPIO.setmode(GP, IO.BCM)
pwm = GPIO.PWM(18, 1000)
pwm.start(0)

while True:
    print("Enter a duty cycle (0-100) or 'q' to quit:")
    user_input = input()
    if user_input == 'q':
        break
    duty_cycle = int(user_input)
    if  duty_cycle < 0 or duty_cycle > 100:
        print("Individual duty cycle")
    pwm.ChangeDutyCycle(duty_cycle)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(18, GPIO.LOW)