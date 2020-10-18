a=int(input("prima latura are "))
b=int(input("a doua latura are "))
c=int(input("a treia latura are "))
if (a<b+c) and (b<a+c) and (c<a+b):
    print("DA")
else:
    print("NU")