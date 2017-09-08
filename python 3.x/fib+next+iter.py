class fib():

    def __init__(self,n):
        self.a=0
        self.b=1
        self.num=n
        self.count=0

    def __iter__(self):
        
        return self

    def __next__(self):

        
              
               if(self.count>self.num):
                   raise StopIteration

               elif(self.count==0):

                    self.count+=1
                    return self.a
               

               else:
                   self.a,self.b=self.b,self.a+self.b
                   self.count+=1

                   return self.a
                                
         

        
           





for i in fib(6):
    print (i)
    

        





        
