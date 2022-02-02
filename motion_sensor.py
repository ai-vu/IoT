from gpio import *
from time import *

motionSensorValue = 0;

def readFromSensor():
	global motionSensorValue
	
	motionSensorValue = digitalRead(9)

def action():
	if(motionSensorValue == HIGH):
		customWrite(1,"2")
		customWrite(2,"2")
	else:
		customWrite(1, "0")
		customWrite(2, "0")

def main():
	pinMode(9, IN) # motion sensor
	pinMode(1, OUT) # coffee maker
	pinMode(2, OUT) # lamp
	
	while True:
		readFromSensor()
		action()
		delay(1000)

if __name__ == "__main__":
	main()
