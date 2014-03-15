#!/usr/bin/env python
import sys
import os
from collections import OrderedDict
from os.path import expanduser

# Size of the history
histsize = 10000

# History file
HISTFILE = ".directory_history"

# Home directory of user
home = expanduser("~")

def split_after_first_semicolon(text):
    return text.split(";", 1)

def get_commands_in_directory(directory):
    commands_dir = []
    commands_not_dir = []
    try:
        with open(home + "/" + HISTFILE, "r") as f:
            # Get commands from history which were executed in directory "directory"
            for line in f.readlines():
                directory_in_history, command = split_after_first_semicolon(line.strip())
                if directory_in_history == directory and len(commands_dir) < histsize:
                    commands_dir.append(command)

            # Get commands from history which where not executed in directory "directory"
            f.seek(0)
            for line in f.readlines():
                directory_in_history, command = split_after_first_semicolon(line.strip())
                if directory_in_history != directory and (len(commands_not_dir) + len(commands_dir)) < histsize:
                    commands_not_dir.append(command)
    except IOError:
        open(home + "/" + HISTFILE, 'a').close()

    # More important/recent commands go towards the end of the list
    # Thats why commands_dir comes after commands_not_dir
    commands = commands_not_dir + commands_dir

    return commands

def get_indices_by_substring_and_directory(directory, substring):
    commands = get_commands_in_directory(directory)

    indices = []
    for cmd in commands:
        if substring.lower() in cmd.lower():
            index = commands.index(cmd)+1
            indices.append(index)

    # Remove duplicates - removing duplicates from the front
    # [4,3,2,1,4] -> [3,2,1,4]
    indices.reverse()
    indices_unique = list(OrderedDict.fromkeys(indices))
    indices_unique.reverse()

    return indices_unique

def get_command_by_index_and_directory(index, directory):
    i = 0
    for line in reversed(open(home + "/" + HISTFILE, "r").readlines()):
        directory_hist, command = split_after_first_semicolon(line.rstrip())

        if directory_hist == directory and index == i:
            print command
            return 0
        elif directory_hist == directory:
            i += 1

    return 1

# Return complete history for a directory if -a/-all -d DIRECTORY are arguments
if len(sys.argv) == 4 and (sys.argv[1] == "-a" or sys.argv[1] == "--all") and (sys.argv[2] == "-d"):
    directory = sys.argv[3]

    print "\n".join(get_commands_in_directory(directory))

# Return list of indizes which match a given substring
# directory_history.py -s/--substring SUBSTRING -d DIRECTORY
if len(sys.argv) == 5 and (sys.argv[1] == "-s" or sys.argv[1] == "--substring") and sys.argv[3] == "-d":
    directory = sys.argv[4]
    substring = sys.argv[2]

    indices = [str(i) for i in get_indices_by_substring_and_directory(directory, substring)]
    print "\n".join(indices)

# Return the i-th command in a certain directory
# directory_history.py -i/--index INDEX -d DIRECTORY
if len(sys.argv) == 5 and (sys.argv[1] == "-i" or sys.argv[1] == "--index") and sys.argv[3] == "-d":
    directory = sys.argv[4]
    index = int(sys.argv[2])

    if get_command_by_index_and_directory(index, directory) == 0:
        sys.exit(0)
    else:
        sys.exit(1)
