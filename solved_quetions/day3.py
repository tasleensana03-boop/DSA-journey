#REMOVING DUPLICATES FROM SORTED LIST

num=[1,1,2,3,3,4]
j=0
for i in range(len(num)):
    if num[i] != num[j]:
        j += 1
        num[j] = num[i]
print(num[:j+1])


#MOVE ALL EVENN NUMBERS TO THE BEGINNING
num=[1,1,2,3,3,4,4]
j=0
for i in range(len(num)):
    if num[i]%2==0:
        num[i],num[j]=num[j],num[i]
        j+=1
print(num)        



#MOVE ALL NEGATIVE TO THE BEGINNING
num=[9,6,-4,7,-2,-3]
j=0
for i in range(len(num)):
    if num[i]<0:
        num[i],num[j]=num[j],num[i]
        j+=1
print(num)  


#FIND THE FIRST NON REPEATING ELEMENT
num=[4,5,1,2,1,4,5]
for i in range(len(num)):
    count=num.count(num[i])
    if count==1:
        print(num[i])

num=[4,5,1,2,1,4,5]
for i in range(len(num)):
    count=0
    for j in range(len(num)):
    
        if num[i]==num[j]:
            count=count+1
    if count==1:
        print(num[i])
        break

               
 # FIND THE PAIR WITH A GIVEN SUM
num=[2,7,11,15]
target=9
for i in range(len(num)):
    for j in range(len(num)):
        if num[i]+ num[j]==target:
            print(num[i],num[j])    


#FIND THE LONGEST INCREASING CONSECUTIVE SEQUENCE
num=[1,2,3,2,4,5,6]   
current=1
longest=1          
for i in range(len(num)-1):
    if num[i+1]==num[i]+1:
        current=current+1
        if current>longest:
            longest=current
    else:
        current=1
print(longest) 



#MAXIMUM SUBARRAY
num=[-2,1,-3,4,-1,2,1,-5,4]
max_sum=0
for i in range(len(num)):
    current_sum=0
    for j in range(i,len(num)):
        current_sum=current_sum+num[j]
        if current_sum>max_sum:
            max_sum=current_sum

print(current_sum)  








  

