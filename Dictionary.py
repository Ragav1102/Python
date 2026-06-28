Student={
    "Name":"Ragav",
    "age":23,
    "CGPA":7.8,
    "City":"Banglore"
}
print(Student)

print(Student["age"])

Student["age"]=24
print(Student)


del Student['CGPA']
print(Student) # Print the dictionary after deleting the 'CGPA' key

Student.pop("City")
print(Student)

print(Student.keys()) # Print all keys in the dictionary

print(Student.items()) # Print all items in the dictionary