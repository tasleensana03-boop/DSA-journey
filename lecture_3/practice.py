#lists
from operator import index


names=["tasleen", "sana","hani",29,"tasleen"]
print(names)

names=["kausar", "ayesha", "True","firdouse",45,"&"]
print(names)

names=["tasleen", "sana","hani",29,"tasleen"]
print(type(names))

#indexing
names=["tasleen", "sana","hani",29,"tasleen"]
print(names,index(3))


name=["tasleen", "sana","hani",29,"tasleen"]
print(len(names))

list1=[1,2,3,5,7]
list1.append(4)
print(list1)

list1=[1,2,3,5,7]
list1.append(4)
list1.append([1,2,3])
list1.extend([1,2,3])
print(list1)

list1=[3,4,6,57,8,9,3]
list1.insert(4,100)
print(list1)

list1=[1,3,5,8,9,0]
list1.remove(0)
print(list1)

list1=[5,8,9,0,3,4,]
list1.pop(5)
print(list1)

list1=[5,6,78,9,8,3,7]
list1.clear()
print(list1)

list1=[98,2,0,87,65]
print(max(list1))
print(min(list1))

list1=[4,5,6,7,8,9,4,3,5,6,7,1,1,5]
print(list1.count(1))
print(list1.count(5))
print(list1.count(7))


list1=[4,5,6,7,8,9,4,3,5,6,7,1,1,5]
(list1.sort())
print(list1)

list1=[4,5,6,7,8,9,4,3,5,6,7,1,1,5]
(list1.reverse())
print(list1)

list1=[4,5,6,7,8,9,4,3,5,6,7,1,1,5]
print(list1.index(9))

list1=[1,2,3,4]
list2=list1
list2.append(5)
print(list1)
print(list2)

list1=[1,2,3,4]
list2=list1.copy()
list2.append(5)
print(list1)
print(list2)

list1=[6,7,8,98,67,45,23]
print(list1[2:4])
print(list1[2:6])
print(list1[2:6:3])
print(list1[:3])
print(list1[:])
print(list1[::-1])


#tuples
tuple1=(6,7,8,98,67,45,23)
print(tuple1[:3])
print(tuple1[2:4])
print(tuple1[:3])
print(tuple1[2:6])
print(tuple1[2:6:3])
print(tuple1[:3])
print(tuple1[:])
print(tuple1[::-1])


#Strings
name="tasleen"
place="karnataka"
college="bangalore"
print(name,type(name))

name="tasleen"
name +="sana"
place="karnataka"
college="bangalore"
print(name,type(name))

name="Tasleen"
name +="Sana"
place="karnataka"
college="bangalore"
print(name,type(name))
print(name.lower())
print(name.replace("a","s"))
print(name.startswith("tasleen"))
print(ord("a"))





