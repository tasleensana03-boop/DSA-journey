#PATTERN MATCHING
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(j+64), end=" ")
    print() 


n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

n=4
for i in range(n,0,-1):
    for j in range(1,n-i+2):
         print(i,end=" ")
    print() 


n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print() 


n=4
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()      


n=4
for i in range(1,n+1 ):
    for j in range(1,i+1):
        print(chr(i+64),end=" ")
    print()        


n=4
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()    
    


n=4
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()    
    
