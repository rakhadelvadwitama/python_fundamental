# kita bisa mengubah tipe data dari satu tipe data ke tipe data lainnya menggunakan fungsi bawaan python seperti int(), float(), str(), dll selama mengikuti aturan konversi tipe data tersebut.
# contoh integer ke string
x = 10
type_x = type(x) # -> <class 'int'>
print(type_x) # -> <class 'int'>
x_str = str(x) # mengubah integer ke string
type_x_str = type(x_str) # -> <class 'str'>
print(type_x_str) # -> <class 'str'>

# contoh float ke string
y = 10.5
type_y = type(y) # -> <class 'float'>
print(type_y) # -> <class 'float'>
y_str = str(y) # mengubah float ke string
type_y_str = type(y_str) # -> <class 'str'>
print(type_y_str) # -> <class 'str'>

print("---")
# contoh string ke integer
z = "20"
type_z = type(z) # -> <class 'str'>
print(type_z) # -> <class 'str'>
print(z, type(z)) # -> 20 <class 'str'>
z_int = int(z) # mengubah string ke integer
type_z_int = type(z_int) # -> <class 'int'>
print(type_z_int) # -> <class 'int'>
print(z_int, type(z_int)) # -> 20 <class 'int'>