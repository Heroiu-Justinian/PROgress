import os,glob


supported_filestypes = ['.py','.cpp','.c','.js','.css','.html']
username = os.getlogin()
print(username)


def get_directory():
    path = input("Give me the path of the directory you want me to read from:  ")
    return path
def get_scripts(path,ftypes,lst):
    for extension in ftypes:
        lst.extend(glob.glob(f"/home/{username}/{path}*{extension}"))

#  (i) I am inclined to leave the comments as written lines because they are quite importamt and you actually take the time to write them so...
def count_lines(script):
    count = 0
    lines =[]
    lines.extend(open(script).readlines())
    for line in lines:
        if not line == "\n":
            count += 1
    return count

    





