from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

tmax = 27
tmin = tmax - 8

while True:
  temp = sense.get_temperature()
  temp_press = sense.get_temperature_from_pressure()
  print(temp)
  temp = int(temp) - tmin
  for x in range(0, 8):
      for y in range(0, temp):
          sense.set_pixel(x, y, 255, 0, 0)
      for y in range(temp, 8):
          sense.set_pixel(x, y, 0, 0, 0)

def tempreading()
    return sense.get_temperature()
    
# this is a placeholder for now, get raw data