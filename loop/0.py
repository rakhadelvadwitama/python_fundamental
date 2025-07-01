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