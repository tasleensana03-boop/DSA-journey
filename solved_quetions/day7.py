s#SUM OF TWO NUMBERS
# a=10
# b=20
# print(a+b)


#CHECK EVEN OR ODD
n=[3,4,5,67,2]
even=0
for i in n:
    if i%2==0:
        even=even+1
        print(n,"even")
    else:
        print(n,"odd")


#largest of two numbers
# n=[6,7,8,9,43]
# largest=0
# for i in n:
#     if i>largest:
#         largest=i
# print(largest)  


#POSITIVE OR NEGATIVE
# n=[4,5,-2,6,-7]
# positive=0
# for i in n:
#     if i>positive:
#         print("positive")
#     else:
#         print("negative")


 #LEAP YEAR YEAR CHECK
n=2026
if(n%100==0 and n%4==0)or(n%100!=0 and n%400!=0):
    print("leap year")
else:
    print("not a leap year")



 #SWAP TWO VARIABLES
a=10
b=20
temp=a
a=b
b=temp
print(a,b)

#factorial of a number
n=5
fact=1
for i in range(1,n+1,+1):
    fact=fact*i
print(fact)


#REVERSE A NUMBER
n=456
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)


#FIBONACCI NUMBER
num=5
a=0
b=1
for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c

#palindrome number check
num=123
original=num
check=0
while num>0:
    digit=num%10
    check=check*10+digit
    num=num//10
if original==check:
    print("palidrome")
else:
    print("not a palindrome")


#ARMSTRONG NUMBER
n=153
original=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit**3
    n=n//10
if original==sum:
    print("armstrong")
else:
    print("not armstrong")


#PRIME NUMBER CHECK
n=5
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1

if count==2:
    print("prime number")  
else:
    print("not a prime number")  



#PRINT ALL PRIME NUMBERS
n=100
# for i in range(2,n+1):
#     isprime=True
#     for j in range(2,int(math.sqrt(i))+1):
#         if i%j==0:
#             isprime==False
#             break
# isprime==True
# print(i)


#TABLE OF NUMBER
n=8
for i in range(1,11):
    print(n,"x",i,"=",n*i)  


#sum of digits of number
n=567
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print(sum)


#PRINT NUMBER 1 TO 100
n=100
def print_numbers(n):
    if n>100:
        return
    print(n)
    print_numbers(n+1)
print_numbers(1)


