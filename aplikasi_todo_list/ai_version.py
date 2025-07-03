# fungsi intro todo list sederhana
def intro():
    print("###############################")
    print("## Aplikasi Todo List Python ##")
    print("###############################")
    print("-------------------------------")
# endof intro

# fungsi ambil input nama depan dan nama belakang
def get_user_name():
    front_name = input("Masukkan nama depan anda: ")
    back_name = input("Masukkan nama belakang anda: ")
    return front_name, back_name
# end of fungsi ambil input nama

# fungsi menu utama
def show_main_menu():
    print("1 add todo | 2 lihat todo | 3 hapus todo | 4 keluar")
# end of fungsi menu utama

# fungsi validasi input user
def get_user_choice():
    while True:
        try:
            user_input = int(input("Masukkan pilihan anda: "))
            if user_input in [1, 2, 3, 4]:
                return user_input
            else:
                print("Input tidak valid. Silakan masukkan angka sesuai pilihan yang tersedia.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka sesuai pilihan yang tersedia.")
# end of fungsi validasi input user

# fungsi pengecekan input user
def handle_user_choice(user_input, todos):
    if user_input == 1:
        return add_todos(todos)
    elif user_input == 2:
        show_todos(todos)
        return todos  # Tambahkan return todos
    elif user_input == 3:
        return delete_todo(todos)
    elif user_input == 4:
        print('Terima kasih telah menggunakan aplikasi Todo List Python!')
        return todos
    else:
        print('Pilihan tidak valid.')
        return todos
# end of fungsi pengecekan input user

# fungsi menyapa user
def greet_user(front_name, back_name):
    print("Selamat datang, " + front_name + " " + back_name + "!")
# end of fungsi menyapa user

# fungsi untuk memasukkan todo
def add_todos(todos):
    while True:
        todo = input("Masukkan todo atau 'exit' untuk keluar: ")
        if todo.lower() == 'exit':
            break
        else:
            todos.append(todo)
            print("Todo '" + todo + "' berhasil ditambahkan!")
    return todos
# end of fungsi untuk memasukkan todo

# fungsi untuk menampilkan todo
def show_todos(todos):
    if not todos:
        print("Anda belum memiliki todo apapun.")
    else:
        print("Daftar Todo Anda:")
        for i, todo in enumerate(todos, 1):
            print(str(i) + ". " + todo)
# end of fungsi untuk menampilkan todo

# fungsi untuk menghapus todo
def delete_todo(todos):
    if not todos:
        print("Anda belum memiliki todo untuk dihapus.")
        return todos
    
    show_todos(todos)
    try:
        index = int(input("Masukkan nomor todo yang ingin dihapus: ")) - 1
        if 0 <= index < len(todos):
            removed_todo = todos.pop(index)
            print("Todo '" + removed_todo + "' berhasil dihapus!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input tidak valid. Masukkan nomor yang benar.")
    return todos
# end of fungsi untuk menghapus todo

# fungsi akhir aplikasi
def exit_app(todos):
    exit_ = input("Apakah anda ingin keluar dari aplikasi? (y/n): ")
    if exit_ == 'y':
        print("Todos anda: " + str(todos) + ", jumlah todos anda: " + str(len(todos)))
        print("Terima kasih telah menggunakan aplikasi Todo List Python!")
        return True
    elif exit_ == 'n':
        print("Anda memilih untuk tetap menggunakan aplikasi.")
        return False
    else:
        print("Pilihan tidak valid. Silakan masukkan 'y' untuk keluar atau 'n' untuk tetap menggunakan aplikasi.")
        return False
# end of fungsi akhir aplikasi

# Program utama
def main():
    todos = []  # list untuk menyimpan todo
    
    # Tampilkan intro
    intro()
    
    # Ambil nama user
    front_name, back_name = get_user_name()
    
    # Sapa user
    greet_user(front_name, back_name)
    
    # Loop utama aplikasi
    while True:
        print("\n" + "="*40)
        show_main_menu()
        user_choice = get_user_choice()
        
        if user_choice == 4:
            if exit_app(todos):
                break
        else:
            todos = handle_user_choice(user_choice, todos)

# Jalankan program utama
if __name__ == "__main__":
    main()