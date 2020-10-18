g=int(input("Introduceti nr de gaina =>"))
b=int(input("Introduceti nr de boabe =>"))
if b%(g+1)==0:
    print(b//(g+1),"egalitate")
else:
    print(b%(g+1), "primeste curcanul Clapon")
