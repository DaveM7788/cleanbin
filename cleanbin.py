import os
import shutil
import getpass

whoami = getpass.getuser()
trashdir = '/Users/' + whoami + '/.Trash'

for root, dirs, files in os.walk(trashdir):
    for dir in dirs:
        dirlocation = os.path.join(root, dir)
        shutil.rmtree(dirlocation, ignore_errors=True)
        print("removing directory " + dirlocation)