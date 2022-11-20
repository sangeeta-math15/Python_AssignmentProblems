# Write a python program to call an external command in Python.
import os, subprocess
subprocess.run('ls -al',shell=True)
# print(os.system('ls -l'))
# print(os.system('pwd'))