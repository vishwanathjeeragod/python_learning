#a=5
#b=5
#print(id(a))
#print(id(b))
#print(a is  not b)

#a=5
#print(id(a))
#a=8
#print(id(a))
#print(a is a)

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is z)        # True — both refer to the same object
print(x is y)        # False — both have same values, but different memory locations
print(x == y)        # True — values are equal
print(x is not y)    # True — because x and y are not the same object
