# try except digunakan untuk menangani error atau exception yang mungkin terjadi dalam program kita. Dengan menggunakan try except, kita bisa menangkap error yang terjadi dan memberikan penanganan yang sesuai, sehingga program tidak akan berhenti secara tiba-tiba.

try:
    number = 10/0  # ini akan menyebabkan ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Terjadi error: {e}")
else:
    print("Tidak ada error, kode ini akan dieksekusi jika tidak ada error")
finally:
    print("Ini akan dieksekusi selalu, baik ada error maupun tidak")    

try:
    number = int(input("Masukkan angka: "))  # jika input bukan angka, akan menyebabkan ValueError
except ValueError as e:
    print(f"Terjadi error: {e}")
else:
    print("Tidak ada error, kode ini akan dieksekusi jika tidak ada error")
finally:
    print("Ini akan dieksekusi selalu, baik ada error maupun tidak")
