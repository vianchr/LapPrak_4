def cek_digit_belakang(a,b,c):
    bil_1=a%10 
    bil_2=b%10 
    bil_3=c%10
    if bil_1==bil_2 or bil_1==bil_3 or bil_2==bil_3:
        return True
    else: return False

a=int(input("masukan bilangan pertama: "))
b=int(input("masukan bilangan kedua  : "))
c=int(input("masukan bilangan ketiga : "))
print (cek_digit_belakang(a,b,c))
