
#0,1,1,2,3,5,8
def fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibonacci(n-1) + fibonacci(n-2))  
 
nterms = int(input("n= "))  


print("Fibonacci sequence:")  
for i in range(nterms):  
    print(fibonacci(i))  
