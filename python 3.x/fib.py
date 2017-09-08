def fib(n):

     a=0
     b=1
     seq=[0]

     while (n>1):

        a,b=b,a+b
        
        seq.append(a)

        n=n-1

     return seq



print(fib(6))

        
         
         
