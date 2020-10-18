a=int(input("prima nota "))
b=int(input("a doua nota "))
c=int(input("a treia nota "))
if c>8:
    print(a, b, c) 
if c<8:
    if a>b:
        print(a)
    if b>a:
        print(b)
    