import os
import datetime
import shutil

def NowString():
    today = datetime.datetime.now()
    time = today.time().strftime('%H:%M:%S')
    return time

def FileWrite(filepath, data):
    filename = os.path.join(str(filepath), "dataFile.txt")
    with open(filename, 'a') as f:
        f.write(NowString())
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

def HandlePlot(path, image):
    test_dir = path
    image_dir = "/var/www/html"
    shutil.copy(image, test_dir)
    shutil.copy(image, image_dir)

def HTMLWrite(data):
    filename = "/var/www/html/index.html"
    currentDay = datetime.date.today()
    dayString = currentDay.isoformat()
    data = data.split()
    with open(filename, 'w+') as f:
        text = '''
            <!DOCTYPE html>
            <html>
            <header><title>Tank Temps</title></header>
            <body>
            <h1>Tank Temps on %s</h1>
            <p>Max temp for today:</p>
            <ul>
                <li>%s</li>
            </ul>
            <p>Temps at %s</p>
            <ul>
              <li>Meter 1: %s</li>
              <li>Meter 2: %s</li>
              <li>Meter 3: %s</li>
            </ul>
            <img src="TempsToday.jpeg" ALT="Temp Plot">
            </body>
            </html>
            ''' % (dayString, data[3], NowString(), data[0], data[1], data[2])
        f.write(text)
        f.close()