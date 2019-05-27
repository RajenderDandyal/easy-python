age = 24
if age and age <= 18:
    print("age is less than or equal to 18")
elif age and age > 18 and age <= 25:
    print("age is less than 25")
else:
    print("unknown age")

# pass keyword
# does nothing just fill the empty code block

if age and age >= 18:
    pass
else:
    pass

# logical operator

# and or not

if not age:
    print(" age is empty")
elif age and age < 25 or age == 25:
    print("age is less than or equal to 25")
# math like conditional chaining
if age and 18 <= age < 25:
    print('you are between 18 & 25')
else:
    pass

# terniary operator
message = "Terniary yes" if 18 < age < 25 else "terniary no"
print(message)
