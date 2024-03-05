# Buatlah fungsi-fungsi konversi suhu menggunakan lambda function. Fungsi-fungsi
# yang harus anda implementasikan:
# Celcius to Fahrenheit. F = (9/5) ∗C +32
# Celcius to Reamur. R = 0.8 ∗C
# Berikan contoh penggunaannya untuk test-case berikut ini:
# Input C = 100. Output F = 212.
# Input C = 80. Output R = 64.
# Input = 0. Output F = 32.
convert ={
    "Farenheit":lambda C: (9/5) *C +32,
    "F":lambda C: (9/5) *C +32,
    "Reamur" : lambda C:0.8 *C,
    "R": lambda C:0.8 *C
}

C=input("masukan suhu dalam celcius:")
skala=input("ubah suhu ke dalam satuan Farenheit/Reamur (F/R): ")
try:
    C=int(C)
    print (convert[skala](C))
except:
    print ("anda salah memasukan input")
    