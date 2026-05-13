import sys

for arg in sys.argv:
    print(arg)

for arg in sys.argv[1:]:    # slice from first index (including) till end, try running this file as: python 01_slice.py Gyan Raj  => we will see Gyan and Raj in output
    print(arg)

for arg in sys.argv[1:-1]:    # slice from first index (including) till last index (excluding), try running this file as: python 01_slice.py Gyan Raj  => we will see Gyan in output
    print(arg)

for arg in sys.argv[:-1]:    # slice from first index (including) till last index (excluding), try running this file as: python 01_slice.py Gyan Raj  => we will see 01_slice.py and Gyan in output
    print(arg)
