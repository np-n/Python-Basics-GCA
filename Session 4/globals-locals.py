
# Gloval vs local variables

##bla = 2         # This is a global variable
##
##def somefunc(num):
####    bla = num + 4
####    print(bla)
####    global bla
####    print(bla)
####    bla = num + 4
##
##somefunc(5)
##print(bla)


# global variable
outer = 5

def sum(oouter):
    # local variable / function scope
    inner = 4
    global outer
    outer = 4
    return inner + outer

print(sum(outer))
print(outer)

