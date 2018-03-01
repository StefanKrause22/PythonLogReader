#
# This program will be the log reader for the DevOps Lab
#

import urllib.request
import re
import fnmatch


# webUrl = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
f = open("logfile.txt", "r+")
# f2 = open("errors.txt", "w+")
# data = webUrl.read().decode('utf-8')
# f.write(data)



totalRequests = 0
mostRequested, mostRequestedtimes = "", 0
leastRequested = 0


errors = []
counterErrors = 0
counter400 = 0
counter300 = 0
file_counter = {}
month_counter = {}

regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

for line in f:
    line = line.replace("\n", "")
    parts = regex.split(line)
    
    # adding to error list
    if not parts or len(parts) < 7:
        errors.append(line + "\n")
        counterErrors = counterErrors + 1
        continue

    # Testing for 4xx messages
    if parts[6][0] == '4':
        counter400 = counter400 + 1
        continue
    # Testing for 3xx messages
    if parts[6][0] == '3':
        counter300 = counter300 + 1
        continue  
    # Populating the Request Dictionary
    f_name = parts[4]
    if f_name in file_counter:
        file_counter[f_name] += 1
    else:
        file_counter[f_name] = 1

    mon = parts[1][3:6]
    if mon in month_counter:
        month_counter[mon] += 1
    else:
        month_counter[mon] = 1


    # print(parts[1][3:6])

    totalRequests += 1
    # print(parts)

# f2.write(str(errors))


for name, req in file_counter.items():
    if req == max(file_counter.values()):
        mostRequested = name
        mostRequestedtimes = req

for req in file_counter.values():
    if req == 1:
        leastRequested += 1

# print(file_counter.values())
# Debugging print lines    
# print(file_counter)

# Questions Answers
print("\n- Answers to Lab Questions -")
print("1) There were ", totalRequests, " total requests.")
print("2) The requests per month are as follows:  \n", month_counter)
print("3) There were ", counter400, " total 4xx messages.")
print("4) There were ", counter300, " total 3xx messages.")
print("5) The file that was requested the most was", mostRequested, " at", mostRequestedtimes, " times.")
print("6) There were ", leastRequested, " files that were only requested once.")
print("There were ", counterErrors, " total errors. They have been written to \"errors.txt\".")

# f2.close()
f.close()