import math

print(math.sqrt(25))

print("pi Value", math.pi)

print("circum",2*math.pi*7)

print("area", math.pi*7*7)

print(math.tau)

print(math.inf)

print(-math.inf)

print(math.ceil(2.33))  #Round off

print(math.floor(2.66)) 

print(math.trunc(3.7))

print(math.fabs(-2.44))  #convert -ve value to +ve

print(math.factorial(6))

print(math.gcd(24,60))

print(math.lcm(240,256))

print(math.comb(10,3))  #n!/r!(n-r)!

print(math.perm(15,4))   #n/(n-r)!

print(math.pow(3,3))

print(math.log(8,2))  #log base 2 of 8

print(math.radians(360))  #convert degree to radians

print(math.degrees(3.14))  #convert radians to degree

print(math.sin(math.radians(90)))  #sine of 90 degree

print(math.sin(0))  #sine of 0 degree

print(math.tan(45))  #tan of 45 degree

print(math.degrees(math.asin(1)))  #inverse sine of 1

print(math.hypot(3,4))  #hypotenuse of right angle triangle


a=[4,5,6,7,8]

print(math.fsum(a))  #sum of list elements

print(math.prod(a))  #product of list elements

print(math.fmod(10,3))  #remainder of 10/3

print(math.modf(7.5))  

print(math.isfinite(10))  #check if number is finite

print(math.isinf(10))  #check if number is infinite

print(math.isinf(math.inf))  #check if number is infinite

a=0.1+0.2
b=0.3
print(a==b)

print(math.isclose(a,b))  #check if a and b are close enough to be considered equal

print(math.copysign(3,-4))  #return a with the sign of b

n=6
print(math.prod(range(1,n+1)))  #factorial of n using prod and range

print(math.gamma(6))  #gamma(n) = (n-1)! for positive integers

