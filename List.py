fruit=["apple","banana","cherry","kiwi","mango "]

print(fruit[:2]) #Print the elements of the list from index 0 to 2

print(fruit[2:]) #Print the elements of the list from index 2 to the end

print(fruit[-2:]) #Print the last two elements of the list

print(fruit[2]) #Print the elements of the list from index -3 to -1

print(fruit[::-1]) #Print the list in reverse order

print(fruit[0:2])   # Print the first two elements of the list

fruit[0:2]=["orange","grapes"] #Replace the values of index 0 and 1 with "orange" and "grapes"
print(fruit)

fruit.append("watermelon") #Add "watermelon" at the end of the list
print(fruit)

fruit.insert(1,"papaya") #insert "papaya" at index 1
print(fruit)

fruit.remove("kiwi") # Remove the first occurrence of "kiwi"
print(fruit)

fruit.pop(1)  # Remove the element at index 1 (which is "papaya" after the previous operations)
print(fruit)

fruit.sort()  #sort the list in ascending order
print(fruit)

fruit.sort(reverse=True)  #sort the list in descending order
print(fruit)

fruit.clear()  #Remove all the elements from the list
print(fruit)

