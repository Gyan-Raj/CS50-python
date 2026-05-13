import sys
from file_01_hello import hello

if (len(sys.argv) >= 2):
    hello(sys.argv[1])


"""
When we run this file using python file_02_call.py Gyan
We now only see following in output:
    Hello Gyan
"""
