a=int(input("primul nr crt "))
b=int(input("al doilea nr crt "))
c=int(input("al treilea nr crt "))
if (a>b) and (a>c):
    print(a)
if (b>a) and (b>c):
    print(b)
if (c>a) and (c>b):
    print(c)
if (a==b) and (a>c) and (b>c):
    print("primul si al doilea crt sunt egali")
if (a==c) and (a>b) and (c>b):
    print("primul si al treilea crt sunt egali")
if (b==c) and (b>a) and (c>a):
    print("al doilea si al treilea crt sunt egali")
if (b==a) and (a==c):
    print("toate crt sunt egali")