from time import pthread_getcpuclockid

# if = 10 # syntax error

#
# name = 'Noha'
# print(name)
# age = 20
# print(age)
#
# # print = "iti"
# # print("helllo")
#
# # define new variable ...
#
# x = y = 10
# print(x)
# print(y)
# x = x + 1
# print(x)
# print(y)


# x = y = 20
# print(hex(id(x)))
# print(hex(id(y)))
#
# x = x + 1  # re-assign
# print(hex(id(x)))
# print(hex(id(y)))

# everything is an object
x = y = 10

x = x +1

print(type(x))

#################3
print( "----------------------- Type casting, type conversion --------------------")

age = "25"
print(age, type(age))

# casting to int

age = int(age)
print(age, type(age))

iti = "Information Technology Institute"
print(iti, type(iti))

print(bool(iti))

#############
import sys
print ('------ convert string to int -------------')
# name = 'noha'
# name = int(name)
var1 = 256
var3 = ""
print(sys.getsizeof(var1), type(var1))
print(sys.getsizeof(var3), type(var3))

var4 = 'a'
print(sys.getsizeof(var4))

var5 = 22.555
print(sys.getsizeof(var5), type(var5))

var5 = 0.0
print(sys.getsizeof(var5), type(var5))


print(10 / 2 )


print(.1 +.2 == .3)

print(float(.1+.2)==float(.3))

x = .1+ .2
y = .3

print(x==y)

print((float(.1)+ float(.2))==float(.3))

print("iti" and 'python')



print("python" and "iti")


print(True  + 1 )

print(True == 1)

######################
"""string operations """


iti = "information technology Institute iiiiii"
new_iti = iti.replace("i", "$", 4)
print(new_iti)

###########################################3


msg = input("please leave your impression: ")

print(msg)
print(len(msg))


#############################3





for char in "information tech":
    print(char)

print("------------------------")


print(char)






















