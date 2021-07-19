"""
file and directory management
shutil.copy()
"""

import os
import sys
import shutil

source = 'pic1.jpg'
target = 'dest_dir'

assert not os.path.isabs(source)
target = os.path.join(target, os.path.dirname(source))
print(target)

# create the folders if not already exists
# os.makedirs(target)

# adding exception handling
try:
    shutil.copy(source, target)
except IOError as e:
    print("Unable to copy file. %s" % e)
except:
    print("Unexpected error:", sys.exc_info())
finally:
    print("done.")
