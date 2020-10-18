zn=int(input("Introduceti ziua nasterii "))
ln=int(input("Introduceti luna nasterii "))
an=int(input("Introduceti anul nasterii "))
zc=int(input("Introduceti ziua curenta "))
lc=int(input("Introduceti luna curenta "))
ac=int(input("Introduceti anul curent "))
v=ac-an
if lc<ln: 
    print(v-1,"ani")
elif lc==ln:
    print(v,"ani")
elif zc>zn:
    print(v,"ani")
elif zc<zn:
    print(v-1,"ani")
elif lc<ln:
    print(v-1,"ani")



    