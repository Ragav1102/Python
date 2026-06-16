'''fruit=["apple","banana","cherry","kiwi","mango "]
print(fruit[2:])'''

'''fruit=["apple","banana","cherry","kiwi","mango "]
print(fruit[::-1])'''

fruit=["apple","banana","cherry","kiwi","mango "]
print(fruit[0:2])

fruit[0:2]=["orange","grapes"]
print(fruit)

fruit.append("watermelon")
print(fruit)

fruit.insert(1,"papaya")
print(fruit)

fruit.remove("kiwi")
print(fruit)

fruit.pop(1)
print(fruit)