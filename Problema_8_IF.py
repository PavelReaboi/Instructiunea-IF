a=int(input("Introduceti un nr "))
b=int(input("Introduceti al doilea nr "))
if (a%2==0) and (b%2==0):
    if a>b:
        print(a)
    if a<b:
        print(b)
elif (a%2==0) and (b%2!=0):
    print(a)
elif (a%2!=0) and (b%2==0):
    print(b)
elif (a%2!=0) and (b%2!=0):
    print("nr nu este par")
