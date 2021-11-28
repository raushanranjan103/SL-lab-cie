conversions=[]
def ctof():
    print("enter the  temperatre in celcius")
    c=float(input())
    f=(c*9/5.0)+32
    print(f"the temperatur in fahrenheit will be ",f);
    conversions.append((c,f))
def ftoc():
    print("enter the  temperatre in fahrenehit")
    f=float(input())
    c=(f-32)*5/9.0
    print(f"the temperatur in celcius will be ",c);
    conversions.append((f,c))
def ctok():
    print("enter the  temperatre in celcius")
    c=float(input())
    k=c+273.0
    print(f"the temperatur in kelvin will be ",k);
    conversions.append((c,k))
def ktoc():
    print("enter the  temperatre in kelvin")
    k=float(input())
    c=k-273.0
    print(f"the temperatur in celcius will be ",c);
    conversions.append((k,c))
def sortConversions():
    print('1. By From value')
    print('2. By To value')
    x = (int)(input('Enter your choice : '))
    
    if x == 1 :
        conversions.sort()
    elif x == 2:
        conversions.sort( key = lambda x : x[1])
        
    print(conversions)
def main():
    flag=True
    while(flag):
     print("1>c->f\n 2>f->c\n 3>c->k\n4>k->c\n 5>sorted values\n 6>exit")
     z=int(input())
     if z==1:
         ctof();
     elif z==2:
         ftoc();
     elif z==3:
         ctok();
     elif z==4:
         ktoc();
     elif z==5:
          sortConversions();
     elif z==6:
          flag=False
          break;
     else:
           print("Wrong input\n")
main()

   
    
    