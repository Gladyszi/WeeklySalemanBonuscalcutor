import os

path="test.txt"

if os.path.exists(path):
    print("This file exists")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("This is a file")
else:
    print("This file could not be found")