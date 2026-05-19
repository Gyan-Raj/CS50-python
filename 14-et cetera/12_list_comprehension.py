# [<function_to_be_executed_on_each_element> for <element> in <tuple/list>]

def main():
    yell("Learning", "Pyhton", "from", "CS50")


def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
