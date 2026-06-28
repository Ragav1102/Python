str="Hello Python World"
print(str)

print(str.upper()) #Convert all characters in the string to uppercase

str1=" Hello Python World "
print(str1.strip()) #Remove the space both side

print(str.lstrip()) #Remove left space

print(str1.rstrip())  #Remove right space

print(str.find("Python"))   #find Index value

print(str.count("l"))  #Count the word

print(str.replace("World","life")) #Replace "World" with "life"

print(str.startswith("H")) #Check if the string starts with "H"

print(str.endswith("d"))  #Check if the string ends with "d"

str1="Hello, Python, World"
b=str1.split(",")  #Split the string into a list using comma as the delimiter
print(b)

name="ragavan RAJA"
print(name.capitalize())  #first word change into upper case

print(name.title())   #Each word starts with upper case

print(name.lower())   #all string small

