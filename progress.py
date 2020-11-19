
import os,glob,processes,time
from math import floor
from processes import supported_filestypes as sftp

# def GLOBALS
scripts =[]
current_lines = 0
comms = 0
lines_since_last_time = 0
current_directory = processes.get_directory()
sub_directories  = processes.traverse_dir(current_directory)
all_directories = [subs for subs in sub_directories]
all_directories.append(current_directory)



with(open("current.txt","w")) as curr: 
    curr.write(current_directory)


with open("time.txt","r") as time_table:
    elapsed =time.time() - float(time_table.read())

with open("time.txt","w") as time_table:
    time_table.write(str(float(time.time())))



with open("lines.txt","r") as f : 
    last_time_lines = int(f.read())

for current in all_directories:
    processes.get_scripts(current,sftp,scripts)

for script in scripts:
    current_lines += processes.count_lines(script)
    comms += processes.count_comments(script)



    


# (i) This is the limit. I put this here so I don't have to go through every script again and number all the lines again, I just start from the lim
lim = len(scripts)
with open("lines.txt" , "w") as f:
    f.write(str(current_lines))

lines_since_last_time = current_lines - last_time_lines



time_in_minutes = floor(elapsed/60)
time_in_hours = floor(elapsed/3600)


if current_lines >= last_time_lines:
    if time_in_minutes > 60:   
        print(f"It looks like you have written {lines_since_last_time} lines of code in {time_in_hours} hours and {time_in_minutes} minutes")
    else:
        print(f"It looks like you have written {lines_since_last_time} lines of code in {time_in_minutes} minutes")
else:
    if time_in_minutes > 60:   
        print(f"It looks like you have written {lines_since_last_time} lines of code in {time_in_hours} hours and {time_in_minutes} minutes")
    else:
        print(f"It looks like you have written {lines_since_last_time} lines of code in {time_in_minutes} minutes")


if(comms/current_lines < 0.03):
    print("Also you should consider adding more comments to your project as the ratio between the number of comments in your code and the number of lines of code you have written in total is less than 1 to 30 which is not very ideal in most cases")





