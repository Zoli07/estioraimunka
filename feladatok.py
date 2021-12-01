#Első feladat

for i in range(1,11):
    print(i,"---",1/i)

#Második feladat

a=int(input("Kérem a hatványalapot: "))
b=int(input("Kérem a hatványkitevőt: "))

hatvanyertek=a**b

print(hatvanyertek)

#Harmadik feladat

while True:
    c=int(input("Kérem egy pozitív számot: "))
    if c<=0:
        print(c)
    else:
        break

#Negyedik feladat

a=int(input("Kérem az első számot: "))
b=int(input("Kérem a második számot: "))

print(-(a-b))

#Ötödik feladat

osszeg=0
for i in range (0,99):
    szam=int(input("Kérek egy számot: "))
    osszeg=osszeg+szam
    if osszeg>=100:
        break