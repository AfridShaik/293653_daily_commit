#solo lear program
#this program is about the celsius to fahrenhit conversion

celsius = int(input())

def conv(c):
    return 9/5 * celsius + 32

fahrenheit = conv(celsius)
print(fahrenheit)