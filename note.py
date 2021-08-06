import os
import datetime

# file = open("note.txt")
# print(file.readline())
# print(file.read())
# file.close()


# # python will close the file automatically
# with open("main.txt") as file:
#     print(file.read())
    
    
# # iterating through files
# with open("main.txt") as file:
#     for line in file:
#         print(line.upper()) 
        
# # Removing new line and characters
# with open("main.txt") as file:
#   for line in file:
#     print(line.strip().upper())
    
# # sorting file
# file = open("note.txt")
# lines = file.readlines()
# file.close()
# lines.sort()
# print(lines)

# # write to the files
# with open("note1.txt", "w") as file:
#   file.write("Writing to the file")
  
  
#  deleting file
# os.remove("note1.txt")

# # rename file
# os.rename("note.txt", "main.txt")

# file exist 
print(os.path.exists("main.txt"))

# get how big the file is
size = os.path.getsize("main.txt")
print(size)
time_stamp = os.path.getmtime("main.txt")
print(time_stamp)

human_format= datetime.datetime.fromtimestamp(time_stamp)
print(human_format)

# convert file to absolute path
abs_path = os.path.abspath("main.txt")
print(abs_path)

# get current working directory
print(os.getcwd())

# create a new directory
# os.mkdir("new_dir")
# change current directory
# 
# remove directory
# os.rmdir("new_dir")

# listing directories
os.listdir(os.getcwd())
print(os.listdir("/Users/sam/Projects/"))

# diff file and directory

dir = "/Users/sam/Projects/"

for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
      print(f"{fullname} is a file")

