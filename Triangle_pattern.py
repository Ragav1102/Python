n=int(input("Enter the number : "))
for i in range (1,n+1):  #right angle triangle pattern
    print(i*"*")

for i in range(1,n+1):  #mirrored right angle triangle pattern
    print((n-i)*" "+i*"*")

for i in range(1,n+1):  #reverse right angle triangle pattern
    print("*"*(n-i+1))

for i in range(1,n+1):  #mirrored reverse right angle triangle pattern
    print((i-1)*" "+(n-i+1)*"*")

for i in range(1,n+1):  #pyramid pattern
    print(" " * (n - i) + "* " * i)
    
for i in range(1,n+1):  #inverted pyramid pattern
    print(" " * (i - 1) + "* " * (n - i + 1))

for i in range(1, n + 1):  #diamond pattern 
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)