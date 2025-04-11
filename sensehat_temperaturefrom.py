from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temp_p = sense.get_temperature_from_pressure()
temp_h = sense.get_temperature_from_humidity()
print(temp_p,temp_h)