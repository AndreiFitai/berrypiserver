import os
import time
from sense_hat import SenseHat

# code inspired from http://yaab-arduino.blogspot.com/2016/08/accurate-temperature-reading-sensehat.html
# normalization values changed based on local testing

# get CPU temperature
def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

# use moving average to smooth readings
def get_smooth(x):
  if not hasattr(get_smooth, "t"):
    get_smooth.t = [x,x,x]
  get_smooth.t[2] = get_smooth.t[1]
  get_smooth.t[1] = get_smooth.t[0]
  get_smooth.t[0] = x
  xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
  return(xs)

sense = SenseHat()

def get_enviromentals():
  t1 = sense.get_temperature_from_humidity()
  t2 = sense.get_temperature_from_pressure()
  t_cpu = get_cpu_temp()
  h = sense.get_humidity()
  p = sense.get_pressure()
  # calculates the real temperature compesating CPU heating
  t = (t1+t2)/2
  t_corr = t - ((t_cpu-t)/2.2)
  t_corr = get_smooth(t_corr)
  return {'temperature': t_corr, 'humidity': h, 'pressure':p, 'pi_cpu_temp':t_cpu}
