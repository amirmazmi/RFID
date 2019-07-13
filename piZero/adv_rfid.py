#1/usr/in/env python3

import RPi.GPIO as GPIO
from mfrc522 import MFRC522

reader = MFRC522()

try:
	content = reader.Read_MFRC522()
	print("Content: ", content)


finally: 
	GPIO.cleanup()


