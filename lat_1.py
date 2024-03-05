def cek_angka(a,b,c):
    if (a!=b!=c!=a)and(a+b == c or b+c == a or c+a == b):
        return True
    else: 
        return False
print (cek_angka(1,2,3))
print (cek_angka(2,2,3))
print (cek_angka(5,3,1))
print (cek_angka(7,2,5))

#bentuk function apabila memakai lambda
#cek_angka= lambda a,b,c: True if (a!=b!=c!=a and (a+b == c or b+c == a or c+a == b)) else False

    