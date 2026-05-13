import sys
from file_01_hello import hello

if(len(sys.argv) >= 2):
    hello(sys.argv[1])


"""
When we run this file using python file_02_call.py Gyan
We see that in output, it is printing:
    Hello World
    Goodbye World
    Hello Gyan
"""
# It is happening because when we import file_01_hello in this file, the main() function of that file gets executed, due to which "Hello World" and "Goodbye World" gets printed
# To fix this, we need to use __name__ == __main__ condition in file_01_hello file, we will see in 03-correct way