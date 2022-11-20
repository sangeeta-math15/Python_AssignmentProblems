# An absolute path refers to the complete details needed to locate a file or folder,
# starting from the root element and ending with the other subdirectories

# Write a Python program to get an absolute file path.
import pathlib

# path of the given file
print(pathlib.Path("color_list.py").parent.absolute())

# current working directory
print(pathlib.Path().absolute())