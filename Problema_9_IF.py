xa=int(input("Introduceti nr de bile albe mici "))
xr=int(input("Introduceti nr de bile rosii mici "))
xv=int(input("Introduceti nr de bile verzi mici "))
ya=int(input("Introduceti nr de bile albe mari "))
yr=int(input("Introduceti nr de bile rosii mari "))
yv=int(input("Introduceti nr de bile verzi mari "))
tx=xa+xr+xv
ty=ya+yr+yv
if tx>ty:
    print("Mici")
elif tx==ty:
    print("Egal")
else:
    print("Mari")
if (xa+ya>xr+yr) and (xa+ya>xv+yv):
    print("Albe")
if (xr+yr>xa+ya) and (xr+yr>xv+yv):
    print("Rosii")
if (xv+yv>xa+ya) and (xv+yv>xr+yr):
    print("Verzi")
