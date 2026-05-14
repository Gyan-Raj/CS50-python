name = input("Enter your name: ")

# Everytime we run "python main.py" and give a name, it will override the file (It will not append)
open("names.txt", "w").write(name)

# names.txt is the file which will be created
# "w" is for write
