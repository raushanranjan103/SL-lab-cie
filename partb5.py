from functools import reduce
data=[]
name=input("enter the file name with extension");
with open(name,"r")as file:
     data=(file.readline().rstrip("\n")).split(" ")
di={}
for i in data:
    di[i]=data.count(i)
s=sorted(di.items(),key=lambda it:it[1],reverse=True)
wordlen=[]
for i in range(10):
    try:
        w=s[i]
        word=w[0]
        no=w[1]
        wordlen.append(len(word))
        print("word:",word,"frequency:",no,"length:",len(word))
    except IndexError:
        print("File has less than 10 words")
        break;
for i in wordlen:
     print(i,end=" ")
print(end='\n')
total_len=reduce(lambda x,y:x+y,wordlen)
avg_len=total_len/len(wordlen)
print("average length of top 10 words:",avg_len)

sq=[i*i for i in range(20) if i%2==0]
print("squares of all odd numbers upto 20:")
for i in sq:
    print(i,end=" ")
print(end='\n')
    
