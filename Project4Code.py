#Jackson Griffis
#TCMG 412-500
#Group Project #3: Using Python

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
filenames = {}

#check if log file is already downloaded
if path.exists('accesslog.log') == False:
    #parse log file and download to local machine with progress bar
    print("Parsing log file, please wait:")
    logfile, headers = urlretrieve(URL, logfile, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)


#open the file, read each line, and count each line and date in past year
fh = open(logfile)
for line in open(logfile):
    total_requests += 1
    fh.readline()
    if past_year in line:
        past_year_requests += 1
    #question 3    
    if '403 -' in line or '404 -' in line:
        unsuccessful_requests += 1
    #question 4    
    if '302 -' in line:
        redirected_requests += 1
    #question 1-2    
    date = re.split('[:', line)
    file = date[]
    if file in filenames:
        filenames[file] += 1
    else:
        filenames[file] = 1
            
        
    
#print the results        
print()       
print("Total requests in the last year: " + str(past_year_requests))
print("Total requests in entire log: " + str(total_requests))
print() 
print("Unsuccessful requests: " + str(unsuccessful_requests))
print("Redirected requests: " + str(redirected_requests))