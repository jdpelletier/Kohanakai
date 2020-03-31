import os
import datetime

def FileWrite(filepath, data):
    filename = os.path.join(str(filepath), "dataFile.txt")
    with open(filename, 'a') as f:
        today = datetime.datetime.now()
        time = today.time().strftime('%H:%M:%S')
        f.write(time)
        f.write(data)
        f.write("\n")
        f.close()


def FolderCreate(today):

    todaystr = today.isoformat()

    parent_directory = "/home/pi/Desktop/Kohanakai/TestData"
    path = os.path.join(parent_directory, todaystr)
    try:
        os.mkdir(path)
    except OSError:
        print ("The folder %s is already created" % path)
    else:
        print ("Successfully created the directory %s " % path)
    return path
