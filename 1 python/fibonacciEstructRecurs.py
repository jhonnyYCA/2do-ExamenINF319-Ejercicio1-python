# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




a=0
b=1

for i in range (10):
    print (a)
    f=a+b
    a=b
    b=f




def fibo(n):
    if n<2:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
    
    
for i in range (10):   
    print (fibo(i))    
    

