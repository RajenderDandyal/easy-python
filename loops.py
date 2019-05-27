# only two types of loops
# for and while
x = [{"id": 1, "name": "raj"}, {"id": 2, "name": "rajender"},
     {"id": 3, "name": "rajenderDandyal"}]

for item in x:
    print(item["id"])
    print(item["name"])

# break and continue
for item in x:
    if item["name"] == "rajender":
        continue
    print(item["name"])

for item in x:
    if item["id"] == 2:
        break
    print(item["id"])

# for else
# look for name starting with J
# if found print Found else Not Found
found = False
for items in x:
    if item["name"].startswith('J'):
        found = True
        break

message = "Found" if found else "Not found"
print(message)

# with for else
# else block executes if the for loop executes successfully
# without using the break statement
message = None
for item in x:
    if item['name'].startswith('J'):
        message = "Found"
        break
else:
    message = "Not found"
print(message)

# range
z = 0
for z in range(0, 10, 1):
    print(z)


# while loop
y = 0
while y <= 10:
    print(y)
    y = y+1

# while with else
# else block will execute even if while loop dosent
while 10 < y < 15:
    print('i am y')
    y = y+1
else:
    print('i am y in else')
