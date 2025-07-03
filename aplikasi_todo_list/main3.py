import json

# fungsi intro todo list sederhana
def intro():
    print("###############################")
    print("## Aplikasi Todo List Python ##")
    print("-------------------------------")
# endof intro

# fungsi ambil input nama depan dan nama belakang
def name_input():
    front_name = input("Masukkan nama depan anda: ")
    back_name = input("Masukkan nama belakang anda: ")
    return f"{front_name} {back_name}"
# end of fungsi ambil input nama

#fungsi menu utama
def main_menu():
    print("ketik 1 untuk memasukkan todo")
    print('ketik 2 untuk melihat todo anda')
    print("ketik 3 untuk menghapus todo anda")
    print("ketik 4 untuk menghapus semua todo anda")
    print("ketik 5 untuk keluar dari aplikasi")
# end of fungsi menu utama

# fungsi validasi input user
def get_user_input():
    while True:
        try:
            user_input = int(input("Masukkan pilihan anda: "))
            if user_input in [1, 2, 3, 4, 5]:
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
        data = {"todos": todos}
        with open('todos.json', 'w') as file:
            json.dump(data, file)
        exit()
    elif exit_ == 'n':
        print("Anda memilih untuk tetap menggunakan aplikasi.")
    else:
        print("Pilihan tidak valid. Silakan masukkan 'y' untuk keluar atau 'n' untuk tetap menggunakan aplikasi.")
# end of fungsi akhir aplikasi

# fungsi menampilkan todo
def show_todos(todos):
    # cek jika todos kosong maka tampilkan pesan bahwa belum ada todo dengan menggunakan if dan length
    # cara 1
    if len(todos) > 0:
        print("Daftar Todo Anda:")
        # cara 1
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo}")
    else:
        print("Anda belum memasukkan todo apapun.")
    
    
    # cara 2
    """
    if not todos:
        print("Anda belum memasukkan todo apapun.")
    else:
        print("Todo anda:")
        # cara 1
        num = 1
        for todo in todos:
            print(f"{num}. {todo}")
            num += 1
        
        # cara 2 bisa menggunakan enumerate untuk menghindari penggunaan variabel tambahan dan ini lebih superior
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo}")
    """
# end of fungsi menampilkan todo

# fungsi untuk menghapus todo
def delete_todo(todos):
    while True:
        todo_delete = int(input("Masukkan todo yang ingin dihapus, ketik 0 untuk batal: "))
        # todos.pop(todo_delete) # yang terjadi disini adalah kita menghapus todo berdasarkan index yang dimasukkan oleh user. misal todo kita berada di nomor 1, akan tetapi index pada list dimulai dari 0, sehingga kita harus mengurangi 1 dari input user.
        if todo_delete == 0:
            return todos
        elif todo_delete > 0 and todo_delete < len(todos):
            todos.pop(todo_delete-1)
        else:
            print("Input tidak valid. Silakan masukkan nomor todo yang benar.")

# end of fungsi untuk menghapus todo
def delete_all_todos(todos):
    confirm = input("Apakah anda yakin ingin menghapus semua todo? (y/n): ")
    if confirm == 'y':
        todos.clear()
        return todos
    else:
        return todos
# end of fungsi untuk menghapus semua todo

# read todos from file json
def read_todos():
    try:
        with open('todos.json', 'r') as file:
            data = json.load(file)
            return data.get("todos", [])
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

if __name__ == "__main__":
    # __name__ == "__main__" digunakan untuk readability

    intro()
    full_name = name_input()
    show_username(full_name)
    todos = read_todos()
    while True:
        main_menu()
        user_input = get_user_input()
        print(f"user input anda adalah: {user_input}")
        if user_input == 1:
            todos = add_todos(todos) #-> seperti ini disebut overriding variable
            print("kembali ke menu utama")
        elif user_input == 2:
            show_todos(todos)
        elif user_input == 3:
            show_todos(todos)
            todos = delete_todo(todos)
            print("kembali ke menu utama")
        elif user_input == 4:
            todos = delete_all_todos(todos)
        elif user_input == 5:
            exit_program(todos)
        else:
            print('Pilihan tidak valid.')