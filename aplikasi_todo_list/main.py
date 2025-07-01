print("###############################")
print("## Aplikasi Todo List Python ##")
print("-------------------------------")

front_name = input("Masukkan nama depan anda: ")
back_name = input("Masukkan nama belakang anda: ")
print(f"Selamat datang, {front_name} {back_name}!")
jumlah_todos = int(input("Berapa banyak todos yang ingin anda masukkan? (1-4): "))
print(type(jumlah_todos))
# exit()

todos = []  # list untuk menyimpan todo
for i in range(jumlah_todos):
    todo = input(f"Masukkan todo ke-{i+1}: ")
    todos.append(todo)

"""
todos = []  # list untuk menyimpan todo
todos1 = input('Masukkan todos anda 1:')
todos2 = input('Masukkan todos anda 2:')
todos3 = input('Masukkan todos anda 3:')
todos4 = input('Masukkan todos anda 4:')

todos.append(todos1) #masukin makan
todos.append(todos2) #masukin minum
todos.append(todos3) #masukin tidur
todos.append(todos4) #masukin belajar python

if len(todos) == 4:
    print(f"todos anda adalah: {todos}, terima kasih telah memasukkan {len(todos)} todos!")
"""

print(f"todos anda hari ini adalah: {todos}, terima kasih telah memasukkan {len(todos)} todos!")

exit_ = input("Apakah anda ingin keluar dari aplikasi? (y/n): ")
if exit_ == 'y':
    print("Terima kasih telah menggunakan aplikasi Todo List Python!")
    exit()
elif exit_ == 'n':
    print("Anda memilih untuk tetap menggunakan aplikasi.")
else:
    print("Pilihan tidak valid. Silakan masukkan 'y' untuk keluar atau 'n' untuk tetap menggunakan aplikasi.")