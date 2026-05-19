# "constants" are used when we don't want to change the value
# There is no cpncept of constants in python
# It is similar to what we learnt for getter-setter (03_the_problem), where we saw it is just the convention to use "_" (_variableName) so that other developers should know that we should not override the variable directly using _variableName (even when we can)
# Similarly, here, for constants we use capital case to let other developers know that the vaiable declared using upper case should not be modified (even when we can do it)

class Cat:
    COUNT = 3

    def meow(self):
        for _ in range(Cat.COUNT):
            print("meow")


cat = Cat.meow()
