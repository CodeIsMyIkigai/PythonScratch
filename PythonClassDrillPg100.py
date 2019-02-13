
import os

'''
Python Class pg 100 Drill Description:
For this drill, you will need to write a script that will check a specific folder on the hard drive, verify whether 
those files end with a “.txt” file extension and if they do, print those qualifying file names and their corresponding 
modified time-stamps to the console.

Requirements:
1) Your script will need to use Python 3 and the OS module.
2) Your script will need to use the listdir() method from the OS module to iterate through all files within a specific 
directory.
3) Your script will need to use the path.join() method from the OS module to concatenate the file name to its file path, 
forming an absolute path.
4) Your script will need to use the getmtime() method from the OS module to find the latest date that each text file has 
been created or modified.
5) Your script will need to print each file ending with a “.txt” file extension and its corresponding mtime to the 
console.

Additional Setup Instructions:
You will need to create a new directory on your system and then create 10 different files within this folder. The files 
that you create should be a combination of any file types you would like just as long as you include at least two that 
are text documents ending with a “.txt” file extension.

This directory will be the directory that your script will need to iterate through to complete the drill.
'''

path = "C:/Users/Chest/PycharmProjects/Scratch"

# Interestingly the os.listdir method can take linux like paths... reduces escaping.
files = os.listdir(path)

for file in files:
    if file.endswith(".txt"):
        mtime = os.path.getmtime(os.path.join(path, file))
        print ("Found a text file: {} with mtime: {}".format(file, mtime))











