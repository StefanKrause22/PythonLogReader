#
# This program will be the log reader for the DevOps Lab
#

# import urllib.request
import re
import fnmatch


# webUrl = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
f = open("logfile.txt", "r")
# data = webUrl.read().decode('utf-8')
# f.write(data)


linegroup = {}
i, cont, newline= 1, True, ""
# days = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15",
#         "16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# years = ["1994", "1995"]

errors = []
counterErrors = 0
counter4Unsuccessful = 0

regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

for line in f:
    line = line.replace("\n", "")
    parts = regex.split(line)
    
    # adding to error list
    if not parts or len(parts) < 7:
        errors.append(line)
        counterErrors = counterErrors + 1
        continue

    # Testing for 4xx messages
    # fourtest = re.compile('4..')
    # if re.match(fourtest, parts[6]):
    #     counter4Unsuccessful = counter4Unsuccessful + 1
    #     continue  


    linegroup[i] = parts      # Assigns the finished entry to the dictionary

# Debugging print lines    
#print(re.match(fourtest, parts[6]))
# print(type(linegroup))
print(linegroup[1])
print(type(linegroup[1]))

# Questions Answers
print("\n- Answers to Lab Questions -")
print("1) There were ", i, " total requests.")
# print("3) There were ", counter4Unsuccessful, " total 4xx messages.")
print("There were ", counterErrors, " total errors.")



