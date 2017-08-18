import re

def makeD(i_str):

                 
                 a=iter(re.split(r'[=;]', i_str))
                 return dict(zip(a,a))




str="a=b;c=d;e=f";


print(makeD(str))
                
