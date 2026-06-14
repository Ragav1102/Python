print('.....Calculator.....')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Modulus')
print('6. Floor Division')
print('7. Exponentiation')

sel=(int(input('Enter your choise (1-7) : ')))

num1=int(input('Enter your number 1 : '))
num2=int(input('Enter your number 2 : '))


if sel==1:
    print(num1, "+" ,num2, "=", num1 + num2)
elif sel==2:
        print(num1, "-" ,num2, "=", num1 - num2)
elif sel==3:
        print(num1, "*" ,num2, "=", num1 * num2)
elif sel==4:
    if num2==0:
        print("Cannot divide by 0")
    else:
        print(num1, "/" ,num2, "=", round( num1 / num2,2))
elif sel==5:
     if num2==0:
        print("Cannot divide by 0")
     else:
        print (num1, "%" ,num2, "=", num1 % num2)
elif sel==6:
    if num2==0:
        print("Cannot divide by 0")
    else:
        print(num1, "//" ,num2, "=", num1 // num2)
        
elif sel==7:
    if num2==0:
        print(num1, "**" ,num2, "=", '1')
    else:
        print(num1, "**" ,num2, "=", num1 ** num2)
else:
    print('Invalid')



