umur = int(input("Masukkan Umur : "))

if 1 <= umur < 5:
    print("Anda Memasuki Klasifikasi Balita")
elif 5 <= umur < 13:
    print("Anda Memasuki Klasifikasi Anak-Anak")
elif 12 <= umur < 25:
    print("Anda Memasuki Klasifikasi Remaja")
else:
    print("Anda Memasuki Klasifikasi Dewasa")