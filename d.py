
a=int(input("a:"))
b=int(input("b:"))
for i in range(1,a):
   if((a%i==0 & b%i==0)):
     gcd=i
     print(gcd)
