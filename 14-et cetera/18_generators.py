def main():
    n = int(input("Enter a number: "))
    for s in sheep(n):
        print(s)


# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock

def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()

# This code above works perfect for small numbers like 1 or 10 or 100 or 1000 or 10000 or even for 100000. But for higher numbers, the app crashes
# This is because the system is trying to print all at once.
# To overcome this, we can use genrators (yield) (18_generators.py)
