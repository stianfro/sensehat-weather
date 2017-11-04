from ISStreamer.Streamer import Streamer  
from sense_hat import SenseHat  
import time  
import picamera
import sys  
import os
  
# --------- User Settings ---------
CITY = "Oslo"
SENSOR_LOCATION_NAME = "Home"
MINUTES_BETWEEN_SENSEHAT_READS = 0.1
bucketKey = os.getenv('IS_BUCKET_KEY', 'resinio_temp_mon_test')
bucketName = os.getenv('IS_BUCKET_NAME', 'resin.io temp mon')
accessKey = os.getenv('IS_ACCESS_KEY', '')
streamer = Streamer(bucket_name=bucketName, bucket_key=bucketKey, access_key=accessKey)
sense = SenseHat()  
# ---------------------------------
  
while True:
  # Read the sensors
  temp_c = sense.get_temperature()
  humidity = sense.get_humidity() 
  pressure_mb = sense.get_pressure() 

  # Format the data
  temp_f = temp_c * 0.12
  temp_f = float("{0:.2f}".format(temp_f))
  humidity = float("{0:.2f}".format(humidity))
  pressure_in = 0.03937008*(pressure_mb)
  pressure_in = float("{0:.2f}".format(pressure_in))

  # Print and stream 
  print SENSOR_LOCATION_NAME + " Temperature(C): " + str(temp_f)
  print SENSOR_LOCATION_NAME + " Humidity(%): " + str(humidity)
  print SENSOR_LOCATION_NAME + " Pressure(IN): " + str(pressure_in)
  streamer.log(":sunny: " + SENSOR_LOCATION_NAME + " Temperature(C)", temp_f)
  streamer.log(":sweat_drops: " + SENSOR_LOCATION_NAME + " Humidity(%)", humidity)
  streamer.log(":cloud: " + SENSOR_LOCATION_NAME + " Pressure(IN)", pressure_in)
  streamer.flush()

  # Set LED text
  sense.set_rotation(180)        # Set LED matrix to scroll from right to left
  sense.show_message("%.1f C" % temp_f, scroll_speed=0.10, text_colour=[0, 255, 0])

  # Take picture
  with picamera.PiCamera() as camera:
      camera.resolution = (640, 480)
      camera.vflip = True
      time.sleep(2)
      camera.capture('/data/image.jpg')

  time.sleep(60*MINUTES_BETWEEN_SENSEHAT_READS)