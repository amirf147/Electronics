#Diode Characteristics

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
       Vd is the applied voltage across the diode"""

    Is = Is * 10E-12

    return (Is * (math.exp((Vd/(n * Vt))) - 1))

#DC or Static Resistance

def Rdc(Vd, Id, Rb):

    #Returns the static resistance

    """Id is the current across diode)
       Vd is the applied voltage across the diode
       Rb is the body and contact resistance"""

    return (Vd/Id) + Rb

#AC or Dynamic Resistance and Average Resistance

def Rac(deltaVd, deltaId, Rb):

    #Returns the dynamic resistance
    #Can be used to calculate average resistace

    """deltaVd is the change in voltage across diode
       deltaId is the change in current across diode
       Rb is the body and contact resistance"""

    return (deltaVd / deltaId) + Rb

def RacAlt(Vt, Id, Rb):

    #Returns the dynamic resistance, ohms

    """Vt is the Thermal Resistance
       Id is the current through the diode
       Rb is the body and contact resistance"""

    return (Vt / deltaId) + Rb
