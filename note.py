file = open("note.txt")
print(file.readline())
print(file.read())
file.close()


# python will close the file automatically
with open("note.txt") as file:
    print(file.read())
    
    
# iterating through files
with open("note.txt") as file:
    for line in file:
        print(line.upper()) 
        
# Removing new line and characters
with open("note.txt") as file:
  for line in file:
    print(line.strip().upper())
    
# sorting file
file = open("note.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)