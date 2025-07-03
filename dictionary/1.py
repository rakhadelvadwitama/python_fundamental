ktp = {
    "NIK": 1234567890123456,
    "Nama": "Galang Adi Pratama",
    "Tempat Lahir": "Jakarta",
    "Tanggal Lahir": "01-01-1990",
    "Jenis Kelamin": "Laki-laki",
    "Alamat": {
        "Jalan": "Jl. Raya No. 123",
        "RT": 1,
        "RW": 2,
        "Kelurahan": "Cempaka Putih",
        "Kecamatan": "Cempaka Putih",
        "Kota/Kabupaten": "Jakarta Pusat",
        "Provinsi": "DKI Jakarta",
        "Kode Pos": 10510
    },
    "Agama": "Islam",
    "Status Perkawinan": False,
    "Pekerjaan": "Programmer",
    "Kewarganegaraan": "WNI",
    "Berlaku Hingga": "31-12-2030",
    "Hobi": ["Membaca", "Menulis", "Bersepeda"]
}

# nested dictionary yaitu dictionary di dalam dictionary

kecamatan = ktp["Alamat"]["Kecamatan"]
print(kecamatan)
print(type(kecamatan))  # akan mengembalikan <class 'str'> karena kita menggunakan [ ] yang mengembalikan value dari key yang ada di dalam dictionary

kabupaten = ktp.get("Alamat", {}).get("Kota/Kabupaten", "Tidak ada data")
print(kabupaten)
print(type(kabupaten))  # akan mengembalikan <class 'str'> karena kita menggunakan .get() yang mengembalikan None jika key tidak ditemukan, dan kita memberikan default value "Tidak ada data" jika key tidak ditemukan
# thats why we use [ ] instead of .get(). because .get() its to long

jalan = ktp["Alamat"].get("Jalan", 0)  # jika key tidak ditemukan, maka akan mengembalikan 0
print(jalan)
print(type(jalan))  # akan mengembalikan <class 'int'> karena kita menggunakan .get() yang mengembalikan None jika key tidak ditemukan, dan kita memberikan default value 0 jika key tidak ditemukan


# modifikasi nilai dalam dictionary
# 1. dengan menggunakan tanda kurung siku []
ktp["Nama"] = "Galang Adi Pratama Siregar"
print(ktp["Nama"])  # akan mengembalikan "Galang Adi Pratama Siregar"
alamat = ktp["Alamat"]["Jalan"]
alamat = "Jl. Raya No. 456"
print(alamat)  # akan mengembalikan "Jl. Raya No. 456"

# 2. dengan menggunakan method .update()
ktp["Alamat"].update({"Jalan": "Jl. Raya No. 456789"})
print(ktp["Alamat"]["Jalan"])  # akan mengembalikan "Jl. Raya No. 456789"
#menambahkan value baru ke dalam hobbi
ktp["Hobi"].append("Berenang")
print(ktp["Hobi"])  # akan mengembalikan ["Membaca", "Menulis", "Bersepeda", "Berenang"]
ktp['Hobi'].remove("Bersepeda")  # menghapus elemen "Bersepeda" dari list Hobi
print(ktp["Hobi"])  # akan mengembalikan ["Membaca", "Menulis", "Berenang"]
# edit list di dalam dictionary akan tetapi tidak bisa menggunakan method .update()
# karena .update() hanya bisa digunakan untuk menambahkan key-value pair baru atau mengubah value dari key yang sudah ada
# untuk mengubah value dari key yang sudah ada, kita bisa menggunakan tanda kurung siku []
ktp["Hobi"][0] = "Bermain Gitar"  # mengubah elemen pertama dari list Hobi
print(ktp["Hobi"])  # akan mengembalikan ["Bermain Gitar", "Menulis", "Berenang"]

ktp["Alamat"]["Kode Pos"] = 123457889  # mengubah value dari key "Kode Pos" di dalam dictionary "Alamat"
print(ktp["Alamat"])  # akan mengembalikan dictionary alamat yang sudah diubah
print(ktp)

# konsep CRUP
# CREATE -> membuat data baru -> menggunakan method .update() atau tanda kurung siku []
# READ -> membaca data -> menggunakan tanda kurung siku [] atau method .get()
# UPDATE -> mengubah data -> menggunakan tanda kurung siku [] atau method .update()
# DELETE -> menghapus data -> menggunakan method .pop() atau del
# untuk menghapus data dari dictionary, kita bisa menggunakan method .pop() atau del
# 1. dengan menggunakan method .pop()
ktp["Hobi"].pop(0)  # menghapus elemen pertama dari list Hobi
print(ktp["Hobi"])  # akan mengembalikan ["Menulis", "Berenang"]
# 2. dengan menggunakan del
del ktp["Alamat"]["Kode Pos"]  # menghapus key "Kode Pos" dari dictionary "Alamat"
print(ktp["Alamat"])  # akan mengembalikan dictionary alamat yang sudah diubah
# 3. dengan menggunakan method .clear() untuk menghapus semua data dari dictionary
ktp.clear()
print(ktp)  # akan mengembalikan {}