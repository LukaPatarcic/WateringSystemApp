import RPi.GPIO as GPIO
import time
import functions as fn

SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
RELAY = 4
photo_ch = 0
MAX_WATER_LEVEL = 110

print("Setting up pins...")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
GPIO.setup(RELAY, GPIO.OUT)
GPIO.output(RELAY, GPIO.HIGH)


def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)

    GPIO.output(clockpin, False)  # start clock low
    GPIO.output(cspin, False)  # bring CS low

    commandout = adcnum
    commandout |= 0x18  # start bit + single-ended bit
    commandout <<= 3  # we only need to send 5 bits here
    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)

    adcout = 0
    # read in one empty bit, one null bit and 10 ADC bits
    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1

    GPIO.output(cspin, True)

    adcout >>= 1  # first bit is 'null' so drop it
    return adcout


try:
    time.sleep(2)
    print("will start detec water level\n")
    while True:
        adc_value = readadc(photo_ch, SPICLK, SPIMOSI, SPIMISO, SPICS)
        if adc_value > MAX_WATER_LEVEL:
            continue
        if adc_value < 10:
            print("no water\n")
            GPIO.output(RELAY, GPIO.LOW)
        elif adc_value >= 1 and adc_value < MAX_WATER_LEVEL:
            if adc_value >= MAX_WATER_LEVEL * 0.7:
                counter = counter + 1
                if counter >= 3:
                    counter = 0
                    fn.send_message("Water pump", "water pump is filling watter")
                    GPIO.output(RELAY, GPIO.HIGH)
            water_level = str("%.1f" % (adc_value / MAX_WATER_LEVEL * 100))
            print("water level:" + water_level + "%\n")
            fn.send_water_level(water_level)
        # print "adc_value= " +str(adc_value)+"\n"
        time.sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

