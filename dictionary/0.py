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
    "Hobbi": ["Membaca", "Menulis", "Bersepeda"]
}
print(ktp)
print(ktp["Nama"])
print(ktp["Alamat"]["Kecamatan"])
print(ktp["Hobbi"][0])
print(len(ktp))
print(len(str(ktp["NIK"])))
print("------------------------------------------------")
#cara mengakses data di dalam dictionary
# akses value dalam dictionary
# anda dapat mengakses value dalam dictionary dengan menggunakan key-nya yang terkait dengan nilainya
# menggunakan tanda kurung siku [] untuk mengakses/passing value dalam dictionary
ex_ktp = {    "NIK": 1234567890123456,
    "Nama": "Galang Adi Pratama",
    "NIK": 1234567890123456,
    "Agama": "Islam",
    "Tempat Lahir": "Jakarta",
    
}

nama_lengkap = ex_ktp["Nama"]
nik = ex_ktp["NIK"]
agama = ex_ktp["Agama"]
tempat_lahir = ex_ktp["Tempat Lahir"]
print(f"Nama Lengkap: {nama_lengkap}")
print(f"NIK: {nik}")
print(f"Agama: {agama}")
print(f"Tempat Lahir: {tempat_lahir}")
# hobbi = ex_ktp["Hobbi"]
# print(hobbi)  # mengakses hobbi akan error karena key "Hobbi" tidak ada dalam dictionary ex_ktp
# print(hobbi[0])  # mengakses hobbi pertama
print("------------------------------------------------")
# metode .get(key) #perbedaanya dengan cara diatas adalah jika key tidak ditemukan, maka akan mengembalikan None, sedangkan jika menggunakan tanda kurung siku [] akan mengeluarkan error KeyError
nama_lengkap = ex_ktp.get("Nama")
print(f"Nama Lengkap: {nama_lengkap}")
hobi = ex_ktp.get("Hobbi")
print(hobi)