print("Hello, World!")

print("ini adalah kalimat")

#variable = tempat menyimpan sebuah data
sentences = "hello world from variable sentences"
print(sentences)

#string -> sebuah kalimat/kumpulan karakter/kata yang menggambarkan kalimat
front_name = "John"
middle_name = "Michael"
last_name = 'Doe'
age = 30 # integer
full_name = front_name + " " + middle_name + " " + last_name # -> tidak efisien, kalau variable stringnya banyak
full_name = f"{front_name} {middle_name} {last_name}" # -> lebih efisien, menggunakan f-string
print(full_name) # -> John Michael Doe

#string tidak hanya support di penjumlahan, tapi juga di perkalian
front_name = "John"
print(front_name * 3) # -> JohnJohnJohn

#ketika kita memasukkan integer ke dalam f-string, maka integer tersebut akan otomatis diubah menjadi string
umur = f"{age}" # -> umur adalah string
print(umur) # -> 30
print(type(umur)) # -> <class 'str'> # tipe data umur adalah string

#jika kita menggunakan penjumlahan antara string dan integer, maka akan terjadi error
# print(front_name + age) # -> TypeError: can only concatenate str (not "int") to str
# untuk menghindari error tersebut, kita harus mengubah integer menjadi string