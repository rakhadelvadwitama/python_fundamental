# fungsi intro todo list sederhana
print("###############################")
print("## Aplikasi Todo List Python ##")
print("-------------------------------")
# endof intro

# fungsi ambil input nama depan dan nama belakang
front_name = input("Masukkan nama depan anda: ")
back_name = input("Masukkan nama belakang anda: ")
# end of fungsi ambil input nama

#fungsi menu utama
print("ketik 1 untuk memasukkan todo")
print('ketik 2 untuk melihat todo anda')
print("ketik 3 untuk menghapus todo anda")
print("ketik 4 untuk keluar dari aplikasi")
# end of fungsi menu utama

# fungsi validasi input user
while True:
    try:
        user_input = int(input("Masukkan pilihan anda: "))
        if user_input in [1, 2, 3, 4]:
            break
        else:
            print("Input tidak valid. Silakan masukkan angka sesuai pilihan yang tersedia.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka sesuai pilihan yang tersedia.")
# end of fungsi validasi input user

# fungsi pengecekan input user
if user_input == 1:
    print('Ini nambahin todo anda')
elif user_input == 2:
    print('Ini menampilkan todo anda')
elif user_input == 3:
    print('Ini menghapus todo anda')
elif user_input == 4:
    print('Terima kasih telah menggunakan aplikasi Todo List Python!')
else:
    print('Pilihan tidak valid.')
# end of fungsi pengecekan input user

# fungsi menyapa user
print(f"Selamat datang, {front_name} {back_name}!")
# end of fungsi menyapa user

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

"""
jumlah_todos = int(input("Berapa banyak todos yang ingin anda masukkan? (1-4): "))
print(type(jumlah_todos))
# exit()

todos = []  # list untuk menyimpan todo
for i in range(jumlah_todos):
    todo = input(f"Masukkan todo ke-{i+1}: ")
    todos.append(todo)
print(f"todos anda hari ini adalah: {todos}, terima kasih telah memasukkan {len(todos)} todos!")

"""

# fungsi untuk memasukkan todo
todos = []  # list untuk menyimpan todo
while True:
    todo = input("Masukkan todo atau 'exit' untuk keluar: ")
    if todo.lower() == 'exit':
        break
    else:
        todos.append(todo)
# end of fungsi untuk memasukkan todo

"""
if len(todos) ==4:
    print(f"Todos anda hari ini adalah: {todos}, terima kasih telah memasukkan {len(todos)} todos!")
else:
    print(f"Anda hanya memasukkan {len(todos)} todos.")
"""

# fungsi akhir aplikasi
exit_ = input("Apakah anda ingin keluar dari aplikasi? (y/n): ")
if exit_ == 'y':
    print(f"Todos anda: {todos}, jumlah todos anda: {len(todos)}")
    print("Terima kasih telah menggunakan aplikasi Todo List Python!")
    exit()
elif exit_ == 'n':
    print("Anda memilih untuk tetap menggunakan aplikasi.")
else:
    print("Pilihan tidak valid. Silakan masukkan 'y' untuk keluar atau 'n' untuk tetap menggunakan aplikasi.")
# end of fungsi akhir aplikasi