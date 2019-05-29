import functools

def my_decorator(func):
  @functools.wrap(func)
  def function_that_run_func(func):
    print("print before func run")
    func()
    print("print after func run")
  return function_that_run_func

@my_decorator
def my_function():
  print("I am function")
  
# my_function()
# decorators simply hijack our function and do something before and after running that function



# decorator with arguments

def my_dec_with_args(number):
  def my_decorator(func):
    @functools.wrap(func)
    def function_that_run_func(func):
      print("print before func run")
      func()
      print("print after func run")
    return function_that_run_func
  return my_decorator

@my_dec_with_args(56)
def my_function2():
  print("I am function")
  
my_function2()

  
