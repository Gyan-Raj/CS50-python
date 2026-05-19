# When we use inputs in command line (and read it using sys (sys.argv[index])), it may get messy when we have lot of arguments (when we configure the application using command line)
# We have to be cautious in the order of arguments
# To simplify this, we have one in-built library called "argparse"

"""
Now, suppose we want to set input of count as 3 from command line, we can do:
python 08_argparse -n 3
# In the above script "python 08_argparse -n 3", we use "-n" just for the sake of convention where it will mean some number
# So, to extract its value in our application, we need to do something like this:
if len(sys.argv)==3 and sys.argv[1] == "-n":
    count = int(sys.argv[2])
    for _ in range(count):
    print("meow")
"""

# But the above approach becomes messy with large number of inputs. Therefore we use argparse package
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument(
    "-n", default=1, help="Number of times cat will meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
