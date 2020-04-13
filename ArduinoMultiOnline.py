import serial
import time
import datetime
import Util
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



# Read and record the data
values = []
data1 = []
data2 = []
data3 = []
t = []
currentDay = datetime.date.today()
path = Util.FolderCreate(currentDay)
startTime = datetime.datetime.now()

try:
    while(True):
        if currentDay != datetime.date.today():
            currentDay = datetime.date.today()
            path = Util.FolderCreate(currentDay)
            startTime = datetime.datetime.now()
            data1 = []
            data2 = []
            data3 = []
        ser = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(5)
        b = ser.readline()         # read a byte string
        string_n = b.decode()      # decode byte string into Unicode
        string = string_n.rstrip() # remove \n and \r
        print(string)
        values = string.split()
        if len(values) != 3 or string[0] != ' ':
            print("line skipped")
            continue
        values[0] = float(values[0])
        values[1] = float(values[1])
        values[2] = float(values[2])
        data1.append(values[0])           # add to the end of data list
        data2.append(values[1])
        data3.append(values[2])
        t = [startTime + datetime.timedelta(minutes=5*i) for i in range(len(data1))]
        plt.plot(t, data1, 'ro', t, data2, 'bs', t, data3, 'g^')
        xformatter = mdates.DateFormatter('%H:%M')
        plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)
        plt.savefig("TempsToday.jpeg")
        plt.close()
        maxes = [np.amax(data1), np.amax(data2), np.amax(data3)]
        maxTotal = str(np.amax(maxes))
        string = string + " " + maxTotal
        Util.FileWrite(path, string)
        Util.HandlePlot(path, "TempsToday.jpeg")
        Util.HTMLWrite(string)
        ser.close()
        time.sleep(295)            # wait 5 minutes
except KeyboardInterrupt:
    print('Script ended')

ser.close()
