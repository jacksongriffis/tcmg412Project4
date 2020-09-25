#Jackson Griffis
#TCMG 412-500
#Group Project #3: Using Python


# 1. How many requests were made on each day? 
# 2. How many requests were made on a week-by-week basis? Per month?
# 3. What percentage of the requests were not successful (any 4xx status code)?
# 4. What percentage of the requests were redirected elsewhere (any 3xx codes)?
# 5. What was the most-requested file?
# 6. What was the least-requested file?


from urllib.request import urlretrieve
from os import path
import re

#variables
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
logfile = 'accesslog.log'
total_requests = 0
past_year_requests = 0
unsuccessful_requests = 0
redirected_requests = 0
past_year = '/1995'
days = {}
months = {}
filenames = {}


#check if log file is already downloaded
if path.exists('accesslog.log') == False:
    #parse log file and download to local machine with progress bar
    print("Parsing log file, please wait:")
    logfile, headers = urlretrieve(URL, logfile, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)


#open the file, read each line, and count each line and date in past year
with open("accesslog.log") as fh:
    Lines = fh.readlines()
    for line in Lines:
        total_requests += 1
        if past_year in line:
            past_year_requests += 1
            #question 3    
            if '403 -' in line or '404 -' in line:
                unsuccessful_requests += 1
            #question 4    
            if '302 -' in line:
                redirected_requests += 1
        #question 1-2    
        result = re.split('.+ \[(.+) .+\] "[A-Z]{3,5} (.+) HTTP/1.0" ([0-9]{3})', line)
        if len(result) == 5:
            date = result[1]
            file = result[2]
            
            
            date = date.split(':')
            if date[0] in days:
                days[date[0]] += 1
            else:
                days[date[0]] = 1
                
            date[0] = date[0].split('/')
            if date[0][1] + " " + date[0][2] in months:
                months[date[0][1] + " " + date[0][2]] += 1
            else:
                months[date[0][1] + " " + date[0][2]] = 1
            
            if file in filenames:
                filenames[file] += 1
            else:
                filenames[file] = 1
            
        
    
#print the results        
print("-----------------------------------")       
print("Total requests in the last year: " + str(past_year_requests))
print("Total requests in entire log: " + str(total_requests))
print("-----------------------------------")
print("Unsuccessful requests: " + str(unsuccessful_requests))
print("Redirected requests: " + str(redirected_requests))
print("-----------------------------------")
print("Most requested file: " + str(list(filenames.keys())[0]))
print("Least requested file: " + str(list(filenames.keys())[-1]))
print("-----------------------------------")
print("Requests per month: ")
for key, value in months.items():
    print(str(key) + " - Occurrences: " + str(value))
print("-----------------------------------")
print("Requests per day: ")
for key, value in days.items():
    print(str(key) + " - Occurrences: " + str(value))
print("-----------------------------------")