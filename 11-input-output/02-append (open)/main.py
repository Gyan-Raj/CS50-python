name = input("Enter your name: ")

# Everytime we run "python main.py" and give a name, it will keep appending that name to the file
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
# names.txt is the file which will be created
# "a" is for append
# f"{name}\n" to write on next line
