#
# This program will be the log reader for the DevOps Lab
#

# import urllib.request


# webUrl = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
f = open("logfile.txt", "r")
# data = webUrl.read().decode('utf-8')
# f.write(data)
linegroup = {}
i, cont, newline= 1, True, ""
days = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15",
        "16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
years = ["1994", "1995"]

while (cont == True):
    line = f.readline()
    line = line.replace("\n", "")
    newline = line.split(" ")
    # newline
    linegroup[i] = newline      # Assigns the finished entry to the dictionary
    
    if (line == ''):
        cont = False
    i = i + 1

# print(type(linegroup))
print(linegroup[1])
print(type(linegroup[1]))


