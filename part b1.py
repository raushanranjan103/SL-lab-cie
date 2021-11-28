m=[x for x in range(1,10) ]
m.append(1)
m.append(2)
m.append(3)
m.append(4)
print(m)
b=[set(m)]
print(list(b))
t=[x for x in m if x%2==0]
print(t)
t.reverse()
print(t)
from collections import Counter
def word_count(fname):
    with open (fname) as f:
      return Counter(f.read().split())
print("the number of words are",word_count("test.txt")) 
z=[]   
def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]

def choice():
    
    flag=True
    while flag:
     print("1>insert into list 2>get the max element 3>exit")
     n=int(input())
     if n==1:
        print("enter the element wanted to insert")
        r=int(input())
        z.append(r)
     elif n==2:
        print(Max(z))
     else: 
       flag=False
       break;
     default:print("wrong input")
choice();

    
        
       
     
