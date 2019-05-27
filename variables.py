print("hello world")
# type anotation
x: int = 1
y: float = 4.2
z: str = 'i am string'
g: str = "i am string too"
f: str = """I am
multiline 
string
"""
print(x*y)
print(z)
print(g)
print(f)

# static types are used in language like c# and java
# where we cannot assign a sting value to variable defined as integer

# javascript and python are dynamic laguage
# means me can assign anyting to our variables
# bcoz variables types are assigned on run time and not on compile time

q = 2
q = "i am q"
print(q)

# primitive types are immutable
# means we cannot change them
m = 3
print(id(m))  # 1781818496
# m refer to this location in memory
m = 5  # update m
print(id(m))  # 1781818528
# m refer to this location in memory now
# as previous memory location id have no ref .. hence it will be removed my garbage collection

# list/array are mutable and can be changed
t = [1, 2, 3]
print(id(t))
t = ['1', 4, 5]
print(id(t))

# premetive constructor
letX = input('X: ')

print(int(letX))
print(float(letX))
print(str(letX))
print(bool(letX))

# Falsy values in python
# "", 0, [], None

# string and number concatination dosent work in python like js auto convert number to string
