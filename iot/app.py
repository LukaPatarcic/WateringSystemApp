import RPi.GPIO as GPIO
import time
import functions as fn
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
photo_ch = 0

def init():
    print("Setting up pins...")
    GPIO.setwarnings(False)
    GPIO.cleanup()  # clean up at the end of your script
    GPIO.setmode(GPIO.BCM)  # to specify whilch pin numbering system
    # set up the SPI interface pins
    GPIO.setup(SPIMOSI, GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
    GPIO.setup(SPICLK, GPIO.OUT)
    GPIO.setup(SPICS, GPIO.OUT)


def main():
    # init()
    fn.send_water_level(10)
    time.sleep(2)
    print("will start detec water level\n")
    while True:
        time.sleep(1)
        print("Loop")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

GPIO.cleanup()
