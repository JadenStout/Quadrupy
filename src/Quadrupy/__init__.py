from .core import RobotDog

# Auto-connect global dog instance
_dog = RobotDog()

def walk():
    _dog.walk()

def writeScreen(text):
    _dog.writeScreen(text)

def writeMotor(val):
    _dog.writeMotor(val)

def reset():
    _dog.reset()

def close():
    _dog.close()
