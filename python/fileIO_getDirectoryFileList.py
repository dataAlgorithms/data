# Obtain a list of files in a directory
#  including all files, subdirectories, symbolic link
import os
names = os.listdir('.')
for name in names:
    print(name, end=' ')

.ipynb_checkpoints ads classification.ipynb datasets Housing.ipynb LinearModel.ipynb SVM.ipynb Untitled.ipynb untitled.txt 

# Get all regular files
import os.path

names = [name for name in os.listdir('.')
          if os.path.isfile(os.path.join('.', name))]
for name in names:
    print(name, end=' ')

classification.ipynb Housing.ipynb LinearModel.ipynb SVM.ipynb Untitled.ipynb untitled.txt 


# Get all dirs
import os.path

dirnames = [name for name in os.listdir('.')
             if os.path.isdir(os.path.join('.', name))]
for name in dirnames:
    print(name, end=' ')

.ipynb_checkpoints ads datasets 

# Filter the content of a directory
import os

txtEndFiles = [name for name in os.listdir('.')
             if name.endswith('.txt')]
untitledStartFiles = [name for name in os.listdir('.')
             if name.startswith('untitled')]

for name in txtEndFiles:
    print(name, end=' ')

for title in untitledStartFiles:
    print(title, end=' ')

untitled.txt untitled.txt 

# Filename matching with glob or fnmatch
import os
import glob

txtfiles = glob.glob("*.txt")
print(txtfiles)

from fnmatch import fnmatch
txtfiles = [name for name in os.listdir('.')
             if fnmatch(name, '*.txt')]
print(txtfiles)

['untitled.txt']
['untitled.txt']

# Get additional info of direcotry listing
import os
import os.path
import glob
import time

ipynbfiles = glob.glob('*.ipynb')

# Get files sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in ipynbfiles]

for name, size, mtime in name_sz_date:
    print(name, size, mtime)

print("\r\n")

# Get file metadata
file_metadata = [(name, os.stat(name)) for name in ipynbfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
    
print("\r\n")

# Format time format
print(time.ctime(meta.st_mtime))

classification.ipynb 11033 1498825535.3480551
Housing.ipynb 220442 1498723157.9832065
LinearModel.ipynb 309567 1499074332.2197454
SVM.ipynb 90799 1499163357.3880062
Untitled.ipynb 6136 1508464484.6488225


classification.ipynb 11033 1498825535.3480551
Housing.ipynb 220442 1498723157.9832065
LinearModel.ipynb 309567 1499074332.2197454
SVM.ipynb 90799 1499163357.3880062
Untitled.ipynb 6136 1508464484.6488225


Fri Oct 20 09:54:44 2017
