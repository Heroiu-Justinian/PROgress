
import os,glob,processes,time
from processes import supported_filestypes as sftp

# def GLOBALS
scripts =[]
current_lines = 0
lines_since_last_time = 0
current_directory = processes.get_directory()
sub_directories  = processes.traverse_dir(current_directory)
all_directories = [subs for subs in sub_directories]
all_directories.append(current_directory)




with open("time.txt","r") as time_table:
    elapsed =  round(time.time() - float(time_table.read()))

with open("time.txt","w") as time_table:
    time_table.write(str(float(time.time())))


with open("lines.txt","r") as f : 
    last_time_lines = int(f.read())

for current in all_directories:
    # print(current)
    processes.get_scripts(current,sftp,scripts)
print(scripts)
for script in scripts:
    current_lines += processes.count_lines(script)
    


# (i) This is the limit. I put this here so I don't have to go through every script again and number all the lines again, I just start from the lim
lim = len(scripts)
with open("lines.txt" , "w") as f:
    f.write(str(current_lines))

lines_since_last_time = current_lines - last_time_lines






if current_lines >= last_time_lines:
    print(f"Well my friend the script says you have written {lines_since_last_time} lines of code in {elapsed/60} minutes")
else:
    print(f"Since the last time you ran the script ({elapsed/60} minutes ago) you have deleted {lines_since_last_time * -1} lines of code")


        


