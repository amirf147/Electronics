#Ideal Diode Characteristics

import math

#Thermal Voltage

k = 1.38E-23 # Boltzmann's constant, J/K

T = 27 #absolute temperature

q = 1.6E-19 # magnitude of electronic charge, C

def vt(T):

    # Returns the thermal voltage of the Diode

    """T in degrees celsius"""

    T = 273 + T
    return (k * T) / q 


Vt = vt(T) # Thermal voltage at 27 degrees celsius

# Shockley's equation for ideal diode

n = 1 # Ideality factor, has range between 1 and 2

def id(Is, Vd):

    # Returns the current through the diode

    """Is is reverse saturation current in pA, i.e. 10)
       Vd is the applied forward-bias voltage across the diode"""

    Is = Is * 10E-12

    return (Is * (math.exp((Vd/(n * Vt))) - 1))
