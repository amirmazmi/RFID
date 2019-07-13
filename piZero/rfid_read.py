#1/usr/in/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	id,text = reader.read()
	print("ID: ", id)
	print("Text: ", text)


finally: 
	GPIO.cleanup()


