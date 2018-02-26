#
# This program will be the log reader for the DevOps Lab
#

import urllib.request


# webUrl = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
f = open("logfile.txt", "r")
# data = webUrl.read().decode('utf-8')
# f.write(data)
linegroup = {}
i, cont = 1, True

while (cont == True):
    line = f.readline()
    
    if (line == ''):
        cont = False
    linegroup[i] = { line }
    i = i + 1

print(type(linegroup))
print(linegroup[1])
