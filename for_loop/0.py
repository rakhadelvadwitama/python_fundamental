# for loop sama while loop
"""
for loop adalah jenis loop dalam python yang digunakan untuk melakukakn iterasi atau perulangan melalui sebuah sequence (seperti list, tuple, string, atau range) dengan cara yang lebih sederhana dan mudah dibaca. for loop memungkinkan kita untuk mengulangi blok kode untuk setiap elemen dalam sequence tersebut.
"""

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(f"number is {number}")
print("======")

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(f"name is {name}")
print("======")

fruit ="apple"
for char in fruit:
    print(f"char is {char}")
print("======")

# range function
for i in range(5):
    print(f"i is {i}")
print("======")
for i in range(1, 6):
    print(f"i is {i}")
print("======")
for i in range(1, 11, 2):
    print(f"i is {i}")
print("======")


# enumerate function
# enumerate adalah fungsi built-in di Python yang digunakan untuk mengiterasi sebuah iterable (seperti list, tuple, atau string) dan mendapatkan indeks dari setiap elemen dalam iterable tersebut. Fungsi ini mengembalikan objek enumerasi yang berisi pasangan indeks dan nilai dari elemen-elemen dalam iterable.
# Ini sangat berguna ketika kita ingin mengakses indeks elemen saat melakukan iterasi, tanpa perlu mengelola variabel indeks secara manual.
# Contoh penggunaan enumerate:
# Misalkan kita memiliki sebuah list dan ingin mencetak setiap elemen beserta indeksnya:
l1 = ["eat", "sleep", "code"]
for ele in enumerate(l1):
    print(f"{ele[0]}. {ele[1]}, type is {type(ele)}")
print("======")

l2 = ["eat", "sleep", "code"]
for i, ele in enumerate(l2, start=1):
    print(f"{i}. {ele}, type is {type(ele)}")