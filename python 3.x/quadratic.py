import math

class root:
     def __init__(self,r = 0,i = 0):
        self.real = r
        self.img = i
        
class quad:
     def __init__(self,a = root(),b = root()):
         self.r1=a
         self.r2=b
     
    

def Qroots (a,b,c):
    x=quad()

    
    
    d=b*b-4*a*c

    if (d==0):
        x.r1.real=x.r2.real=-b/2*a
        x.r1.img=x.r2.img=0
    

    elif (d>0):
         x.r1.img=x.r2.img=0
         x.r1.real=(-b+math.sqrt(d))/(2*a)

         x.r2.real=(-b-math.sqrt(d))/(2*a)


    else:
        x.r1.real=x.r2.real=-b/2*a
        x.r1.img=math.sqrt(-d)
        x.r2.img=-math.sqrt(-d)


    return x




print("enter coefficients:")

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

A=quad()
A=Qroots(a,b,c)

if (A.r1.img==0):
    print("roots are :",A.r1.real," and ",A.r2.real)

else:
    print("roots are:",A.r1.real,"+j",A.r1.img,"and",A.r1.real,"+j",-A.r1.img)





    
    
         
         
        

    

    
