```
apply_tuple = lambda f: lambda args: f(*args)
Example 1:

def add(a, b):
    return a + b

three = apply_tuple(add)((1, 2))
Example 2:

@apply_tuple
def add(a, b):
    return a + b

three = add((1, 2))
```
