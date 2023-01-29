from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET
import re
import os



dct = '20070810'
input = 'the quick brown fox will come today and lazy from will come tomorrow'

# List all files in a directory using os.listdir
basepath = 'data/text2graph'

    #open text file
text_file = open(basepath + "/data.txt", "w")

#write string to file
text_file.write(input)

#close file
text_file.close()

timex = dct

# compose the command to run
command = '../venv/bin/python tarsqi.py --dct ' + timex +' data/text2graph/data.txt'  + ' output.xml'
#command = 'python ttk/tarsqi.py --dct ' + timex +' /home/neo/environments/ttk/ttk/data/text2graph/'+entry+' ' + filename+'.xml'
stream = os.popen(command).read() 


output = ""
with open('output.xml','r') as file:
    output = file.read()
print(output)

