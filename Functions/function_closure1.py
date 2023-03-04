# Closure is a nested fun that allows us to access variables of the outer fun even after the outer function is closed
# Closure is a function object that remembers values in enclosing scopes even if they are not present in memory


def outer_function(outer):
    def inner_function(inner):
        return outer + inner

    return inner_function


inner_func = outer_function(5)
print(inner_func(10))
