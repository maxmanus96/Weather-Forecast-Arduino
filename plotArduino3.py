import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *
from weather import Weather, Unit

import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
#city = input('City Name :')
url = api_address + ('Toruń')
json_data = requests.get(url).json()
format_add = json_data['main']['temp']
#print(format_add)


tempC= []
pressure=[]

arduinoData = serial.Serial('/dev/ttyS1', 9600) #Creating our serial object named arduinoData
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0

def makeFig(): #Create a function that makes our desired plot
    #plt.ylim(80,90)                                 #Set y min and max values
    plt.title('My Live Streaming Sensor Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Temp C')                            #Set ylabels
    plt.plot(tempC, 'ro-', label='Degrees C')       #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
    plt2=plt.twinx()                                #Create a second y axis
    #plt.ylim(93450,93525)                           #Set limits of second y axis- adjust to readings you are getting
    plt2.plot(pressure, 'b^-', label='Temperature from Web') #plot pressure data
    plt2.set_ylabel('Weather-API')                    #label second y axis
    #plt2.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    plt2.legend(loc='upper right')                  #plot the legend
    

while True: # While loop that loops forever
    while (arduinoData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    arduinoString = arduinoData.readline() #read the line of text from the serial port
    #dataArray = arduinoString.split(',')   #Split it into an array called dataArray
    temp = arduinoString            #Convert first element to floating number and put in temp
    #weather = Weather(unit=Unit.CELSIUS)
    #lookup=weather.lookup(522678) #522678 WOEID for Torun,PL
    #condition = lookup.condition
    #forecasts=lookup.forecast
    #print(condition.text)
    #P =    float( dataArray[1])            #Convert second element to floating number and put in P
    tempC.append(temp)                     #Build our tempC array by appending temp readings
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
#city = input('City Name :')
    url = api_address + ('Toruń')
    json_data = requests.get(url).json()
    format_add = json_data['main']['temp']
    pressure.append(format_add)
    #for forecast in forecasts:
    	#pressure.append(forecast.low)#Building our pressure array by appending P readings    
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
        tempC.pop(0)                       #This allows us to just see the last 50 data points
        pressure.pop(0)
