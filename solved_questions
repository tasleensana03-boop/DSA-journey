#even and odd

n=[4,5,6,3]
for i in n:
    if i%2==0:
        print(i)
for i in n:
    if i%2!=0:
        print(i)



#largest number
num=[4,8,2,9,5]
largest=0
for i in num:
    if i>largest:
     largest=i
print(largest)  



#smalllest number
num=[7,3,9,2,5]
smallest=None
for i in num:
    if smallest is None or i<smallest:
        smallest=i
print(smallest) 


#how many even and odd numbers present in a list

num=[4,7,2,9,6,3,8]
even=0
odd=0
for i in num:
    if i%2==0:
        even+=1        
for i in num:
    if i%2!=0:
        odd+=1
print("even=",even)
print("odd=", odd)



#sum of even numbers
num=[4,7,2,9,6,3,8]
sum=0
for i in num:
    if i%2==0:
        sum=sum+i
print(sum)     


#second largest
num=[10,5,8,20,15]
first=-1
second=-1
for i in num:
    if i>first:
        second=first
        first=i
    elif i>second and i<first:
        second=i
print(second) 



#frequency of a number
#num=[2,3,4,2,6,2,7]
#n=int(input("enter a number:"))
#count=0
#for i in num:
#    if i == n:
#       count=count+1
#print(count) 



#reverse a string
num=3452
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

num=[3,4,5,6]
for i in range(len(num)-1,-1,-1):
    print(num[i], end=" ")


#sum of all elements
num=[3,4,56,7]
sum=0
for i in num:
    sum=sum+i
print(sum)   



#remove duplicates
num=[4,3,3,5,7,8,4]
elements=set(num)
print(elements)


num=[4,3,3,5,7,8,4]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]==num[j]:
            print(num[i])



#find missing element

arr=[1,2,3,5]
n=len(arr)+1
sum1=0
for i in range(1,n+1):
    sum1=sum1+i
sum2=0
for num in arr:
    sum2=sum2+num
sum=sum1-sum2
print(sum)




#move all zeroes to end

num=[0,1,0,3,12]
j=0
for i in range(len(num)):
    if num[i]!=0:
        num[i],num[j]=num[j],num[i]
        j+=1
print(num)   



#palindrome or not

n=1221
ans= str(n)[::-1]
print(ans)

n=1221
original=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if original==rev:
    print("number is palindrome") 
else:
    print("not a palindrome")   




#find largest and smallest

n=[10,5,8,20,3,15]
largest=n[0]
smallest=n[0]
for i in n:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print(smallest)
print(largest)    
    



