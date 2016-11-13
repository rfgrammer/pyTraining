# REF : https://www.youtube.com/watch?v=tJxcKyFMTGo

import os
from datetime import datetime

# display all function of os supported
print(dir(os))

# change directory
os.chdir('/home/charles/PycharmProjects/pyTraining/files')

# get current working directory
print(os.getcwd())

# list directories
print(os.listdir(os.getcwd()))

# create directory, but not allow to create sub-directory
os.mkdir('OS-Demo1')

# create directory even sub-directory is required
os.makedirs('OS-Demo3/Sub-Dir-1')

# remove directory, but not allow to remove sub-directory
os.rmdir('OS-Demo1')

# remove directory even sub-directory is required
os.removedirs('OS-Demo3/Sub-Dir-1')

# rename filename
os.rename('test.txt', 'demo.txt')

# get file information
print(os.stat('demo.txt'))
print(os.stat('demo.txt').st_mtime)

# change st_mtime to human-readable format
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# print all directories and files
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

# combine directory path and file name without worry
print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'demo.txt')
print(file_path)

# get filename only
print(os.path.basename(file_path))

# check if file exists. if not, return false
print(os.path.exists('/tmp/test.txt'))

# check if this is a directory
print(os.path.isdir('/tmp/test.txt'))

# check if this is a file
print(os.path.isfile('/tmp/test.txt'))

# spit file extension
print(os.path.splitext('/tmp/test.txt'))

# display all functions supported on os.path
print(dir(os.path))
