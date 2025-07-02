"""
while loop digunakaan untuk menjalankan blok kode berulang kali selama kondisi yang diberikan adalah True. Ini berguna ketika jumlah iterasi tidak diketahui sebelumnya atau ketika kita ingin terus menjalankan blok kode sampai kondisi tertentu terpenuhi. blok kode akan terus dieksekusi selama kondisi loop adalah True. Jika kondisi menjadi False, loop akan berhenti.

bedanya dengan for loop, while loop tidak memerlukan iterable seperti list atau range. Sebagai gantinya, kita menentukan kondisi yang harus dipenuhi untuk terus menjalankan loop.
"""

x = 10
y = 0
while x > y:
    print(f"kode ini akan terus berjalan selama {x} lebih besar dari {y}")
    y += 1
print("kode ini akan dieksekusi setelah while loop selesai.")