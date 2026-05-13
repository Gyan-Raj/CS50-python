# def:      => def is define
# def hello (to="World"):           => function hello has a parameter with default value of "World"
# NOTE: Unlike JS, here hoisting (in normal functions) is not a concept in python, which means that we have to define a function before calling it
def hello(to="World"):
    print("Hello", to.title())


name = input("Enter you name ")
hello(name)


# return
def main():
    num = int(input("Enter a number "))
    print(f"Square of {num} is {square(num)}")


def square(n):
    # return n*n
    # return pow(n,2)
    return n**2  # all three does the same thing


main()
