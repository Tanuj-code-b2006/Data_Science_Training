"""
n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
Sum=0

for i in range(n1,n2+1):
    if (i%2==0):
        print(i)
        Sum+=i
print("The Sum is :",Sum)


"""

#Grading System
"""
num=int(input("Enter number:"))
if (num==100 or num>=80):
    print("Grade:A")
elif (num<80 and num>=50):
    print("Grade:B")
elif (num<50 and num>=30):
    print("Grade:C")
elif (num<30):
    print("Failed")   
else:
    print("Invalid Entry")
"""


#Factorial
"""
n=int(input("Enter any number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial =",fact)
"""

#comparison
"""
lst=[20,21,70,80,64,36,90,9]
count=0
max_int=0
for i in range (0,len(lst)):
        if (lst[i]>max_int):
            max_int=lst[i]
print(max_int)
"""

#star patterns
"""
for i in range(0,9):
    print(i*"*")
"""

"""
#3
n=int(input("Enter number:"))
for i in range(1,n):
    print(i*"*")
for j in range(n,1,-1):
    print(j*"*")

"""




#perimeter and area of circle if radius is given
'''
r=int(input("Enter Radius:"))
print("perimeter:",2*3.14*r)
print("AREA:",3.14*r*r)

'''








