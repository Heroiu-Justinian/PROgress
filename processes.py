import os,glob


supported_filestypes = ['.py','.cpp','.c','.js','.css','.html']
username = os.getlogin()


def get_directory():
    curr_dir = ""
    run_as_last_time = input("Do you want the script to run in the same directory?(y/n)")
    if run_as_last_time == "y":
        with(open("current.txt","r")) as last:
            curr_dir = last.read()
    else:
        path = input("Give me the path of the directory you want me to read from:  ")
        curr_dir = f"/home/{username}/{path}"
    return curr_dir

def get_scripts(path,ftypes,lst):
    for extension in ftypes:
        lst.extend(glob.glob(f"{path}*{extension}"))

def count_lines(script):
    count = 0
    lines =[]
    lines.extend(open(script).readlines())
    for line in lines:
        if (not line == "\n") or (not line[0] == "#"):
            count += 1
    return count

def count_comments(script):
    comments = 0
    for line in (open(script).readlines()):
        if line[0] == "#":
            comments += 1
    return comments



def traverse_dir(path):
    subdirs = []
    subdirs.extend(glob.glob(f"{path}*/"))
    return subdirs
    



    





