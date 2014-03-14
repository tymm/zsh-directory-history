#!/usr/bin/env python
import sys
from os.path import expanduser

if len(sys.argv) != 3:
    print "Needs command and directory as arguments"
    sys.exit(1)

command = sys.argv[1]
directory = sys.argv[2]
home = expanduser("~")

with open(home + "/.directory_history", "a") as f:
    # Append "directory;command"
    f.write(directory + ";" + command + "\n")
