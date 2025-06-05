# scope, global variables
'''scope means
theres a apple tree in your garden so u can only access it 
but if the apple is on the road then everyone can access it
'''
# local scope: only be accessed inside the function
# global scope: mentioned outside the function, can be accessed anywhere in the code
'''python is not a block scope language, 
it means that if you define a variable inside a loop or an if statement, it can still be accessed outside of that block'''
x = 3


def pp():
    y = 100
    if x < 5:
        print(y)
        # x = x + 1 this will give an error because x is not defined in this scope
        print(x)


pp()
# how to change global variable inside a function
print("<========>")
z = 3


def pp():
    y = 100
    global z
    while z < 8:
        print(z)
        z = z + 1


pp()
# another way by using return statement
o = 1


def pp2(q):
    return q + 1


o = pp2(o)
print(o)

'''global constants which meant not to be changed is wriiten in all caps separated by underscore'''
