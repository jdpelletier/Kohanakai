import os
import datetime

def FileWrite(filepath, data):
    filename = filepath + "dataFile.txt"
    file = open(filename, W+)
    file.write(data)
    file.close()


def FolderCreate(today):

    todaystr = today.isoformat()

    path = "C:\\Users\\johnp\\Desktop\\Kohanakai\\TestData\\%s" % todaystr

    try:
        os.mkdir(todaystr)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
        return path
