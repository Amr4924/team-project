# comment = true
# print =true
# input =true
# variables = true
# data types = true
# str string "anything" , "23", " "
# int intger 12, 15, -110
# bool boolean True, False
# float fractions 3.3, 5.2, 0.012

# print, input, type, upper, lower, capitalize, title, strip, lstrip, rstrip, split, join, swapcase, len


# print("amr","saad",sep=' ',end="--")
print("Age is 20")
# age=input("Enter your age: ")

# print(age)

a="amr"
print(type(a))
print("-"*50)

b=20

print(type(b))
print("-"*50)

c= True

print(type(c))
print("-"*50)

d=305.14

print(type(d))


print("*" * 50)

name = "Amr saad"

print(name.upper()) # convert to uppercase
print(name.lower()) # convert to lowercase
print(name.capitalize()) # capitalize First Latter
print(name.title()) # capitalize First Letter of each word

print("*" * 50)

name2 ="  amr saad  "
print(name2.lstrip())
print(name2.rstrip())
print(name2.strip())
print("*" * 50)

name3 = "       amr          saad           rajab        "
# print(name3.split()) # split by space

# name4= name3.split()
# print(name4)
# name5 = " ".join(name4)
# print(name5)

print(" ".join(name3.split()))
name8 = "amr saad rajab"

print(len(name8))