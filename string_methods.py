x = "  This is a long string  "

y = x[7:10]  # is
print(y)

y = x[7:]  # is a long string
print(y)

y = x[::-1]  # reverse string
print(y)

z = [1, 2, 3]
q = z[::-1]  # reverse array
print(q)
# methods
y = x.split(' ')
print(x)
print(y)
# y.join()  # join method is for string not for array

x.strip()
print(x)
print(x.find('long'))  # returns index
print(x.upper())
print(x.lower())
print(x.isalnum())
print(x.isdigit())
print(x.isnumeric())
print(x.startswith("  T"))  # True

# just like back ticks in js
# formatted strings
fff = "Hi"
gg = "There!"
hhh = f"{fff} {gg}"  # Hi There!
jjj = "{} {}".format(fff, gg)  # Hi There!
print(hhh, jjj)
