import os,glob


supported_filestypes = ['.py','.cpp','.c','.js','.css','.html']
username = os.getlogin()


def get_directory():
    path = input("Give me the path of the directory you want me to read from:  ")
    return f"/home/{username}/{path}"
def get_scripts(path,ftypes,lst):
    for extension in ftypes:
        lst.extend(glob.glob(f"{path}*{extension}"))

def count_lines(script):
    count = 0
    lines =[]
    lines.extend(open(script).readlines())
    # print(script,lines[0])
    for line in lines:
        if not line == "\n":
            count += 1
    return count

def traverse_dir(path):
    subdirs = []
    subdirs.extend(glob.glob(f"{path}*/"))
    return subdirs
    


    





