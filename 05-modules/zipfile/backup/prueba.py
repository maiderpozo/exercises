import os
import zipfile
import sys
f = open(sys.argv[1], "r")
lines =  f.readlines()
lines
with zipfile.ZipFile('file.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    for line in lines:
        line = line.rsplit("\n",1)[0]
        print(os.path.isfile(line))      
        zipf.write(line)
        print(line,"passed")
    