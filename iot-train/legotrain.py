#!/usr/bin/python3
import os
import time
from gpiozero.pins.native import NativePin
import gpiozero.devices
# Force the default pin implementation to be NativePin
gpiozero.devices.DefaultPin = NativePin
from gpiozero import Button

LEGO_CH = "1"
LEGO_COL = "R"

REED_PIN = 4
ACC_DELAY = 0.5

rswitch = Button(REED_PIN)

MAX_SPEED = 5
STATION_DELAY = 10

def send_lego_cmd (lego_ch, lego_col, op):
	os.system("irsend --count=5 SEND_ONCE LEGO_Single_Output " +lego_ch+lego_col+"_"+op);

# Go from stop to max speed
def train_speed_up (maxspeed):
    speed = 0
    while speed < maxspeed:
        speed = speed + 1
        send_lego_cmd (LEGO_CH, LEGO_COL, str(speed))
        time.sleep(ACC_DELAY)
        
        
def train_slow_down (currentspeed):
    speed = currentspeed
    while speed > 0:
        speed = speed - 1
        send_lego_cmd (LEGO_CH, LEGO_COL, str(speed))
        time.sleep(ACC_DELAY)

def train_set_speed (speed):
    send_lego_cmd (LEGO_CH, LEGO_COL, str(speed))


def main() :
    while True:
        print ("Leaving the station")
        # Accelerate up to full speed
        train_speed_up(MAX_SPEED)
        # wait until it trigger reed switch
        print ("Going to station")
        rswitch.wait_for_press()
        print ("Stopping at station")
        train_slow_down(MAX_SPEED)
        time.sleep(STATION_DELAY)
    

#Run the main function when this program is run
if __name__ == "__main__":
    main()

