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

'''Student.pop('CGPA')
print(Student)'''

del Student['CGPA']
print(Student)