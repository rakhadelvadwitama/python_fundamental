# fungsi intro todo list sederhana
def intro():
    print("#############################################################################")
    print("                        Aplikasi Todo List Python                            ")
    print("-----------------------------------------------------------------------------")
# endof intro

# fungsi ambil input nama depan dan nama belakang
def name_input():
    front_name = input("Masukkan nama depan anda: ")
    back_name = input("Masukkan nama belakang anda: ")
    return f"{front_name} {back_name}"
# end of fungsi ambil input nama

#fungsi menu utama
def main_menu():
    print("*****************************************************************************")
    print("1. add todo | 2. lihat todo | 3. hapus todo | 4. hapus semua todo | 5. keluar")
    print("*****************************************************************************")
# end of fungsi menu utama

# fungsi validasi input user
def get_user_input():
    while True:
        try:
            user_input = int(input("Masukkan pilihan anda: "))
            if user_input in [1, 2, 3, 4,5]:
                return user_input
            else:
                print("Input tidak valid. Silakan masukkan angka sesuai pilihan yang tersedia.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka sesuai pilihan yang tersedia.")
# end of fungsi validasi input user


# fungsi pengecekan input user
def user_input_action(user_input):
    while True:
        print(f"user input anda adalah: {user_input}")
        if user_input == 1:
            todos = add_todos()
            print("inin harusnya keluar dari fitur")
        elif user_input == 2:
            print('Ini menampilkan todo anda')
        elif user_input == 3:
            print('Ini menghapus todo anda')
        elif user_input == 4:
            exit_program(todos)
        else:
            print('Pilihan tidak valid.')
# end of fungsi pengecekan input user

# fungsi menyapa user
def show_username(full_name):
    full_name = full_name.upper()
    print(f"Selamat datang, {full_name}!")
# end of fungsi menyapa user

# fungsi untuk memasukkan todo
def add_todos(todos):
    while True:
        todo_name = input("Masukkan todo atau 'exit' untuk keluar: ")
        if todo_name.lower() == 'exit':
            return todos
        else:
            todos.append(todo_name)
# end of fungsi untuk memasukkan todo

# fungsi akhir aplikasi
def exit_program(todos):
    exit_ = input("Apakah anda ingin keluar dari aplikasi? (y/n): ")
    if exit_ == 'y':
        print("Exiting program")
        if not todos:
            print("Anda belum memasukkan todo apapun.")
        else:
            print(f"Todos anda: {todos}, jumlah todos anda: {len(todos)}")
        exit()
    elif exit_ == 'n':
        print("Anda memilih untuk tetap menggunakan aplikasi.")
    else:
        print("Pilihan tidak valid. Silakan masukkan 'y' untuk keluar atau 'n' untuk tetap menggunakan aplikasi.")
# end of fungsi akhir aplikasi

# fungsi menampilkan todo
def show_todos(todos):
    if not todos:
        print("Anda belum memasukkan todo apapun.")
    else:
        print("Todo anda:")
        """
        num = 1
        for todo in todos:
            print(f"{num}. {todo}")
            num += 1
        """
        #bisa menggunakan enumerate untuk menghindari penggunaan variabel tambahan dan ini lebih superior
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo}")
# end of fungsi menampilkan todo

# fungsi untuk menghapus todo
def delete_todo(todos):
    todo_delete = int(input("Masukkan todo yang ingin dihapus, ketik 0 untuk batal: ")) - 1
    # todos.pop(todo_delete) # yang terjadi disini adalah kita menghapus todo berdasarkan index yang dimasukkan oleh user. misal todo kita berada di nomor 1, akan tetapi index pada list dimulai dari 0, sehingga kita harus mengurangi 1 dari input user.
    if todo_delete == -1:
        return todos
    else:
        todos.pop(todo_delete)
        return todos
# end of fungsi untuk menghapus todo
def delete_all_todos(todos):
    confirm = input("Apakah anda yakin ingin menghapus semua todo? (y/n): ")
    if confirm == 'y':
        todos.clear()
        return todos
    else:
        return todos
    


intro()
full_name = name_input()
show_username(full_name)
todos = ["makan", "minum", "tidur"] #-> ini adalah contoh list yang sudah ada
while True:
    main_menu()
    user_input = get_user_input()
    print(f"user input anda adalah: {user_input}")
    if user_input == 1:
        todos = add_todos(todos) #-> seperti ini disebut overriding variable
        print("ini harusnya keluar dari fitur")
    elif user_input == 2:
        show_todos(todos)
    elif user_input == 3:
        show_todos(todos)
        todos = delete_todo(todos)
    elif user_input == 4:
        todos = delete_all_todos(todos)
    elif user_input == 5:
        exit_program(todos)
    else:
        print('Pilihan tidak valid.')