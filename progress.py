
import os,glob,read,time
from read import supported_filestypes as sftp

# def GLOBALS
scripts =[]
current_lines = 0
lines_since_last_time = 0

with open("time.txt","r") as time_table:
    elapsed =  time.time() - float(time_table.read())

with open("time.txt","w") as time_table:
    time_table.write(str(float(time.time())))


with open("lines.txt","r") as f : 
    last_time_lines = int(f.read())

read.get_scripts(read.get_directory(),sftp,scripts)


for script in scripts:
    current_lines += read.count_lines(script)
with open("lines.txt" , "w") as f:
    f.write(str(current_lines))

lines_since_last_time = current_lines - last_time_lines






if current_lines >= last_time_lines:
    print(f"Well my friend the script says you have written {lines_since_last_time} lines of code in {elapsed/60} minutes")
else:
    print(f"Since the last time you ran the script ({elapsed/60} minutes) you have deleted {lines_since_last_time * -1} lines of code")
