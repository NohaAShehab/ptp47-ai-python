import sys

l = [1,2,3]

print(sys.getrefcount(l))

m = l

print(sys.getrefcount(l))