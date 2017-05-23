# ConeVolumeCalculator.py
# Your job is to write a function in ConeVolumeCalculator.py (call
# it **calculateConeVolume()** that calculates the volume of a cone
# factor based on the Volume Calculator
# Calculator.net (http://www.calculator.net/volume-calculator.html)

# Define Function below
# be sure to return an integer

import math
#volume = 1/3πr2h
#where r is the radius of the base, h is the height
def calculateConeVolume(baseRadius, height):

    volume = volume = 1/3*math.pi*baseRadius**2*height
    volume = round(volume, 2)
    return volume

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    answer = calculateConeVolume(10, 2)
    print(answer)
