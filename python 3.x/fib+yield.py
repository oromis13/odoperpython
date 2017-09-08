def fib(n):

     a=0
     b=1
        
     while (n>0):

        yield a

        a,b=b,a+b
        n=n-1

        
    
        
     

x=fib(6)

for i in x:
    print (i)

    
