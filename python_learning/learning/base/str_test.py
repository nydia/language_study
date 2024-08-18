

ss: str = '1'
print(ss)


name = "Eve"
age = 30

# 使用加号
print("Hello, " + name + "! You are " + str(age) + " years old.")

# 使用 join()
print(" ".join(["Hello,", name, "!", "You", "are", str(age), "years", "old."]))

# 使用 f-string
print(f"Hello, {name}! You are {age} years old.")

# 使用 %
print("Hello, %s! You are %d years old." % (name, age))

# 使用 format()
print("Hello, {}! You are {} years old.".format(name, age))

# 使用 format_map()
data = {'name': name, 'age': age}
print("Hello, {name}! You are {age} years old.".format_map(data))