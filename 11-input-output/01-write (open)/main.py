name = input("Enter your name: ")

# Everytime we run "python main.py" and give a name, it will override the file (It will not append)

file = open("names.txt", "w")
file.write(name)
file.close()  # We need to open and then finally close it

# names.txt is the file which will be created
# "w" is for write
