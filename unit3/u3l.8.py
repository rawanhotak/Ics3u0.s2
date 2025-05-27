def wc(TdegC: float, windKPH: float) -> float:
    """
    * Calculates the wind chill, given
    * TdegC: the temp in degrees C
    * windKPH: the wind speed in km/h
    *
    * Returns:
    * vTemp: Wind chill in degrees C
    """
    vTemp = 0
    # place your code here!
    return vTemp
# the Main program
T = -5.0
W = 10.0
print("WC=%8.3f T=%8.3f W=%6.3f km/h" % (wc(T, W), T, W))
T = -20.0
W = 20.0
print("WC=%8.3f T=%8.3f W=%6.3f km/h" % (wc(T, W), T, W))
T = -45.0
W = 40.0
print("WC=%8.3f T=%8.3f W=%6.3f km/h" % (wc(T, W), T, W))
