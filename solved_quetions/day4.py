#LENGTH OF THE LAST WORD
s= " start coding here "
count=0
for i in range(len(s)-1,-1,-1):
    if s[i]==" ":
        if count>0:
            break
        else:
            count+=1
print(count)  



#SUM OF ALL DIVISORS
num=36
sum=0
for i in num:
    if i%num==0:
        sum=sum+i
        if i!=num/i:
            sum=sum+num/i
print(sum) 




#PERFECT NUMBERS
n=28
sum=0
for i in range(i,int(math.sqrt(n))+1):
    if i%n==0:
        sum=sum+i
        if i!=n/i:
            sum=sum+n/i
sum=sum-n
if sum==n:
    print(True)
else:
    print(False)



#PRINT ALL PROIME NUMEBRS FORM 2 TO 100
for i in range(2,n+1):
    isprime=True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            isprime==False
            break
if isprime==True:
    print(i)   


#HCF AND GCD
a=28
b=38
while a!=0:
    temp=a
    a=b%a
    b=temp
    print(b)

#DIGITAL ROOT
n=693
sum=0
while n>9:
    for i in str(n):
         sum=sum+int(i)
         n=sum   
print(sum)


#REPLACE 0 TO 5
n=1004
ans=" "
for i in n:
    if n=="0":
        ans=ans+"5"
    else:
        ans+=i
print(int(ans))



#ARMSTRONG NUMBER
n=153
original=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit**3
    n=n//10
if sum==original:
    print("Armstrong number")
else:
    print("Not an armstrong number")


