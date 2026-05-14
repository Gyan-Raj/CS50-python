name = input("Enter your name: ")

# Instead of opening and then finally closing the "file" after writing, we can do it using "with" keyword
"""
    file = open("names.txt", "a")
    file.write(f"{name}\n")
    file.close()
"""

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

"""
# The syntax is:
    with function_in_question as name_of_the_variable_that_should_be_assigned_to_the_return_value_of_the_"funciton_in_question":
"""