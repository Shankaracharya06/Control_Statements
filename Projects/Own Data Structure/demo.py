def type_checker(datatype):
    def decorator(func_name):
        def wrapper(*args, **kwargs):
            homo = True
            for value in (args or kwargs.values()):
                if type(value) != datatype:
                    homo = False
                    print("Wrong Data Type")
                    break
            
            if homo == True:
                func_name(*args, **kwargs)
        return wrapper
    return decorator

@type_checker(str)
def concat(string1, string2):
    print(string1 + string2)

# concat(12,n2=13)

# Create a parameterised decorator that takes number of time
def repeat(numbers):
    def decorator(func_name):
        def wrapper(*args, **kwargs):
            for _ in range(numbers):
                func_name(*args, **kwargs)
        return wrapper
    return decorator

@repeat(10)
def Sample():
    print("Hello")
Sample()