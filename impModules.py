import time
# This will print readable time.
print(time.ctime())

# The following function will calculate time since 1-Jan-1970 12:00:00 till now in seconds.
print(time.time())

# This will sleep/delay the program for a specific time.
for i in range(1, 11):
    print(i)
    time.sleep(2)
    
# ----------------------------------------------------------------------------------------------------------#

import webbrowser
import time

time.time() #Currnet time since 1970 in seconds.
time.sleep() #Adding delay in processing 

# ****************************************************************************************#

# Task - Auto open browser an lunch a video on youtube in a time interval.

time.sleep(5)
webbrowser.open('https://www.youtube.com/watch?v=60ItHLz5WEA')
 
# This can be run infinite time repeated in one hour with while loop.
while True:
  time.sleep(3600)
  webbrowser.open('https://www.youtube.com/watch?v=60ItHLz5WEA')
  
# ****************************************************************************************#

 # ----------------------------------------------------------------------------------------------------------#

import os

# Creating directory with Python code.
# Looking for current position in dir.
# print(os.getcwd())

# Changing current directory 
# os.chdir('path')

# Creating new directory.
# os.mkdir('Test Folder')

# Changing current directory
# os.chdir('path')

# Removing current directory
# os.rmdir('path')

# Looking all folders and files
# print(os.listdir())
