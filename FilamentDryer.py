#!/usr/bin/env python

__author__      = "Inherited Object"
__source__      = "github.com/inherited-object/FilamentDryer"
__copyright__   = "Copyright 2024, Inherited Object"

#Global references
from Log import Log
from Config import Config

# Overall / parent object to all functions
# Funcionality:
#   Drying, heating, ventalation (internal & external)
#      Set, operate drying function
#      Internal ventalation to even out
#      Shedding excess humidity
#   Rotating / churning of spools
#     Allow for spools to be used in printing while being dried
class FilamentDryer:
    
    def __init__(self, _logFilePath:str = "./history.log", _pinFactory = None, _highAlertTempC = 60, _highAlertHumP = 40,
                 _lowAlertTempC = 30, _lowAlertHumP = 30, _timeLimitHours = 12, _heaterPowerLevel = "HALF_POWER"):
        
        #Initial Values
        
        #Initialize Log
        self.logFilePath = _logFilePath
        self.theLog = Log(self.logFilePath)
        #example use
        self.theLog.addEntry("Pin Factory: {}, High Alert Temp in C: {}, High Alert Humidity in %: {}, Low Alert Temp in C: {}, Low Alert Humidity in %: {}, Time Limit in Hours: {}, Heater Power level: {}, LogPath: {}"
                             .format(_pinFactory, _highAlertTempC, _highAlertHumP, _lowAlertTempC, _lowAlertHumP, _timeLimitHours, _heaterPowerLevel, self.logPath))
        
        
        self. pinFactory = _pinFactory
        self.highAlertTempC = _highAlertTempC
        self.highAlertHumP = _highAlertHumP
        self.lowAlertTempC = _lowAlertTempC
        self.lowAlertHumP = _lowAlertHumP
        self.timeLimitHours = _timeLimitHours
        self.heaterPowerLevel = _heaterPowerLevel
        #self.powerButton = digitalio.Di

        self.i2c = board.I2C()

        self.thSensor = adafruit_hdc302x.HDC302x(self.i2c)
        #initial value before being read
        self.currentTempC = 0
        self.currentHumP = 0
        
        
        
        
        
        
        #End of FilamentDryer.__init__()
        
        
        
        
        
        #Manage drying
        
        
        
        #Manage internal ventalation
        
        
        
        
        #Manage shedding ventalation
        
        
        
        
        #Manage spool curning / rotation
          #If a spool is in use don't rotate it
        
        
        
        
#Manage startup settings
######################################################################
#STARTUP/ENTRY
  #Read in config settings from file
configs=Config.readFromFile("config.txt")

_pinFactory = None
for i,a in configs.items():
    print("TEST: {} {}".format(a.name, a.value))
    
    if(a.name == 'HIGH_ALERT_TEMP_C'):
        _highAlertTempC = int(a.value)
    elif(a.name == 'HIGH_ALERT_HUM_P'):
        _highAlertHumP = int(a.value)
    elif(a.name == 'LOW_ALERT_TEMP_C'):
        _lowAlertTempC = int(a.value)
    elif(a.name == 'LOW_ALERT_HUM_P'):
        _lowAlertHumP = int(a.value)
    elif(a.name == 'TIME_LIMIT_HOURS'):
        _timeLimitHours = a.value
    elif(a.name == 'HEATER_POWER_LEVEL'):
        _heaterPowerLevel = a.value
    elif(a.name == 'LOG_FILE_PATH'):
        _logFilePath = a.value
    elif(a.name == 'PIN_FACTORY_IP'):
        _pinFactory = a.value
                #PiGPIOFactory(a.value)
        
pm = HeaterController(_logFilePath, _pinFactory, _highAlertTempC, _highAlertHumP, _lowAlertTempC, _lowAlertHumP, _timeLimitHours, _heaterPowerLevel)
            




    
    
    
