
name = "ahmed azab"   # global variable


def say_hi():
    """
    Any variable defined inside the memory ==> local variable
    can be accessed only inside the function
    :return:
    """
    user_name = input("Please enter your name: ")
    print(f'Hello {user_name}!')



def outer():
    print("----Hello from outer function ---- ")
    def inner():
        course_name = 'python'
        print(course_name)
    inner()




####################################

print("----------------- checking the cope -----0")

# 1- do operation on global variable
# 1- can be accessed anywhere
print(name)  # read

name = name.title() # update
# print(f"name after update {name}")

print("----------------------")

#####################################
# local variable ---> any variable defined inside the function #

# say_hi()
# print(user_name)

def sum_numbers(num1, num2):
    return num1 + num2

# res = sum_numbers(1, 2)


#################################
print("----- Global variable and function ----------------------")

grade = 90

# I can read the value of the global variable from inside the function
def print_grade():
    print(f"from function I can see that the grade = {grade}")

# print_grade()

print('----- what happened when I try to modify the grade from inside the function ?')

def modify_grade():
    grade = input("Please enter your grade: ")  # new local variable
    if grade.isdigit():
        grade = int(grade)
        print(f"from function I can see that the grade = {grade}")
    else:
        print("the entered grade is not valid")



# modify_grade()
# print(f'after modification the grade is: {grade}')
######################################################
# you need to tell the interpreter that you will use the global variable


def modify_grade():
    global grade  # please don't create new local variable use the global
    grade = input("Please enter your grade: ")  # new local variable
    if grade.isdigit():
        grade = int(grade)
        print(f"from function I can see that the grade = {grade}")
    else:
        print("the entered grade is not valid")


# modify_grade()
# print(f'after modification the grade is: {grade}')


########################################
print("function inside a function ")
user_name = 'nshehab'

def user_info():
    user_name = input("Please enter your name: ")
    def print_user_name():
        print(f"username is {user_name}")
    print_user_name()
# user_info()








def user_info():
    user_name = input("Please enter your name: ")
    def print_user_name():
        print(f"username is {user_name}")

    def modify_user_name():
        nonlocal user_name
        user_name = user_name.title()
        user_name = input("Please enter your name: ").upper()  # new local variable
        print(f"username after modification {user_name}")
    modify_user_name()

user_info()
# user_info()
















