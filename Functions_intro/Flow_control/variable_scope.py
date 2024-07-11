x = 'global'             # The outer function can not access the inner function but the inner function can access for the outer one.

def outer_func():
    y = 'enclosing'
    def inner_func():
        z = 'local'
        print(x)
        print(y)
        print(z)         # The inner function can acces the outer function.
    inner_func()

outer_func()
print(x)
# print(y)               # The outer function can not access the inner function but the inner function can access for the outer one.