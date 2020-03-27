import serial
import time
import datetime
import Util
#import chart_studio.plotly as py
#import plotly.graph_objects as go



ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

# Read and record the data
values = []
data1 =[]
data2 =[]
data3 = []                    # empty list to store the data
t =[]
i = 0
currentDay = datetime.date.today()
path = FolderCreate(currentDay)

try:
    while(True):
        if currentDay != datetime.date.today():
            currentDay = datetime.date.today()
            FolderCreate(currentDay)
        b = ser.readline()         # read a byte string
        string_n = b.decode()      # decode byte string into Unicode
#        string = string_n.rstrip() # remove \n and \r
        FileWrite(path, string_n)
#        values = string.split()
#        values[0] = float(values[0])
#        values[1] = float(values[1])
#        values[2] = float(values[2])
#        data1.append(values[0])           # add to the end of data list
#        data2.append(values[1])
#        data3.append(values[2])
#        if i%60 == 0:
#            t = [datetime.datetime.now() + datetime.timedelta(seconds=i) for i in range(len(data1))]
#            xy1 = go.Scatter(
#                x = t,
#                y = data1
#                )
#            xy2 = go.Scatter(
#                x = t,
#            xy3 = go.Scatter(
#                x = t,
#                y = data3
#            )
#            xydata = [xy1, xy2, xy3]
#            first_plot_url = py.plot(xydata, filename = 'Temps', auto_open=False)
#	    print i
#        i += 1
        time.sleep(5)            # wait 5 minutes
except KeyboardInterrupt:
    print('Script ended')

ser.close()
