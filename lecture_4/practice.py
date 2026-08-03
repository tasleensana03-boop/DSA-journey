#sets
set1={2,4, "hello",2,"abhinav","hello",2,4}
print(type(set1))
print(len(set1))

list=[3,4,6,3,2,4,56,7,5,2,2,4,6,23,2,45,5]
set1=set(list)
print(len(set1))
print(set1)


set1={"hello", 2, 4, "abhinav"}
set1.add(100)
set1.add("hello")
print(set1)
    

set1={"hello", 2, 4, "abhinav"}
set1.remove(2)
print(set1)
    
set1={"hello", 2, 4, "abhinav"}
set1.discard(4)
print(set1)
   
set1={"hello", 2, 4, "abhinav"}
set1.discard("hii")
print(set1)

set1={"hello", 2, 4, "abhinav"}
set1.clear()
print(set1)
     
set1={1,3,4,5,6}
set2=set1
set2.add(2)
print(set1, set2)

set1={1,3,4,5,6}
set2=set1.copy()
set2.add(2)
print(set1, set2)

set1={1,3,4,5,6,4,5,3,8}
set2={9,8,7,6}
print(set1 .union(set2))

set1={1,3,4,5,6,4,5,3,8}
set2={9,8,7,6}
print(set1 .intersection(set2))

set1={1,3,4,5,6,4,5,3,8}
set2={9,8,7,6}
print(set1&set2)


#dictionaries

dict1={1:"abinav", "hello":200}
print(type(dict1))
print(len(dict1))

dict1={1:"abinav", "hello":200,(1,3,4):"tasleen"}
print(type(dict1))
print(len(dict1))













