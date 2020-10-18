a=int(input("Introduceti primul nr "))
b=int(input("Introduceti al doilea nr "))
c=int(input("Introduceti al treilea nr "))
if (a>0) and (b>0) and (c>0):
    if b>c:
        print(b)
    if b<c:
        print(c)
elif (a<0) or (b<0) or (c<0):
    print(a+b)