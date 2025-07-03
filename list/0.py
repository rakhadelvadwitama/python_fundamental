# list -> tipe data yang menyimpan serangkaiaan items dalam urutan tertentu

students = ["Galang", "Sugeng", "Bobon"] # kumpulaan data
student1=students[0] # indeks python dimulai dari 0

# support indeks negatif
student2=students[-1] # indeks -1 adalah indeks terakhir
print(student2)

# list di python bersifat mutable -> isinya bisa diubah
# untuk menambah elemen di dalam list/ nambah value di dalam list. itu kita ada namanya method append()
students = ["Galang", "Sugeng", "Bobon"] # kumpulaan data
new_student1 = "Joko"
new_student2 = "Budiman"
#students.append(new_student1, new_student2) # menambah elemen baru di dalam list -> akan error karena append() hanya menerima satu argumen dengan nama error TypeError: append() takes exactly one argument (2 given)
students.append(new_student1)
students.append(new_student2)
print(students)

# list di python juga bisa menggabungkan dua list menjadi satu list dengan method extend()
students = ["Galang", "Sugeng", "Bobon"]
new_students = ["Budiman", "Joko"]
students.extend(new_students)
print(students)

# menghapus element didalam list ada beberapa cara:
# 1. dengan menggunakan del -> menghapus elemen berdasarkan indeks
# 2. dengan menggunakan method remove() -> menghapus elemen berdasarkan value
# 3. dengan menggunakan method pop() -> menghapus elemen berdasarkan indeks

# 1. dengan del
students = ["Galang", "Sugeng", "Bobon"]
del students[0] # menghapus elemen pertama
print(students)

# 2. dengan method remove()
students = ["Galang", "Sugeng", "Bobon"]
students.remove("Sugeng") # menghapus elemen dengan value "Sugeng"
print(students)
# dengan menggunakan .remove() terdapat kekurangan yaitu jika value yang ingin dihapus tidak ada di dalam list, maka akan terjadi error dengan nama error ValueError: list.remove(x): x not in list selain itu jika ada lebih dari satu value yang sama, maka hanya value pertama yang akan dihapus.
# Jika ingin menghapus semua value yang sama, kita bisa menggunakan loop atau list comprehension untuk menghapus semua value yang sama.

# 3. dengan method pop() -> nge cut
students = ["Galang", "Sugeng", "Bobon", "Sugeng"]
x = students.pop(-1) # menghapus elemen terakhir
print(students)
print(x) # menampilkan elemen yang dihapus

# untuk menghitung jumlah elemen di dalam list, kita bisa menggunakan fungsi len()
students = ["Galang", "Sugeng", "Bobon", "sugeng"]
total_students = len(students) # menampilkan jumlah elemen di dalam list
print(total_students) # menampilkan jumlah elemen di dalam list

# untuk melihat banyaknya elemen yang sama di dalam list, kita bisa menggunakan method count()
students = ["Galang", "Sugeng", "Bobon", "sugeng"]
count_sugeng = students.count("Sugeng") # menghitung jumlah elemen "Sugeng" di dalam list
print(count_sugeng) # menampilkan jumlah elemen "Sugeng" di dalam list