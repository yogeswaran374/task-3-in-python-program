'''create a textfile with current timestamp'''


def createafile(filename,data):
    file = open(filename, "w")
    file.write(data)
    return file

from datetime import datetime

time = datetime.now().strftime("%d_%m_%y_%H_%M")
t = str(time)
a=str(datetime.now())
filename = t+".txt"
print(createafile(filename,a))