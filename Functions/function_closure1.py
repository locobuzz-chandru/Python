# Closure is a nested fun that allows us to access variables of the outer fun even after the outer function is closed
# Closure is a function object that remembers values in enclosing scopes even if they are not present in memory


def multiply_outer(n):
    def multiply_inner(x):
        return n * x

    return multiply_inner

# times3 = multiply_outer(3)
# times5 = multiply_outer(5)
# print(times3(9))
# print(times5(5))
