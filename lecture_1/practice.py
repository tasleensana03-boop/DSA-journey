monday= 87               
tuesday=76

avg=(monday+tuesday)/2
print(avg)


age=65                                         #type of class
print(age,type(age))
height=5.9
print(height,type(height))
c=2+3j
print(c,type(c))

ismarried=False
isgraduated=True                                 #boolean
print(ismarried,type(ismarried))
print(isgraduated,type(isgraduated))



first_name= input("enter your first name:")
last_name= input("enter your last name:")       # taking input from user input
print(first_name)



age=int(input())                               
height=float(input())                           #converting datatypes
print(age,height)



full_name="tasleen sana"
age=20
adress="bangalore"
print(full_name, age, adress)



#take input of age on the basis of age print the eligibility
age=int(input())

if(age>=18):
    test=input()
    test=="PASS"
    print("eligible for driving license")
else:
    print("not eligible for driving license")    



    temp=int(input("enter temparature:"))

    if temp<=50 and temp>=25:                  #conrol statements
        print("hot")
    elif temp<=24 and temp>=10:
        print("cold")
    elif temp<10:
        print("extremly cold")



age=int(input("enter your age:"))      
result= "Eligible" if age>=18 else "Not eligible"    #ternary operators
print(result)

#while loop
i=0

while i<5:
    print(i, end=" ")
    i+=1

#for loop
for i in range(1,11):
    print(i,end=" ")
    print()

for i in range(5,11):
    print(i,end= " ")
    print()

for i in range(1,11,2):
    print(i,end= " ")
    print()


for i in range(20,0,-1):
    print(i,end= " ")
    print()


#functions
def printName(name):
    print(name)
printName("tasleen")

def addTwoNumbers(a,b):
    sum =a+b
    return sum
ans=addTwoNumbers(4,7)
print(ans)

    











