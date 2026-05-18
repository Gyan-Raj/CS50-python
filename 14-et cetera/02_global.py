balance = 0


def main():
    print("Balance:", balance)
    deposit(120)
    withdraw(30)
    print("Balance:", balance)


def deposit(n):
    balance += n


def withdraw(n):
    balance -= n


if __name__ == "__main__":
    main()

r"""
This code will throw an "UnboundLocalError"
Balance: 0
Traceback (most recent call last):
  File "C:\Users\bhard\Desktop\learning\CS50-python\14-et cetera\02_global.py", line 20, in <module>
    main()
    ~~~~^^
  File "C:\Users\bhard\Desktop\learning\CS50-python\14-et cetera\02_global.py", line 6, in main
    deposit(120)
    ~~~~~~~^^^^^
  File "C:\Users\bhard\Desktop\learning\CS50-python\14-et cetera\02_global.py", line 12, in deposit
    balance += n
    ^^^^^^^
UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value
"""

"""
To resolve this, we need to use "global" keyword as in 03_global.py
"""