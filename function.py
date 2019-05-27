# without return statement function return None


def double(a=2):
    return a*2
    # pass return None


print(double(5))

# type annotation
# can be int, str, float, list, dict, touple.. etc


def increment(number: int, by: int = 1) -> int:
    return number+by


print(increment(4))

# arguments
# *args return arguments in a tuple -- read only iterator
# ** args return arguments in an dict


def letsTest(*args):
    print(args)
    for item in args:
        print(item)
    return True


print(letsTest(1, 2, 3, 4, 5, 6))


def dictArgs(**args):
    print(args)
    for item in args:
        print(item)
    return False


dictArgs(id=1, name="rajender")


def fizz_buzz(number):
    if (number % 5 == 0 and number % 3 == 0):
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return "FizzBuzz"


print(fizz_buzz(56))

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.


def x(a): return a + 10


print(x(5))


def x(a, b, c): return a + b + c


print(x(5, 6, 2))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))
