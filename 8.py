def lucky_number(name):
    number = len(name) * 9
    name = "Hello " + name + ". Your lucky number is " + str(number)
    return name


print(lucky_number("Kay"))
print(lucky_number("Cameron"))