# 2 numbers
#__def largest of 3 numbers
#___def to find num is even
#___def greet GM(name)

#___def greet GM(name)
# def greet():
#     name=input("enter name:")
#     print("Good morning",name)
# greet()


#def largest of 3 numbers
def largest():
    first = 7
    second =5
    third = 8
    if(first>second and first>third):
        print(first)
    elif(second>first and second>third):
        print(second)
    else:
        print(third)
largest()


#__Add 2 numbers
def num():
    n1=3
    n2=4
    print(n1+n2)
num()



#find square of number
def square():
    a=10
    print(a**2)
square() 



#___def to find num is even

def even_or_odd():
    a=10
    if a %2==0:
        print("Even")
    else:
        print("odd")
even_or_odd()




#Different types of function:
#	1.No i/p  & no o/p:
	
def square():
	n=5*5
	print(n)
square()
  

 # 2.no i/p & o/p
def square ():
    n=5*5
    return n
print(square())


# 3.i/p & no o/p
def square(n):
    res=n*n
    print(res)
square(3)


 #4.i/p & o/p
def square(n):
    return n*n
res=(square(16))
print(res)




#no i/p &  no o/p
def even_or_odd():
    a=12
    if(a%2==0):
        print("Even")
    else:
        print("odd")
even_or_odd()


# 2.no i/p & o/p

def even_or_odd():
    a=12
    if(a%2==0):
        return "Even"
    else:
        return "odd"
print(even_or_odd())    



# 3.i/p & no o/p

def even_or_odd(a):
    if(a%2==0):
        print("Even")
    else:
        print("odd")
even_or_odd(12)


#4.i/p & o/p
    
def even_or_odd(a):
    if(a%2==0):
        return "Even"
    else:
        return "odd"
print(even_or_odd(12))