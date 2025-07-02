"""
while loop digunakaan untuk menjalankan blok kode berulang kali selama kondisi yang diberikan adalah True. Ini berguna ketika jumlah iterasi tidak diketahui sebelumnya atau ketika kita ingin terus menjalankan blok kode sampai kondisi tertentu terpenuhi. blok kode akan terus dieksekusi selama kondisi loop adalah True. Jika kondisi menjadi False, loop akan berhenti.

bedanya dengan for loop, while loop tidak memerlukan iterable seperti list atau range. Sebagai gantinya, kita menentukan kondisi yang harus dipenuhi untuk terus menjalankan loop.
"""

while True:
    x += 1
    y += 1
    print(f"x: {x}, y: {y}")
    