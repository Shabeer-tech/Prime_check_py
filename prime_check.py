n=int(input("enter value :"))
if n>1:
    for i in range(2,n):
        if(n%i == 0):
            print("not prime")
            break
    else:
            print("prime")
else:
            print("not")
 
   
        