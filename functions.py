########## functions with mandatory know number of parameters ############33

# syntax

def say_hi():
    pass

# print(say_hi())

####
def say_hi2():
    return

############
def say_hi3():
    return "Hi AI47"

res = say_hi3()


####
# function accept argument, return res

def sum_num(num1, num2):
    print(f"num1= {num1}, num2= {num2}")
    res = num1 + num2
    return res

myres = sum_num(3,4)
print(myres)

myres2 = sum_num(4,3)
print(myres2)



myres2 = sum_num(num2=4,num1=3)
print(myres2)


#######################

# functions with optional parameters ??
########## functions with mandatory know number of parameters (min, max) ############33


def multiply_num(num1, num2=10):
    print(f"num1= {num1}, num2= {num2}")
    res = num1 * num2
    return res

print(multiply_num(3,4))
print(multiply_num(4))



# SyntaxError: parameter without a default follows parameter with a default

"""
def multiply_num(num1=5, num2):
    print(f"num1= {num1}, num2= {num2}")
    res = num1 * num2
    return res
"""

#############################
### functions that accept zero or more ,,, *
print()
print(3,44,44)
print(3)

def ask_for_grades(*grades):
    print(f"Grades: {grades}")  # tuple

# ask_for_grades(223)
# ask_for_grades(33, 324)

##########################3
# temp ="My name is {}, I lives in {}"
# print(temp.format("Nada", "SIn"))


################################
def introduce_your_self(**info):
    print(info)


introduce_your_self(name='noha', work="ITI", salary =3000000)

introduce_your_self()
introduce_your_self(last_name='Hesham')


temp ="My name is {name}, I lives in {city}"
print(temp.format(name="Nada", city="SIn"))







