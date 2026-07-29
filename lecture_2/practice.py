#time complexty

n=10
x=3
for i in range(n):     
  if i==x:
    break
  print(i,end=" ") 


#linear complexity
for i in range(n/2):
  print(i,end=" ")

for i in range(n+100):
  print(i,end=" ")

for i in range(n*2):
  print(i,end=" ")


#constant time 
for i in range(1000):
  print(i,end=" ")


#quadratic time
for i in range(n**2):
  print(i,end=" ")

for i in range(n):
  for j in range(n):
    print(i,j)

#lograthmic time
i=1
n=100
while i<=n:
  print(i,end=" ")
  i*=2
      

#recursion
#base case
def printNumbers(i,n):
  if i>n:
    return
#recursive case
print(i,end=" ")
printNumbers(i+1,n)
printNumbers(1,5)

#factorial with recursive
def fact(n):
  if n==0:
    return 1
  return n*fact(n-1)
print(fact(4))


#recursive tree
def fib (self, n: int) -> int:
  if n==0 and n==1
  return n
  return fin(n-1)+fib(n-2) 