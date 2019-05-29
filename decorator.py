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
  

# decorators simply hijack our function and do something before and after running that function
