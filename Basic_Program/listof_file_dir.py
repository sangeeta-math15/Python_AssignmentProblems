
import pathlib
basedir = pathlib.Path('.').absolute()
print(basedir)
proj=basedir /'file.py'
proj.touch()
print(proj.exists())
# path='E:\Bridgelabz_CFP_127_batch\Python_Django_Programs'
#
# dir_list = os.listdir(path)
#
# print("Files and directories in '", path, "' :")
#
# print(dir_list)