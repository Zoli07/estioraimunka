a=int(input("Kérek egy számot!"))
b=int(input("Kérek egy másik számot!"))
print(a+b)


import random
list=[]
for i in range(10):
    list.append(random.randrange(1,30))

szamok=len(list)
összeg=sum(list)
atlag=összeg/szamok
print(atlag)


minimum=min(list)
maximum=max(list)
print(minimum)
print(maximum)

#eldöntés tétele
vane=False
for i in list:
    if i==9:
        vane=True

if vane==True:
    print("Van  benne 9-es!")

else:
    print("Nincs benne 9-es!")

print(list)