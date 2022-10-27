# https://github.com/dafvid/micropython-bmp280

# import the required libraries
from bmp280 import *
from machine import Pin, I2C
import utime
from time import sleep
from I2C_LCD import I2CLcd

def check_devices(device_list):
    if devices == []:
        print("No i2c device !")
    else:
        print('i2c devices found:', len(device_list))
     
    for device in device_list:  
        print("Decimal address: ", device," | Hex address: ", hex(device))

# Function for calculation altitude from pressure and temperature values
# because altitude() method is not present in the Library

def altitude_HYP(hPa , temperature):
    # Hypsometric Equation (Max Altitude < 11 Km above sea level)
    temperature = temperature
    local_pressure = hPa
    sea_level_pressure = 1013.25 # hPa      
    pressure_ratio = sea_level_pressure/local_pressure # sea level pressure = 1013.25 hPa
    h = (((pressure_ratio**(1/5.257)) - 1) * temperature ) / 0.0065
    return h


# altitude from international barometric formula, given in BMP 180 datasheet
def altitude_IBF(pressure):
    local_pressure = pressure    # Unit : hPa
    sea_level_pressure = 1013.25 # Unit : hPa
    pressure_ratio = local_pressure / sea_level_pressure
    altitude = 44330*(1-(pressure_ratio**(1/5.255)))
    return altitude

# Initiate I2C 
i2c = I2C(0,           # positional argument - I2C id
          sda=Pin(4),  # named argument - serial data pin
          scl=Pin(5),  # named argument - serial clock pin
          freq=400000) # named argument - i2c frequency

# scan i2c port for available devices
devices = i2c.scan()

if devices != []:
    print("found LCD I2C address")
    check_devices(devices)
else:
    print("unable to find LCD I2C address")

lcd = I2CLcd(i2c, 0x3f, 2, 16)
lcd.move_to(0,0)
lcd.putstr("Weather Station")
lcd.move_to(0,1)
lcd.putstr("Raspberry PiPico")

# Initiate I2C 
i2c = I2C(1,              # positional argument - I2C id
          sda = Pin(10),   # named argument - serial data pin
          scl = Pin(11),   # named argument - serial clock pin
          freq = 1000000) # named argument - i2c frequency

# scan i2c port for available devices
devices = i2c.scan()

if devices != []:
    print("found BMP280 I2C address")
    check_devices(devices)
else:
    print("unable to find BMP280 I2C address")

# create a BMP 280 object
#bmp280_object = BMP280(i2c_object,
#                       addr = 0x77, # change it 
#                       use_case = BMP280_CASE_WEATHER)

# configure the sensor
# These configuration settings give most accurate values in my case
# tweak them according to your own requirements

bmp = BMP280(i2c, 0x77, use_case = BMP280_CASE_WEATHER)
# bmp.power_mode = BMP280_POWER_NORMAL
# bmp.oversample = BMP280_OS_HIGH
# bmp.temp_os = BMP280_TEMP_OS_8
# bmp.press_os = BMP280_TEMP_OS_4
# bmp.standby = BMP280_STANDBY_250
# bmp.iir = BMP280_IIR_FILTER_2

print("BMP Object created successfully !")
utime.sleep(2) # change it as per requirement
print("\n")

#sleep(2)
#lcd.clear()
while True:
    # accquire temperature value in celcius
    temperature_c = bmp.temperature # degree celcius
    
    # convert celcius to kelvin
    temperature_k = temperature_c + 273.15
    
    # accquire pressure value
    pressure = bmp.pressure  # pascal
    
    # convert pascal to hectopascal (hPa)
    # 1 hPa = 100 Pa
    # Therefore 1 Pa = 0.01 hPa
    #pressure_hPa = ( pressure * 0.01 ) + ERROR # hPa
    pressure_hPa = ( pressure * 0.01 ) # hPa
    
    # accquire altitude values from HYPSOMETRIC formula
    h = altitude_HYP(pressure_hPa, temperature_k)
    
    # accquire altitude values from International Barometric Formula
    altitude = altitude_IBF(pressure_hPa)
    press = "{:.2f}".format(pressure_hPa)
    h_alti = "{:.2f}".format(h)
    i_alti = "{:.2f}".format(altitude)
    print("Temperature : ",temperature_c," Degree Celcius")
    print("Pressure : ",pressure," Pascal (Pa)")
    print("Pressure : ",press," hectopascal (hPa) or millibar (mb)")
    print("Altitude (Hypsometric Formula) : ", h_alti ," meter")
    print("Altitude (International Barometric Formula) : ", i_alti ," meter")
    print("\n")
    #utime.sleep(1.5)
    
    lcd.move_to(0,0)
    lcd.putstr("STEM Weather Stn")
    lcd.move_to(0,1)
    lcd.putstr("                ")
    lcd.move_to(0,1)
    lcd.putstr("Temp: ")
    lcd.putstr(str(temperature_c))
    lcd.putstr(" C")
    sleep(1.5)
    lcd.move_to(0,1)
    lcd.putstr("                ")
    lcd.move_to(0,1)
    lcd.putstr("Press:")
    lcd.putstr(str (press))
    lcd.putstr(" hPa")
    sleep(1.5)
    lcd.move_to(0,1)
    lcd.putstr("                ")
    lcd.move_to(0,1)
    lcd.putstr("Alt: ")
    lcd.putstr(str (i_alti))
    lcd.putstr(" mtr")
    sleep(1.5)
    

