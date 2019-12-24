# install circuitpython - pip3 install adafruit-blinka
# install ads1115 lib   - pip3 install adafruit-circuitpython-ads1x15
# install numpy         - pip3 install numpy

import time
import numpy as np

# ADS1115 logic
# import board
# import busio
# import adafruit_ads1x15.ads1115 as ADS
# from adafruit_ads1x15.analog_in import AnalogIn

# i2c = busio.I2C(board.SCL, board.SDA)
# ads = ADS.ADS1115(i2c)
# ads.gain = 2/3
# channel = AnalogIn(ads, ADS.P3)


# ADC settings
resolution = 16
gainlist = {
    2 / 3: 6.144,
    1: 4.096,
    2: 2.048,
    4: 1.024,
    8: 0.512,
    16: 0.256
}
gain = 2 / 3
intmax = (2 ** resolution)
Vsource = 5  # pressure sensor source voltage (V)
samplefreq = 200  # Sampling frquency (Hz)
sampleduration = 20  # duration of heart rate test (s)
interval = 1 / samplefreq  # sleep interval between samples (s)


# Pressure transfer functions (source: MPX5050 datasheet)
# Vout = Vsource * (0.018 * P + 0.04) (V)
# P = ((Vout / Vsource) - 0.04) / 0.018 (kPa)
def SampleToVoltage(sample):
    return sample / intmax * gainlist[gain] * 2


def VoltageToPressure(voltage):
    return ((voltage / Vsource) - 0.04) / 0.018


arraysize = sampleduration * samplefreq
samples = np.zeros(arraysize, dtype=int)

# test = SampleToVoltage(1197)
# print(2 ** resolution)
# print(gainlist[gain])
# print(test)
# test2 = VoltageToPressure(test)
# print()
# print(test2)

try:
    input("Press enter to start")

    while (1):
        # print(channel.value, channel.voltage)

        time.sleep(interval)

except KeyboardInterrupt:
    print("Well then fak off")