import types

# decorator
def outer(callable_address):
    # if callable is function
    if isinstance(callable_address, types.FunctionType):
        def wrapper1(*args, **kwargs):
            print("inside decorator")
            callable_address(*args, **kwargs)
            print("outside decorator")

        return wrapper1

    # else callable  is class
    elif isinstance(callable_address, type):
            def method_decorator(method_name):
                def wrapper2(*args, **kwargs):
                    print("inside class decoratror")
                    method_name(*args, **kwargs)
                    print("outside class decorator")
                return wrapper2
            
            # decorating each and every function with method_decorator
            for name, address in callable_address.__dict__.items():
                if callable(address):
                    setattr(callable_address, name, method_decorator(address))
            return callable_address
    else:
        print("Invalid Callable Address")
        raise AttributeError

@outer
class Sample:
    
    def __init__(self,num1,num2):
        # print("start")
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1 + self.num2)
    
    def multiply(self):
        print(self.num1 * self.num2)
object1 = Sample(10,20)
@outer
def Point():
    print("Hello World")
# Point()
