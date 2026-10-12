"""
    hello this the playground module
    here we test we learned


"""
# import modules_packages
#
# print(modules_packages.__name__)
# print(__name__)
# print(__doc__)
#
# print(modules_packages.__doc__)


###########################################################

# import iti.courses
#
# import ai.greeting
#
# iti.courses.desc_python()
# ai.greeting.say_goodbye()

#
# from iti.courses import desc_python
#
# desc_python()


import iti
iti.test_connection()
iti.desc_python()

# from iti import test_connection
# test_connection()


def sum_num():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        print(num1 + num2)
        res = num1 + num2
        return res
    except Exception as e:
        print(e)
        return None
    finally:
        print("===The function reached its end  .... ")
    print("*******************************************")

val = sum_num()

print(val)













