#Arithmetic operator
print(3+3)  #6
print(3-3) #0
print(3*3) #9
print(1 / 3) #0.3333333333333333
print(100 % 30) #10
print(3 ** 3) #9
print(10 // 3) #3

# Comparison operator
print(11 ==10) #false
print(11 !=10)
print(11 > 10)
print(11 <10)
print(11 >= 10) #tRUE
print(11 <= 10) #False

# Assignment operator
a = 10
print(a)  #10
a += 10  
print(a) #20
a -= 10
print(a)  #10
a *= 10
print(a) #100
a /= 10
print(a) #10.0
a /= 10 
print(a) #1.0
a %=10 
print(a) #1.0
a **=2
print(a)
a = 2
a //= 2
print(a)


#Logical operator

a = False
b = False
print(a and b) # False
print(a or b) # False
print(not a) # True
print(not b) #True

a = (5 > 3) and (4 < 6) #True
a = (5 < 3) or (4 < 6)  #true
a = not (5 > 3) # false


# identity operator
a = 10
b = 10
print(a is b) # True
print(a is not b) #True
print(a == b) #True
print(a != b) #false

#Membership operator
a = [1,2,3,4,5]
print(1 in a) #true
print(6  in a) #false
print(1 not in a) #false
print(6 not in a) #true

#Bitwise operator

a = 2
b = 3
print(a & b)  #2
print(a | b) #3
print(a ^ b) #1
a = 5
print(~a) #-6
print(a << b) #40
print(a >> b) #0

