#PRINT ALL PRIME FACTORS IN SORTED ARRAY
n=120
i=2
while n!=1:
    while n%i==0:
        print(i)
        n=n//i
i=i+1



#SECOND LARGEST
arr=[2,5,7,9]
first=-1
second=-1
for i in arr:
    if i>first:
        second=first
        first=arr
    elif arr> second and arr<first:
        second=arr
print(second)



#ARRAY LEADERS
