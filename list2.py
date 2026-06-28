fruits = ["apple","mango","banana","orange","pine"]
vegetable=["carrot","beetroot","beans"]

fruits.extend(vegetable)
print(fruits)

fruits.sort() #sort the list in ascending order
print(fruits)

fruits.reverse() #sort the list in descending order
print(fruits)

print (len(fruits)) #Return the number of elements in the list

print(fruits.index("banana")) #Return the index of "banana" in the list

print(fruits.count("mango")) #Return the number of occurrences of "mango" in the list