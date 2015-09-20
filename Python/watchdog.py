## AUTHOR: Kieran Owen Wand (14yrs)
## ASSISTANT: Christopher John Butcher (DAD, 35yrs)

## CREATED JUNE 2015

## CREDITS
#   - ASTROPI FORUM MEMBERS, HELP AND SUPPORT FOR SCRIPTS AND FAULT FINDING
#   - RASPBERRY PI FORUM MEMBERS, HELP AND SUPPORT FOR SCRIPTS AND FAULT FINDING
#   - Tsena Wand (MUM), ASSESSING THE EASE OF USE FOR THE READING DISPLAYS AND WARNING STATES


## IMPORT MODULES REQUIRED FOR PROGRAM ##
import RPi.GPIO as GPIO
import time, logging
from datetime import datetime
import sys, os
import astro_pi
from astro_pi import AstroPi
from time import sleep, asctime

## SETS ASTROPI MODULES AS FRIENDLY NAME ##

ap = astro_pi.AstroPi()

# SETTING UP RASPBERRYPI FOR FLIGHT BUTTONS TO USE GPIO PINS

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


# ASSIGNING FRIENDLY NAMES FOR GPIO PINS

UP = 26
DOWN = 13
LEFT = 20
RIGHT = 19
A = 21
B = 16

# FORCING PROGRAM TO RUN WITHIN WHILE LOOP

running = True


## CREATE TIMESTAMP AS FRIENDLY NAME ##

tmstmp = time.strftime("%Y%m%d-%H%M%S")
    
    
## ASSIGNING LEVELS TO LED'S AND COLOURS ##

# ADJUSTABLE LED LIGHT LEVELS

led_level = 150

# ASSIGNING LEVELS TO COLOURS

red = 255                           # TEMPERATURE LED LIGHT LEVEL
blue = 255                          # PRESSURE LED LIGHT LEVEL


## ASSIGNING DEFAULTS TO TEMP + HUM OR PRESSURE PAGES ##

temp_hum_on = 0
psi_on = 0


## ASSIGNING DEFAULTS VALUES TO ALARM TRIGGERS ##

tmp_alarm = 0
hum_alarm = 0
psi_alarm = 0
id_num = 0


## ASSIGNING DEFAULTS TO WARNINIG PAGES (MUTE / SHOW) ##

tmp_mute = 0
hum_mute = 0
psi_mute = 0


## ASSIGNING DEFAULT TO DISPLAY OFF TRIGGER ##

display_mute = 0

## CREATES A LOG FILE WITH THE TITLE "log/{timestamp:%Y-%m-%d-%H-%M}watchdog.csv" ##
## THIS ALSO ADDS A TIMESTAMP TO THE START OF THE FILE NAME CREATED ##

count = 0
file = open('log/'+(str(tmstmp))+' watchdog-log.csv', 'w')
file.write("\"Time\",\"Display\",\"Temperature\",\"Temp_Reading\",\"Temp_Alarm\",\"Humidity\",\"Hum_Reading\",\"Hum_Alarm\",\"Pressure\",\"PSI_Reading\",\"PSI_Alarm\",\"Pitch\",\"Roll\",\"Yaw\"\n")


## EXAMPLE FOR WRITING INFORMATION ONTO LED MATRIX PIXELS:

    #ap.set_pixel(x, y, red, green, blue)
    

## TEMPERATURE NUMBERS MATRIX BELOW ##

def temp_num_matrix_1(num):

  if num == '0':
# number 0_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, led_level, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '1':
    # number 1_top_left - TEMPERATURE
    ap.set_pixel(0, 0, 0, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, led_level, 0, 0)   
    ap.set_pixel(1, 2, led_level, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, 0, 0, 0)   
    ap.set_pixel(2, 1, 0, 0, 0)   
    ap.set_pixel(2, 2, 0, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '2':
# number 2_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, 0, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, led_level, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, 0, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '3':
# number 3_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, 0, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, led_level, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '4':
# number 4_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, led_level, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, 0)
    ap.set_pixel(1, 0, 0, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, led_level, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, 0)
    ap.set_pixel(2, 0, 0, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '5':
# number 5_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, led_level, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, 0, 0, 0)   
    ap.set_pixel(2, 2, 0, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '6':
# number 6_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, led_level, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, 0, 0, 0)   
    ap.set_pixel(1, 1, led_level, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, 0, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '7':
# number 7_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)
  
  if num == '8':
# number 8_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, led_level, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, led_level, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '9':
# number 9_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, led_level, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, led_level, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

def temp_num_matrix_2(num):
    
  if num == '0':
# number 0_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, led_level, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '1':
    # number 1_top_right - TEMPERATURE
    ap.set_pixel(4, 0, 0, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, led_level, 0, 0)   
    ap.set_pixel(5, 2, led_level, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, 0, 0, 0)   
    ap.set_pixel(6, 1, 0, 0, 0)   
    ap.set_pixel(6, 2, 0, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '2':
# number 2_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, 0, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, led_level, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, 0, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '3':
# number 3_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, 0, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, led_level, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '4':
# number 4_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, led_level, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, 0)
    ap.set_pixel(5, 0, 0, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, led_level, 0, 0)   
    ap.set_pixel(5, 3, 0, 0, 0)
    ap.set_pixel(6, 0, 0, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '5':
# number 5_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, led_level, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, 0, 0, 0)   
    ap.set_pixel(6, 2, 0, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '6':
# number 6_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, led_level, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, 0, 0, 0)   
    ap.set_pixel(5, 1, led_level, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, 0, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '7':
# number 7_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, 0, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '8':
# number 8_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, led_level, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, led_level, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '9':
# number 9_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, led_level, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, led_level, 0, 0)   
    ap.set_pixel(5, 3, 0, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

def temp_num_error_high():
# error state warning for - HIGH TEMPERATURE
    ap.set_pixel(0, 0, red, 0, 0)   
    ap.set_pixel(0, 1, red, 0, 0)   
    ap.set_pixel(0, 2, red, 0, 0)   
    ap.set_pixel(0, 3, red, 0, 0)
    ap.set_pixel(1, 0, red, 0, 0)   
    ap.set_pixel(1, 1, red, 0, 0)   
    ap.set_pixel(1, 2, red, 0, 0)   
    ap.set_pixel(1, 3, red, 0, 0)
    ap.set_pixel(2, 0, red, 0, 0)   
    ap.set_pixel(2, 1, red, 0, 0)   
    ap.set_pixel(2, 2, red, 0, 0)   
    ap.set_pixel(2, 3, red, 0, 0)
    ap.set_pixel(3, 0, red, 0, 0)   
    ap.set_pixel(3, 1, red, 0, 0)   
    ap.set_pixel(3, 2, red, 0, 0)   
    ap.set_pixel(3, 3, red, 0, 0)
    ap.set_pixel(4, 0, red, 0, 0)   
    ap.set_pixel(4, 1, red, 0, 0)   
    ap.set_pixel(4, 2, red, 0, 0)   
    ap.set_pixel(4, 3, red, 0, 0)
    ap.set_pixel(5, 0, red, 0, 0)   
    ap.set_pixel(5, 1, red, 0, 0)   
    ap.set_pixel(5, 2, red, 0, 0)   
    ap.set_pixel(5, 3, red, 0, 0)
    ap.set_pixel(6, 0, red, 0, 0)   
    ap.set_pixel(6, 1, red, 0, 0)   
    ap.set_pixel(6, 2, red, 0, 0)   
    ap.set_pixel(6, 3, red, 0, 0)
    ap.set_pixel(7, 0, red, 0, 0)   
    ap.set_pixel(7, 1, red, 0, 0)   
    ap.set_pixel(7, 2, red, 0, 0)   
    ap.set_pixel(7, 3, red, 0, 0)
    
def temp_num_error_low():
# error state warning for - LOW TEMPERATURE
    ap.set_pixel(0, 0, 0, 0, blue)   
    ap.set_pixel(0, 1, 0, 0, blue)   
    ap.set_pixel(0, 2, 0, 0, blue)   
    ap.set_pixel(0, 3, 0, 0, blue)
    ap.set_pixel(1, 0, 0, 0, blue)   
    ap.set_pixel(1, 1, 0, 0, blue)   
    ap.set_pixel(1, 2, 0, 0, blue)   
    ap.set_pixel(1, 3, 0, 0, blue)
    ap.set_pixel(2, 0, 0, 0, blue)   
    ap.set_pixel(2, 1, 0, 0, blue)   
    ap.set_pixel(2, 2, 0, 0, blue)   
    ap.set_pixel(2, 3, 0, 0, blue)
    ap.set_pixel(3, 0, 0, 0, blue)   
    ap.set_pixel(3, 1, 0, 0, blue)   
    ap.set_pixel(3, 2, 0, 0, blue)   
    ap.set_pixel(3, 3, 0, 0, blue)
    ap.set_pixel(4, 0, 0, 0, blue)   
    ap.set_pixel(4, 1, 0, 0, blue)   
    ap.set_pixel(4, 2, 0, 0, blue)   
    ap.set_pixel(4, 3, 0, 0, blue)
    ap.set_pixel(5, 0, 0, 0, blue)   
    ap.set_pixel(5, 1, 0, 0, blue)   
    ap.set_pixel(5, 2, 0, 0, blue)   
    ap.set_pixel(5, 3, 0, 0, blue)
    ap.set_pixel(6, 0, 0, 0, blue)   
    ap.set_pixel(6, 1, 0, 0, blue)   
    ap.set_pixel(6, 2, 0, 0, blue)   
    ap.set_pixel(6, 3, 0, 0, blue)
    ap.set_pixel(7, 0, 0, 0, blue)   
    ap.set_pixel(7, 1, 0, 0, blue)   
    ap.set_pixel(7, 2, 0, 0, blue)   
    ap.set_pixel(7, 3, 0, 0, blue)
 
 
## HUMIDITY NUMBERS MATRIX BELOW ##    

def hum_num_matrix_1(num):

  if num == '0':
# number 0_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, led_level, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '1':
    # number 1_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, 0, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, led_level, 0)   
    ap.set_pixel(1, 6, 0, led_level, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, 0, 0)   
    ap.set_pixel(2, 5, 0, 0, 0)   
    ap.set_pixel(2, 6, 0, 0, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '2':
# number 2_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, 0, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, led_level, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, 0, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '3':
# number 3_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, 0, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, led_level, 0)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '4':
# number 4_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, led_level, 0)   
    ap.set_pixel(0, 7, 0, 0, 0)
    ap.set_pixel(1, 4, 0, 0, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, led_level, 0)   
    ap.set_pixel(1, 7, 0, 0, 0)
    ap.set_pixel(2, 4, 0, 0, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '5':
# number 5_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, led_level, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, 0, 0)   
    ap.set_pixel(2, 6, 0, 0, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '6':
# number 6_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, led_level, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, 0, 0)   
    ap.set_pixel(1, 5, 0, led_level, 0)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, 0, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '7':
# number 7_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, 0, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, 0, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '8':
# number 8_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, led_level, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, led_level, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '9':
# number 9_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, led_level, 0)   
    ap.set_pixel(0, 7, 0, 0, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, led_level, 0)   
    ap.set_pixel(1, 7, 0, 0, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

def hum_num_matrix_2(num):

  if num == '0':
# number 0_bottom_left - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, led_level, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)
    
  if num == '1':
# number 1_bottom_left - HUMIDITY
    ap.set_pixel(4, 4, 0, 0, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, led_level, 0)   
    ap.set_pixel(5, 6, 0, led_level, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, 0, 0)   
    ap.set_pixel(6, 5, 0, 0, 0)   
    ap.set_pixel(6, 6, 0, 0, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)
    
  if num == '2':
# number 2_bot_left - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, 0, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, led_level, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, 0, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '3':
# number 3_bot_left - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, 0, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, led_level, 0)   
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '4':
# number 4_bot_left - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, led_level, 0)   
    ap.set_pixel(4, 7, 0, 0, 0)
    ap.set_pixel(5, 4, 0, 0, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, led_level, 0)   
    ap.set_pixel(5, 7, 0, 0, 0)
    ap.set_pixel(6, 4, 0, 0, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '5':
# number 5_bot_left - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, led_level, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, 0, 0)   
    ap.set_pixel(6, 6, 0, 0, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '6':
# number 6_bot_left - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, led_level, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, 0, 0)   
    ap.set_pixel(5, 5, 0, led_level, 0)   
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, 0, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '7':
# number 7_bot_left - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, 0, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, 0, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '8':
# number 8_bot_left - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, led_level, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, led_level, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '9':
# number 9_bot_left - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, led_level, 0)   
    ap.set_pixel(4, 7, 0, 0, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, led_level, 0)   
    ap.set_pixel(5, 7, 0, 0, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)
	
def hum_num_error_high():
# error state warning for - HIGH HUMIDITY
    ap.set_pixel(0, 4, red, 0, 0)   
    ap.set_pixel(0, 5, red, 0, 0)   
    ap.set_pixel(0, 6, red, 0, 0)   
    ap.set_pixel(0, 7, red, 0, 0)
    ap.set_pixel(1, 4, red, 0, 0)   
    ap.set_pixel(1, 5, red, 0, 0)   
    ap.set_pixel(1, 6, red, 0, 0)   
    ap.set_pixel(1, 7, red, 0, 0)
    ap.set_pixel(2, 4, red, 0, 0)   
    ap.set_pixel(2, 5, red, 0, 0)   
    ap.set_pixel(2, 6, red, 0, 0)   
    ap.set_pixel(2, 7, red, 0, 0)
    ap.set_pixel(3, 4, red, 0, 0)   
    ap.set_pixel(3, 5, red, 0, 0)   
    ap.set_pixel(3, 6, red, 0, 0)   
    ap.set_pixel(3, 7, red, 0, 0)
    ap.set_pixel(4, 4, red, 0, 0)   
    ap.set_pixel(4, 5, red, 0, 0)   
    ap.set_pixel(4, 6, red, 0, 0)   
    ap.set_pixel(4, 7, red, 0, 0)
    ap.set_pixel(5, 4, red, 0, 0)   
    ap.set_pixel(5, 5, red, 0, 0)   
    ap.set_pixel(5, 6, red, 0, 0)   
    ap.set_pixel(5, 7, red, 0, 0)
    ap.set_pixel(6, 4, red, 0, 0)   
    ap.set_pixel(6, 5, red, 0, 0)   
    ap.set_pixel(6, 6, red, 0, 0)   
    ap.set_pixel(6, 7, red, 0, 0)
    ap.set_pixel(7, 4, red, 0, 0)   
    ap.set_pixel(7, 5, red, 0, 0)   
    ap.set_pixel(7, 6, red, 0, 0)   
    ap.set_pixel(7, 7, red, 0, 0)
   	
def hum_num_error_low():
# error state warning for - LOW HUMIDITY
    ap.set_pixel(0, 4, 0, 0, blue)   
    ap.set_pixel(0, 5, 0, 0, blue)   
    ap.set_pixel(0, 6, 0, 0, blue)   
    ap.set_pixel(0, 7, 0, 0, blue)
    ap.set_pixel(1, 4, 0, 0, blue)   
    ap.set_pixel(1, 5, 0, 0, blue)   
    ap.set_pixel(1, 6, 0, 0, blue)   
    ap.set_pixel(1, 7, 0, 0, blue)
    ap.set_pixel(2, 4, 0, 0, blue)   
    ap.set_pixel(2, 5, 0, 0, blue)   
    ap.set_pixel(2, 6, 0, 0, blue)   
    ap.set_pixel(2, 7, 0, 0, blue)
    ap.set_pixel(3, 4, 0, 0, blue)   
    ap.set_pixel(3, 5, 0, 0, blue)   
    ap.set_pixel(3, 6, 0, 0, blue)   
    ap.set_pixel(3, 7, 0, 0, blue)
    ap.set_pixel(4, 4, 0, 0, blue)   
    ap.set_pixel(4, 5, 0, 0, blue)   
    ap.set_pixel(4, 6, 0, 0, blue)   
    ap.set_pixel(4, 7, 0, 0, blue)
    ap.set_pixel(5, 4, 0, 0, blue)   
    ap.set_pixel(5, 5, 0, 0, blue)   
    ap.set_pixel(5, 6, 0, 0, blue)   
    ap.set_pixel(5, 7, 0, 0, blue)
    ap.set_pixel(6, 4, 0, 0, blue)   
    ap.set_pixel(6, 5, 0, 0, blue)   
    ap.set_pixel(6, 6, 0, 0, blue)   
    ap.set_pixel(6, 7, 0, 0, blue)
    ap.set_pixel(7, 4, 0, 0, blue)   
    ap.set_pixel(7, 5, 0, 0, blue)   
    ap.set_pixel(7, 6, 0, 0, blue)   
    ap.set_pixel(7, 7, 0, 0, blue)

    
## PRESSURE NUMBERS MATRIX BELOW # 

def psi_num_matrix_1(num):

  if num == '0':
# number 0_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, led_level)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '1':
# number 1_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, 0)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, led_level)   
    ap.set_pixel(1, 2, 0, 0, led_level)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, 0)   
    ap.set_pixel(2, 1, 0, 0, 0)   
    ap.set_pixel(2, 2, 0, 0, 0)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '2':
# number 2_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, led_level)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, 0)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '3':
# number 3_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, led_level)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '4':
# number 4_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, led_level)   
    ap.set_pixel(0, 3, 0, 0, 0)
    ap.set_pixel(1, 0, 0, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, led_level)   
    ap.set_pixel(1, 3, 0, 0, 0)
    ap.set_pixel(2, 0, 0, 0, 0)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '5':
# number 5_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, led_level)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, 0)   
    ap.set_pixel(2, 2, 0, 0, 0)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '6':
# number 6_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, led_level)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, led_level)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, 0)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '7':
# number 7_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, 0)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, 0)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '8':
# number 8_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, led_level)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, led_level)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '9':
# number 9_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, led_level)   
    ap.set_pixel(0, 3, 0, 0, 0)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, led_level)   
    ap.set_pixel(1, 3, 0, 0, 0)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

def psi_num_matrix_2(num):

  if num == '0':
# number 0_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, led_level)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '1':
    # number 1_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, 0)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, led_level)   
    ap.set_pixel(5, 2, 0, 0, led_level)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, 0)   
    ap.set_pixel(6, 1, 0, 0, 0)   
    ap.set_pixel(6, 2, 0, 0, 0)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '2':
# number 2_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, led_level)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, 0)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '3':
# number 3_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, led_level)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '4':
# number 4_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, led_level)   
    ap.set_pixel(4, 3, 0, 0, 0)
    ap.set_pixel(5, 0, 0, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, led_level)   
    ap.set_pixel(5, 3, 0, 0, 0)
    ap.set_pixel(6, 0, 0, 0, 0)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '5':
# number 5_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, led_level)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, 0)   
    ap.set_pixel(6, 2, 0, 0, 0)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '6':
# number 6_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, led_level)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, led_level)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, 0)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '7':
# number 7_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, 0)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, 0, 0, 0)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '8':
# number 8_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, led_level)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, led_level)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '9':
# number 9_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, led_level)   
    ap.set_pixel(4, 3, 0, 0, 0)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, led_level)   
    ap.set_pixel(5, 3, 0, 0, 0)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

def psi_num_matrix_3(num):

  if num == '0':
# number 0_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, led_level)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '1':
    # number 1_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, 0)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, led_level)   
    ap.set_pixel(1, 6, 0, 0, led_level)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, 0)   
    ap.set_pixel(2, 5, 0, 0, 0)   
    ap.set_pixel(2, 6, 0, 0, 0)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '2':
# number 2_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, led_level)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, 0)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '3':
# number 3_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, led_level)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '4':
# number 4_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, led_level)   
    ap.set_pixel(0, 7, 0, 0, 0)
    ap.set_pixel(1, 4, 0, 0, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, led_level)   
    ap.set_pixel(1, 7, 0, 0, 0)
    ap.set_pixel(2, 4, 0, 0, 0)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '5':
# number 5_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, led_level)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, 0)   
    ap.set_pixel(2, 6, 0, 0, 0)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '6':
# number 6_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, led_level)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, 0)   
    ap.set_pixel(1, 5, 0, 0, led_level)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, 0)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '7':
# number 7_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, 0, 0)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, 0, 0)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '8':
# number 8_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, led_level)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, led_level)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '9':
# number 9_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, led_level)   
    ap.set_pixel(0, 7, 0, 0, 0)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, led_level)   
    ap.set_pixel(1, 7, 0, 0, 0)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

def psi_num_matrix_4(num):

  if num == '0':
# number 0_bottom_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, led_level)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '1':
    # number 1_bottom_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, 0)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, led_level)   
    ap.set_pixel(5, 6, 0, 0, led_level)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, 0)   
    ap.set_pixel(6, 5, 0, 0, 0)   
    ap.set_pixel(6, 6, 0, 0, 0)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '2':
# number 2_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, led_level)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, 0)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '3':
# number 3_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, led_level)   
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '4':
# number 4_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, led_level)   
    ap.set_pixel(4, 7, 0, 0, 0)
    ap.set_pixel(5, 4, 0, 0, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, led_level)   
    ap.set_pixel(5, 7, 0, 0, 0)
    ap.set_pixel(6, 4, 0, 0, 0)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '5':
# number 5_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, led_level)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, 0)   
    ap.set_pixel(6, 6, 0, 0, 0)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '6':
# number 6_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, led_level)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, 0)   
    ap.set_pixel(5, 5, 0, 0, led_level)   
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, 0)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '7':
# number 7_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, 0, 0)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, 0)
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, 0, 0)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '8':
# number 8_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, led_level)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, led_level)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '9':
# number 9_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, led_level)   
    ap.set_pixel(4, 7, 0, 0, 0)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, led_level)   
    ap.set_pixel(5, 7, 0, 0, 0)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)
	
def psi_num_error_high():
# error state warning for - HIGH PRESSURE
    ap.set_pixel(0, 0, red, 0, 0)   
    ap.set_pixel(0, 1, red, 0, 0)   
    ap.set_pixel(0, 2, red, 0, 0)   
    ap.set_pixel(0, 3, red, 0, 0)
    ap.set_pixel(1, 0, red, 0, 0)   
    ap.set_pixel(1, 1, red, 0, 0)   
    ap.set_pixel(1, 2, red, 0, 0)   
    ap.set_pixel(1, 3, red, 0, 0)
    ap.set_pixel(2, 0, red, 0, 0)   
    ap.set_pixel(2, 1, red, 0, 0)   
    ap.set_pixel(2, 2, red, 0, 0)   
    ap.set_pixel(2, 3, red, 0, 0)
    ap.set_pixel(3, 0, red, 0, 0)   
    ap.set_pixel(3, 1, red, 0, 0)   
    ap.set_pixel(3, 2, red, 0, 0)   
    ap.set_pixel(3, 3, red, 0, 0)
    ap.set_pixel(4, 0, red, 0, 0)   
    ap.set_pixel(4, 1, red, 0, 0)   
    ap.set_pixel(4, 2, red, 0, 0)   
    ap.set_pixel(4, 3, red, 0, 0)
    ap.set_pixel(5, 0, red, 0, 0)   
    ap.set_pixel(5, 1, red, 0, 0)   
    ap.set_pixel(5, 2, red, 0, 0)   
    ap.set_pixel(5, 3, red, 0, 0)
    ap.set_pixel(6, 0, red, 0, 0)   
    ap.set_pixel(6, 1, red, 0, 0)   
    ap.set_pixel(6, 2, red, 0, 0)   
    ap.set_pixel(6, 3, red, 0, 0)
    ap.set_pixel(7, 0, red, 0, 0)   
    ap.set_pixel(7, 1, red, 0, 0)   
    ap.set_pixel(7, 2, red, 0, 0)   
    ap.set_pixel(7, 3, red, 0, 0)
    ap.set_pixel(0, 4, red, 0, 0)   
    ap.set_pixel(0, 5, red, 0, 0)   
    ap.set_pixel(0, 6, red, 0, 0)   
    ap.set_pixel(0, 7, red, 0, 0)
    ap.set_pixel(1, 4, red, 0, 0)   
    ap.set_pixel(1, 5, red, 0, 0)   
    ap.set_pixel(1, 6, red, 0, 0)   
    ap.set_pixel(1, 7, red, 0, 0)
    ap.set_pixel(2, 4, red, 0, 0)   
    ap.set_pixel(2, 5, red, 0, 0)   
    ap.set_pixel(2, 6, red, 0, 0)   
    ap.set_pixel(2, 7, red, 0, 0)
    ap.set_pixel(3, 4, red, 0, 0)   
    ap.set_pixel(3, 5, red, 0, 0)   
    ap.set_pixel(3, 6, red, 0, 0)   
    ap.set_pixel(3, 7, red, 0, 0)
    ap.set_pixel(4, 4, red, 0, 0)   
    ap.set_pixel(4, 5, red, 0, 0)   
    ap.set_pixel(4, 6, red, 0, 0)   
    ap.set_pixel(4, 7, red, 0, 0)
    ap.set_pixel(5, 4, red, 0, 0)   
    ap.set_pixel(5, 5, red, 0, 0)   
    ap.set_pixel(5, 6, red, 0, 0)   
    ap.set_pixel(5, 7, red, 0, 0)
    ap.set_pixel(6, 4, red, 0, 0)   
    ap.set_pixel(6, 5, red, 0, 0)   
    ap.set_pixel(6, 6, red, 0, 0)   
    ap.set_pixel(6, 7, red, 0, 0)
    ap.set_pixel(7, 4, red, 0, 0)   
    ap.set_pixel(7, 5, red, 0, 0)   
    ap.set_pixel(7, 6, red, 0, 0)   
    ap.set_pixel(7, 7, red, 0, 0)
	
def psi_num_error_low():
# error state warning for - LOW PRESSURE
    ap.set_pixel(0, 0, 0, 0, blue)   
    ap.set_pixel(0, 1, 0, 0, blue)   
    ap.set_pixel(0, 2, 0, 0, blue)   
    ap.set_pixel(0, 3, 0, 0, blue)
    ap.set_pixel(1, 0, 0, 0, blue)   
    ap.set_pixel(1, 1, 0, 0, blue)   
    ap.set_pixel(1, 2, 0, 0, blue)   
    ap.set_pixel(1, 3, 0, 0, blue)
    ap.set_pixel(2, 0, 0, 0, blue)   
    ap.set_pixel(2, 1, 0, 0, blue)   
    ap.set_pixel(2, 2, 0, 0, blue)   
    ap.set_pixel(2, 3, 0, 0, blue)
    ap.set_pixel(3, 0, 0, 0, blue)   
    ap.set_pixel(3, 1, 0, 0, blue)   
    ap.set_pixel(3, 2, 0, 0, blue)   
    ap.set_pixel(3, 3, 0, 0, blue)
    ap.set_pixel(4, 0, 0, 0, blue)   
    ap.set_pixel(4, 1, 0, 0, blue)   
    ap.set_pixel(4, 2, 0, 0, blue)   
    ap.set_pixel(4, 3, 0, 0, blue)
    ap.set_pixel(5, 0, 0, 0, blue)   
    ap.set_pixel(5, 1, 0, 0, blue)   
    ap.set_pixel(5, 2, 0, 0, blue)   
    ap.set_pixel(5, 3, 0, 0, blue)
    ap.set_pixel(6, 0, 0, 0, blue)   
    ap.set_pixel(6, 1, 0, 0, blue)   
    ap.set_pixel(6, 2, 0, 0, blue)   
    ap.set_pixel(6, 3, 0, 0, blue)
    ap.set_pixel(7, 0, 0, 0, blue)   
    ap.set_pixel(7, 1, 0, 0, blue)   
    ap.set_pixel(7, 2, 0, 0, blue)   
    ap.set_pixel(7, 3, 0, 0, blue)
    ap.set_pixel(0, 4, 0, 0, blue)   
    ap.set_pixel(0, 5, 0, 0, blue)   
    ap.set_pixel(0, 6, 0, 0, blue)   
    ap.set_pixel(0, 7, 0, 0, blue)
    ap.set_pixel(1, 4, 0, 0, blue)   
    ap.set_pixel(1, 5, 0, 0, blue)   
    ap.set_pixel(1, 6, 0, 0, blue)   
    ap.set_pixel(1, 7, 0, 0, blue)
    ap.set_pixel(2, 4, 0, 0, blue)   
    ap.set_pixel(2, 5, 0, 0, blue)   
    ap.set_pixel(2, 6, 0, 0, blue)   
    ap.set_pixel(2, 7, 0, 0, blue)
    ap.set_pixel(3, 4, 0, 0, blue)   
    ap.set_pixel(3, 5, 0, 0, blue)   
    ap.set_pixel(3, 6, 0, 0, blue)   
    ap.set_pixel(3, 7, 0, 0, blue)
    ap.set_pixel(4, 4, 0, 0, blue)   
    ap.set_pixel(4, 5, 0, 0, blue)   
    ap.set_pixel(4, 6, 0, 0, blue)   
    ap.set_pixel(4, 7, 0, 0, blue)
    ap.set_pixel(5, 4, 0, 0, blue)   
    ap.set_pixel(5, 5, 0, 0, blue)   
    ap.set_pixel(5, 6, 0, 0, blue)   
    ap.set_pixel(5, 7, 0, 0, blue)
    ap.set_pixel(6, 4, 0, 0, blue)   
    ap.set_pixel(6, 5, 0, 0, blue)   
    ap.set_pixel(6, 6, 0, 0, blue)   
    ap.set_pixel(6, 7, 0, 0, blue)
    ap.set_pixel(7, 4, 0, 0, blue)   
    ap.set_pixel(7, 5, 0, 0, blue)   
    ap.set_pixel(7, 6, 0, 0, blue)   
    ap.set_pixel(7, 7, 0, 0, blue)

   
## SETTING UP FLIGHT BUTTONS FOR USE AND ASSIGNING COMMANDS
   
def button_pressed(button):             ## CONTINUOUSLY MONITORS FOR BUTTON EVENTS
    global running
    global ap
    global led_level
    global temp_hum_on
    global psi_on
    global tmp_mute
    global hum_mute
    global alarm_count
    
    if button == UP and led_level < 250:    ## ADJUST LED MATRIX BRIGHTNESS - UP
        led_level = led_level + 10

    if button == DOWN and led_level > 40:   ## ADJUST LED MATRIX BRIGHTNESS - DOWN
        led_level = led_level - 10

    if button == LEFT:                  ## FORCE TEMPERATURE AND HUMIDITY PAGE ON (5s)
        temp_hum_on = 1                 
        
        temp_num_matrix_1(temp[0])      ## FIRST DIGIT - TEMPERATURE
        temp_num_matrix_2(temp[1])      ## SECOND DIGIT - TEMPERATURE
        hum_num_matrix_1(hum[0])        ## FIRST DIGIT - HUMIDITY
        hum_num_matrix_2(hum[1])        ## SECOND DIGIT - HUMIDITY
        
        time.sleep(5.0)                 ## WAIT 5 SECONDS TO ENSURE READING CAN BE RECORDED
        
        temp_hum_on = 0                 ## CLOSE TEMPERATURE AND HUMIDITY PAGE OFF
        
        tmp_mute = 0                    ## SHOWS THE WARNING FOR TEMPERATURE
        hum_mute = 0                    ## SHOWS THE WARNING FOR HUMIDITY
        
    if button == RIGHT:                 ## FORCE PRESSURE PAGE ON (5s)
        psi_on = 1                      
        
        psi_num_matrix_1(psi[0])        ## FIRST DIGIT - PRESSURE
        psi_num_matrix_2(psi[1])        ## SECOND DIGIT - PRESSURE
        psi_num_matrix_3(psi[2])        ## THIRD DIGIT - PRESSURE
        psi_num_matrix_4(psi[3])        ## FOURTH DIGIT - PRESSURE
        
        time.sleep(5.0)                 ## WAIT 5 SECONDS TO ENSURE READING CAN BE RECORDED
        
        psi_on = 0                      ## FORCE PRESSURE PAGE OFF
        
    if button == A:                     ## ALLOWS ASTRONAUT (Tim) TO MUTE ALARMS
        alarm_count = 0                 # RESETS 'alarm_count' TO ZERO TO START COUNTDOWN
        tmp_mute = 1                    # MUTES THE WARNING FOR TEMPERATURE
        hum_mute = 1                    # MUTES THE WARNING FOR HUMIDITY
        psi_mute = 1                    # MUTES THE WARNING FOR PRESSURE
        
    if button == B:
        alarm_count = 0                 # RESETS 'alarm_count' TO ZERO TO START COUNTDOWN
        tmp_mute = 0                    # SHOWS THE WARNING FOR TEMPERATURE
        hum_mute = 0                    # SHOWS THE WARNING FOR HUMIDITY
        psi_mute = 0                    # SHOWS THE WARNING FOR PRESSURE
                
for pin in [UP, DOWN, LEFT, RIGHT, A, B]:## SETUP GPIP PIN VALUES
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=button_pressed, bouncetime=500)
   
   
## SET PREVIOUS TEMPERATURE, HUMIDITY, & PRESSURE VALUES TO ZERO  ##

temp_prev = 0                           # PREVIOUS TEMPERATURE READING
temp_int = 0                            # CURRENT TEMPERATURE READING
hum_prev = 0                            # PREVIOUS HUMIDITY READING
hum_int = 0                             # CURRENT HUMIDITY READING
psi_prev = 0                            # PREVIOUS PRESSURE READING
psi_int = 0                             # CURRENT PRESSURE READING
pitch = 0                               # CURRENT PITCH (ORIENTATION) READING
roll = 0                                # CURRENT ROLL (ORIENTATION) READING
yaw = 0                                 # CURRENT YAW (ORIENTATION) READING

sec_count = 0                           # CURRENT TRIGGER READING FOR RECORDING RESULTS INTO LOG

alarm_count = 0                         # TRIGGER FOR RE-ENABLING ALARM AFTER A SET PERIOD OF TIME
alarm_timer = 0

## NEW ASTROPI CLASS FILE TO ENSURE ORIENTATION READING IS DISPLAYED CORRECTLY ##

ap = AstroPi()

class AstroPiContinuous(AstroPi):       # NEW CLASS FILE WRITEN BY 'LetHopeItsSnowing' (ASTROPI FORUM)
    """
    A class which continuously reads orientation data from AstroPi as without
    it the orientatin data looses sync
    """
    def __init__(self,
            fb_device='/dev/fb1',
            imu_settings_file='RTIMULib',
            text_assets='astro_pi_text',
            sample_rate = 0.1):

        AstroPi.__init__(self, fb_device, imu_settings_file, text_assets)
       
        self.sample_rate = sample_rate
        self.stopped = True
        self.running = False
           
    def start(self):
        """
        starts the thread that continuously reads the astro pi orientation data
        """
        #initialise the IMU by getting the orientation
        self.get_orientation()
        #start the orientation thread
        thread.start_new_thread(self._get_orientation_threaded, ())
           
    def _get_orientation_threaded(self):
        """
        reads the orientation data every sample rate to ensure astro pi is kept in sync
        """
        self.stopped = False
        self.running = True

        #keep reading the orientation data, this keeps AstroPi in sync
        while(not self.stopped):
            self.get_orientation()
            sleep(self.sample_rate)
               
        self.running = False
       
    def stop(self):
        """
        stops the continous read thread
        """
        self.stopped = True
        #wait for the thread to stop
        while(self.running):
            sleep(0.01)
               
    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.stop()

        
## NEW CLASS FILE TO ALLOW CPU_TEMP TO BE RECALLED AS NEEDED ##
        
class CPUTemp:
    def __init__(self, tempfilename = "/sys/class/thermal/thermal_zone0/temp"):
        self.tempfilename = tempfilename

    def __enter__(self):
        self.open()
        return self

    def open(self):
        self.tempfile = open(self.tempfilename, "r")
    
    def read(self):
        self.tempfile.seek(0)
        return self.tempfile.read().rstrip()

    def get_temperature(self):
        return self.get_temperature_in_c()

    def get_temperature_in_c(self):
        tempraw = self.read()
        return float(tempraw[:-3] + "." + tempraw[-3:])

    def get_temperature_in_f(self):
        return self.convert_c_to_f(self.get_temperature_in_c())
    
    def convert_c_to_f(self, c):
        return c * 9.0 / 5.0 + 32.0

    def __exit__(self, type, value, traceback):
        self.close()
            
    def close(self):
        self.tempfile.close()

        
## MAIN PROGRAM LOOP ##
  
try:  
  while running:                        ## ENSURES THAT THE SCRIPT IS ALWAYS RUNNING IN A LOOP
    import thread                       ## ALLOWS THE SCRIPT TO IMPORT THE NEW CLASS FILE
    with AstroPiContinuous() as ap:     ## FORCES SYSTEM TO USE NEW ORIENTATION CLASS FILE
        while(True):                    ## SCRIPT LOOP FOR DISPLAYING READINGS AND RECORDING DATA
            o = ap.get_orientation()
            pitch = o["pitch"]          # SEPARATES OUT THE PITCH SECTION FROM ORIENTATION READINGS
            roll = o["roll"]            # SEPARATES OUT THE ROLL SECTION FROM ORIENTATION READING
            yaw = o["yaw"]              # SEPARATES OUT THE YAW SECTION FROM ORIENTATION READING
            
            
            ## ALLOWS THE LOG SECTION TO RECALL INFORMATION FROM THE VARIOUS SECTIONS OF THIS SCRIPT
            
            global display_f
            global temp_f
            global temp_reading_f
            global temp_alarm_f
            global hum_f
            global hum_reading_f
            global hum_alarm_f
            global psi_f
            global psi_reading_f
            global psi_alarm_f
                   
        
            ## SET VALUES FOR LOGGING INFORMATION ##
   
            if sec_count == 15:          ## ONLY WRITES THE LOGGING INFORMATION EVERY 30 SECONDS

                print("Logged {}".format(count))  #KEEPS ASTRONAUT (Tim) UP TO DATE WITH READINGS RECORDED
                file.write("\"{}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\"\n".format(asctime(),display_f,temp_f,tmp_reading_f,tmp_alarm_f,hum_f,hum_reading_f,hum_alarm_f,psi_f,psi_reading_f,psi_alarm_f,pitch,roll,yaw))
                sec_count = 0 
                count+=1
                alarm_timer = alarm_timer + 1     # ADDS 1 TO THE 'alarm_timer' TRIGGER

                
            ## RE-ENABLE ALARMS FOR THE TEMPERATURE, HUMIDITY AND PRESSURE READINGS 
            
            if alarm_count == 35:        ## WAITS FOR 30mins (APPROX.) BEFORE RE-ENABLING ALARMS
                tmp_mute = 0
                hum_mute = 0
                psi_mute = 0
                alarm_count = 0          # RESETS 'alarm_count' TO ZERO TO START COUNTDOWN AGAIN
                
            elif alarm_timer >= 5:
                alarm_count+=1           # ONCE 'alarm_timer' EQUALS 5, ADDS ONE TO 'alarm_count',
                alarm_timer = 0          # THIS ENSURES THE TIMERS ARE CLEARED ON A BUTTON PRESS
            
            
            ## CALCULATIONS FOR TEMPERATURE TO COMPENSATE FOR CPU_TEMP AFFECTING TEMPERATURE READINGS
            
            t = ap.get_temperature()
            p = ap.get_temperature_from_pressure()
            h = ap.get_temperature_from_humidity()
            with CPUTemp() as cpu_temp:
                c = cpu_temp.get_temperature()
    
            temp_calc = ((t+p+h)/3) - (c/4)
    
  
            ## GET TEMPERATURE, HUMIDITY, & PRESSURE READINGS FROM ASTROPI SENSORS ##
            ## also CREATES INTERGAR FOR LOGGING INFORMATION CORRECTLY ON A TABLE ##
 
            temp_f = temp_calc              ## STORES TEMPERATURE READING WITHIN temp_f
            temp_int = int(temp_f)          ## CREATES INTERGAR FROM TEMPERATURE READING
 
            hum_f = ap.get_humidity()       ## STORES TEMPERATURE READING WITHIN hum_f                
            hum_int = int(hum_f)            ## CREATES INTERGAR FROM HUMIDITY READING
 
            psi_f = ap.get_pressure()       ## STORES TEMPERATURE READING WITHIN psi_f
            psi_int = int(psi_f)            ##CREATES INTERGAR FROM PRESSURE READING
        
    
            ## LOG IF THE DISPLAY HAS BEEN MUTED (BLACK BOX STYLE) ##
    
            if led_level < 50:              # DOUBLE CHECK LED LIGHT LEVELS TO CONFIRM DISPLAY ACTIVE
                display_mute = 1
            elif led_level > 40:
                display_mute = 0
            
            if display_mute == 1:           # TRANSLATES DISPLAY MUTE TO ON AND OFF FOR LOG FILE
                display_f = 0
            elif display_mute == 0:
                display_f = 1
    
    
            ## LOG IF THE TEMPERATURE ALARM READING AND IF IT HAS BEEN MUTED (BLACK BOX STYLE) ##
    
            if tmp_mute == 1:               # TRANSLATES THE ALARM MUTE INTO ON AND OFF FOR LOG FILE
                tmp_alarm_f = 0
            elif tmp_mute == 0:
                tmp_alarm_f = 1
        
            if tmp_alarm == 2:              # TRANSLATES THE READINGS INTO HIGH, LOW AND OK FOR LOG FILE
                tmp_reading_f = 1
            elif tmp_alarm == 1:
                tmp_reading_f = -1
            elif tmp_alarm == 0:
                tmp_reading_f = 0 

                    
            ## LOG IF THE HUMIDITY ALARM READING AND IF IT HAS BEEN MUTED (BLACK BOX STYLE)  ##
    
            if hum_mute == 1:               # TRANSLATES THE ALARM MUTE INTO ON AND OFF FOR LOG FILE
                hum_alarm_f = 0
            elif hum_mute == 0:
                hum_alarm_f = 1
        
            if hum_alarm == 2:              # TRANSLATES THE READINGS INTO HIGH, LOW AND OK FOR LOG FILE
                hum_reading_f = 1
            elif hum_alarm == 1:
                hum_reading_f = -1
            elif hum_alarm == 0:
                hum_reading_f = 0
    
    
            ## LOG IF THE PRESSURE ALARM READING AND IF IT HAS BEEN MUTED (BLACK BOX STYLE)
    
            if psi_mute == 1:               # TRANSLATES THE ALARM MUTE INTO ON AND OFF FOR LOG FILE
                psi_alarm_f = 0
            elif psi_mute == 0:
                psi_alarm_f = 1
        
            if psi_alarm == 2:              # TRANSLATES THE READINGS INTO HIGH, LOW AND OK FOR LOG FILE
                psi_reading_f = 1
            elif psi_alarm == 1:
                psi_reading_f = -1
            elif psi_alarm == 0:
                psi_reading_f = 0
                

            ## CONVERTS TEMPERATURE, HUMIDITY, PRESSURE READINGS TO A STRING ## 
            ## also OVERWRITES AND STORES SENSOR READINGS WITHIN PREVIOUS READINGS ##

            temp_prev = temp_int            # STORE READING IN temp_prev
            temp =  str(temp_int)           # CONVERT TEMPERATURE READING TO STRING ##

            hum_prev = hum_int              # STORE READING IN temp_prev
            hum =  str(hum_int)             # CONVERT HUMIDITY READING TO STRING ##

            psi_prev = psi_int              # STORE READING IN temp_prev
            psi =  str(psi_int)             # CONVERT PRESSURE READING TO STRING ##
 
 
 
 
            ## ROTATE THE LED MATRIX DISPLAY (if required) ##
    
            ap.set_rotation(270)           ## ROTATION ENABLED TO WORK WITH ASTROPI NASA CASE
 
 
            ## WRITES VALUES ONTO THE LED MATRIX FOR THE TEMPERATURE, HUMIDITY, & PRESSURE ##
        
            ## WRITES TO TOP_LINE ONLY - TEMPERATURE (2 DIGITS)##
    
            temp_num_matrix_1(temp[0])          # FIRST DIGIT - TEMPERATURE
            temp_num_matrix_2(temp[1])          # SECOND DIGIT - TEMPERATURE
    
    
            ## WRITE TO BOTTOM_LINE ONLY - HUMIDITY (2 DIGITS)##
    
            hum_num_matrix_1(hum[0])            # FIRST DIGIT - HUMIDITY
            hum_num_matrix_2(hum[1])            # SECOND DIGIT - HUMIDITY
 
    
            ## TEMPERATURE - ERROR STATE CHECKING ##    
    
            if temp_hum_on == 1:                # IF TEMP+HUMIDITY PAGE ACTIVE DISPLAY PREVIOUS READING FOR 5s
                time.sleep(5.0)
            elif temp_hum_on == 0:
                time.sleep(0.5)                 # IF NOT ONLY WAIT FOR 0.5s
      
            if tmp_mute == 0:                   # ONLY WORKOUT ALARM STATES FOR READINGS WITHIN TEMPERATURE IF NOT MUTED
                if temp_int - 5 > temp_prev:    # IF RISE OF 5 DEGREES BETWEEN READING - ALARM STATE
                    temp_num_error_high()
                    t_h_wait = 1
                    tmp_alarm = 2
        
                elif temp_int + 5 < temp_prev:  # IF FALL OF 5 DEGREES BETWEEN READING - ALARM STATE
                    temp_num_error_low()
                    t_h_wait = 1
                    tmp_alarm = 1
        
                elif temp_int > 36:             ## CHECKED AGAINST ISS REQUIREMENTS INC CPU READING
                    temp_num_error_high()
                    t_h_wait = 1
                    tmp_alarm = 2
        
                elif temp_int < 18:             ## CHECKED AGAINST ISS REQUIREMENTS INC CPU READING
                    temp_num_error_low()
                    t_h_wait = 1
                    tmp_alarm = 1
    
                else:
                    t_h_wait = 1                # IF NOTHING MATCHES WAIT ANOTHER 0.5s BEFORE MOVING FORWARD
                    tmp_alarm = 0
        
    
            ## HUMIDITY - ERROR STATE CHECKING ## 
    
            if hum_mute == 0:                   # ONLY WORKOUT ALARM STATES FOR READINGS WITHIN HUMIDITY IF NOT MUTED
                if hum_int - 5 > hum_prev:      # IF RISE OF 5 BETWEEN READING - ALARM STATE
                    hum_num_error_high()
                    t_h_wait = 1
                    hum_alarm = 2
        
                elif hum_int + 5 < hum_prev:    # IF FALL OF 5 BETWEEN READING - ALARM STATE
                    hum_num_error_low()
                    t_h_wait = 1
                    hum_alarm = 1
        
                elif hum_int > 60:              ## MUST BE CHECKED AGAINST ISS REQUIREMENTS
                    hum_num_error_high()
                    t_h_wait = 1
                    hum_alarm = 2
        
                elif hum_int < 40:              ## MUST BE CHECKED AGAINST ISS REQUIREMENTS
                    hum_num_error_low()
                    t_h_wait = 1
                    hum_alarm = 1
        
                else:
                    t_h_wait = 1                # IF NOTHING MATCHES WAIT ANOTHER 0.5s BEFORE MOVING FORWARD
                    hum_alarm = 0

        
            ## ALLOW ASTRONAUT (Tim) TO READ THE PREVIOUS TEMPERATURE & HUMIDITY READINGS ON LED MATRIX ##
    
            if t_h_wait == 1:
                time.sleep(0.5)
            else:
                time.sleep(0.5)


            ## WRITE TO BOTH TOP_LINE & BOTTOM_LINE - PRESSURE (4 DIGITS) ##
    
            psi_num_matrix_1(psi[0])            # FIRST DIGIT - PRESSURE
            psi_num_matrix_2(psi[1])            # SECOND DIGIT - PRESSURE
            psi_num_matrix_3(psi[2])            # THIRD DIGIT - PRESSURE
            psi_num_matrix_4(psi[3])            # FOURTH DIGIT - PRESSURE

    
            ## PRESSURE - ERROR STATE CHECKING ##
    
            if psi_on == 1:                     # IF PRESSURE PAGE ACTIVE DISPLAY PREVIOUS READING FOR 5s
                time.sleep(5.0)
            elif psi_on == 0:
                time.sleep(0.5)                 # IF NOT ONLY WAIT FOR 0.5s
        
            if psi_int - 5 > psi_prev:          # ONLY WORKOUT ALARM STATES FOR READINGS WITHIN PRESSURE IF NOT MUTED
                psi_num_error_high()            # IF RISE OF 5 BETWEEN READING - ALARM STATE
                psi_wait = 1
                psi_alarm = 2
        
            elif psi_int + 5 < psi_prev:        # IF FALL OF 5 BETWEEN READING - ALARM STATE
                psi_num_error_low()
                psi_wait = 1
                psi_alarm = 1
        
            elif psi_int > 1040:                ## MUST BE CHECKED AGAINST ISS REQUIREMENTS
                psi_num_error_high()
                psi_wait = 1
                psi_alarm = 2
        
            elif psi_int < 1000:                ## MUST BE CHECKED AGAINST ISS REQUIREMENTS
                psi_num_error_low()
                psi_wait = 1
                psi_alarm = 1
        
            else:        
                psi_wait = 1
                psi_alarm = 0
    
    
            ## ALLOW ASTRONAUT (Tim) TO READ THE PREVIOUS PRESSURE READING ON LED MATRIX ##
    
            if psi_wait == 1:
                time.sleep(0.5)
            else:
                time.sleep(0.5)

        
            ## RESETS THE LOGGING COUNTER & START LOOP AGAIN ##

            sec_count+=1                    ## ADD 1 TO SEC_COUNT FOR LOGGING
    
	
## PROGRAMMIG TO CLEANLY EXIT THE PYTHON PROGRAM AND STOP RECORDING READINGS (if required) ##
    
finally:

    ## CLEARS THE LED MATRIX ON ASTROPI ##
    
    file.close()                    ## CLOSE CSV FILE TO ENSURE READINGS ARE RECORDED
    
    ap.show_letter(    " ", back_colour = [0, 0, 0])    ## SETS BACKGROUND COLOUR TO BLACK (off)
    
    ap.clear                        ## CLEARS LED MATRIX

    os.system("clear")              ## CLEARS THE SSH DISPLAY

    sys.exit()                      ## FORCES THE PYTHON PROGRAM TO EXIT