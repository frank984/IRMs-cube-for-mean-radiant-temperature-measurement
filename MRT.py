# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example shows using four MLX90640 sensors attached to TCA9548A channels 0, 1, 2 and 3.
# Use with other I2C sensors would be similar.
import time,board,busio
import numpy as np
from datetime import datetime
import adafruit_mlx90640
import adafruit_tca9548a


# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA
#i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

#use the following correction factor to adjust the Temp value monitored by each sensor, by direct comparison with a Thermal camera, pointing the same omogeneus area.
corr_fact_frame = 0.0 #in °C
corr_fact_frame1 = 0.0 #in °C
corr_fact_frame2 = 0.0 #in °C
corr_fact_frame3 = 0.0 #in °C
corr_fact_frame4 = 0.0 #in °C
corr_fact_frame5 = 0.0 #in °C

'''
# For each sensor, create it using the TCA9548A channel instead of the I2C object
tsl1 = adafruit_tsl2591.TSL2591(tca[0])
tsl2 = adafruit_tsl2591.TSL2591(tca[1])

# After initial setup, can just use sensors as normal.
while True:
    print(tsl1.lux, tsl2.lux)
    time.sleep(0.1)
'''

#mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm

mlx = adafruit_mlx90640.MLX90640(tca[0]) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate

mlx1 = adafruit_mlx90640.MLX90640(tca[1]) # begin MLX90640 with I2C comm
mlx1.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate

mlx2 = adafruit_mlx90640.MLX90640(tca[2]) # begin MLX90640 with I2C comm
mlx2.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate

mlx3 = adafruit_mlx90640.MLX90640(tca[3]) # begin MLX90640 with I2C comm
mlx3.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate

mlx4 = adafruit_mlx90640.MLX90640(tca[4]) # begin MLX90640 with I2C comm
mlx4.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate

mlx5 = adafruit_mlx90640.MLX90640(tca[5]) # begin MLX90640 with I2C comm
mlx5.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate

frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures
frame1 = np.zeros((24*32,)) # setup array for storing all 768 temperatures
frame2 = np.zeros((24*32,)) # setup array for storing all 768 temperatures
frame3 = np.zeros((24*32,)) # setup array for storing all 768 temperatures
frame4 = np.zeros((24*32,)) # setup array for storing all 768 temperatures
frame5 = np.zeros((24*32,)) # setup array for storing all 768 temperatures

while True:
    try:
        mlx.getFrame(frame) # read MLX temperatures into frame var
        mlx1.getFrame(frame1) # read MLX temperatures into frame var
        mlx2.getFrame(frame2) # read MLX temperatures into frame var
        mlx3.getFrame(frame3) # read MLX temperatures into frame var
        mlx4.getFrame(frame4) # read MLX temperatures into frame var
        mlx4.getFrame(frame5) # read MLX temperatures into frame var
        break
    except ValueError:
        continue # if error, just read again

# print out the average temperature from the MLX90640
print('Average MLX90640_zero Temperature: {0:2.1f}C ({1:2.1f}F)'.\
      format(np.mean(frame+corr_fact_frame),(((9.0/5.0)*(np.mean(frame)+corr_fact_frame))+32.0)))
print('Average MLX90640_one Temperature: {0:2.1f}C ({1:2.1f}F)'.\
      format(np.mean(frame1+corr_fact_frame1),(((9.0/5.0)*(np.mean(frame1)+corr_fact_frame1))+32.0)))
print('Average MLX90640_one Temperature: {0:2.1f}C ({1:2.1f}F)'.\
      format(np.mean(frame2+corr_fact_frame2),(((9.0/5.0)*(np.mean(frame2)+corr_fact_frame2))+32.0)))
print('Average MLX90640_one Temperature: {0:2.1f}C ({1:2.1f}F)'.\
      format(np.mean(frame3+corr_fact_frame3),(((9.0/5.0)*(np.mean(frame3)+corr_fact_frame3))+32.0)))
print('Average MLX90640_one Temperature: {0:2.1f}C ({1:2.1f}F)'.\
      format(np.mean(frame4+corr_fact_frame4),(((9.0/5.0)*(np.mean(frame4)+corr_fact_frame4))+32.0)))
print('Average MLX90640_one Temperature: {0:2.1f}C ({1:2.1f}F)'.\
      format(np.mean(frame5+corr_fact_frame5),(((9.0/5.0)*(np.mean(frame5)+corr_fact_frame5))+32.0)))
print('Overall_Average Temperature: {0:2.1f}C ({1:2.1f}F)'.\
      format(np.mean([frame+corr_fact_frame, frame1+corr_fact_frame1,frame2+corr_fact_frame2,frame3+corr_fact_frame3,frame4+corr_fact_frame4,frame5+corr_fact_frame5]),(((9.0/5.0)*np.mean([frame+corr_fact_frame, frame1+corr_fact_frame1,frame2+corr_fact_frame2,frame3+corr_fact_frame3,frame4+corr_fact_frame4,frame5+corr_fact_frame5]))+32.0)))
      #format(np.mean([frame1,frame2]),(((9.0/5.0)*np.mean([frame1,frame2]))+32.0)))

file = open("/home/pi/Desktop/MRT_log.txt","a")
file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S, '))

#if np.mean([frame, frame1,frame2]) is not None:
if np.mean([frame,frame1,frame2,frame3]) is not None:
    file.write('{0:2.1f}' .\
               format(np.mean(frame)+corr_fact_frame)+ ", " +
               '{0:2.1f}' .\
               format(np.mean(frame1)+corr_fact_frame1) + ", " + 
               '{0:2.1f}' .\
               format(np.mean(frame2)+corr_fact_frame2)+ ", " +
               '{0:2.1f}' .\
               format(np.mean(frame3)+corr_fact_frame3)+ ", " +
               '{0:2.1f}' .\
               format(np.mean(frame4)+corr_fact_frame4)+ ", " +
               '{0:2.1f}' .\
               format(np.mean(frame5)+corr_fact_frame5)+ ", " +
               '{0:2.1f}' .\
               format(np.mean([frame+corr_fact_frame, frame1+corr_fact_frame1,frame2+corr_fact_frame2,frame3+corr_fact_frame3,frame4+corr_fact_frame4,frame5+corr_fact_frame5])) +"\n")
               #format(np.mean([frame1,frame2])) +"\n")
else:
    #file = open("/home/pi/Desktop/env_data_monit_with_wearable/MRT/log.txt","a")
    file.write("NAN  " +"\n")
file.close()

