'''create a function to read a text file. the function will take 
the name of the text file and display the content of the file into the console'''


def createafile(file,data):
    f = open(file,"w")
    f.write(data)
    return f
def readafile(file):
    f = open(file,"r")
    return f.read()
file = "this file is for read.txt"
data = "I am creating this file is for read and write"
print(createafile(file,data))
print(readafile(file))

    