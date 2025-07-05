import json

def intro():
    print("###############################")
    print("## Aplikasi Todo List Python ##")
    print("-------------------------------")

def main_menu():
    print("ketik 1 untuk memasukkan todo")
    print('ketik 2 untuk melihat todo anda')
    print("ketik 3 untuk menghapus todo anda")
    print("ketik 4 untuk menghapus semua todo anda")
    print("ketik 5 untuk keluar dari aplikasi")

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

def user_input_action(user_input):
    while True:
        print(f"user input anda adalah: {user_input}")
        if user_input == 1:
            todos = add_todo()
            print("inin harusnya keluar dari fitur")
        elif user_input == 2:
            print('Ini menampilkan todo anda')
        elif user_input == 3:
            print('Ini menghapus todo anda')
        elif user_input == 4:
            exit_program(todos)
        else:
            print('Pilihan tidak valid.')

def show_username(full_name):
    print(f"Selamat datang, {full_name}!")

def add_todo(todos):
    name = input("Masukan todo anda: ")
    description = input("Deskripsi todo anda: ")
    isImportant = bool(input(f"Apakah todo {name} penting? (ketik 1 untuk penting dan 0 untuk tidak): "))
    notes = []
    while True:
        note = input("Masukkan catatan extra, ketik exit untuk keluar: ")
        if note == 'exit':
            break
        else:
            notes.append(note)
    todo = {
        "name": name,
        "description": description,
        "isImportant": isImportant,
        "notes": notes
    }
    todos.append(todo)
    print(f"✅ Todo '{name}' berhasil ditambahkan!")
    return todos

def exit_program(db):
    exit_ = input("Apakah anda ingin keluar dari aplikasi? (y/n): ")
    if exit_ == 'y':
        print("Exiting program")
        save_json('db.json', db)
        exit()
    elif exit_ == 'n':
        print("Anda memilih untuk tetap menggunakan aplikasi.")
    else:
        print("Pilihan tidak valid. Silakan masukkan 'y' untuk keluar atau 'n' untuk tetap menggunakan aplikasi.")

def show_todos(todos):
    if len(todos) > 0:
        print("Daftar Todo Anda:")
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo}")
    else:
        print("Anda belum memasukkan todo apapun.")

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


def delete_all_todos(todos):
    confirm = input("Apakah anda yakin ingin menghapus semua todo? (y/n): ")
    if confirm == 'y':
        todos.clear()
        return todos
    else:
        return todos

def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data

def save_json(filename, db):
    with open(filename, 'w') as file:
        json.dump(db, file)

def login(db):
    username = input('Username:')
    password = input('Password:')
    if username in db and db[username]['password1'] == password:
        print('login success, welcome', db[username]['name'])
        return db[username]
    else:
        raise ValueError('login failed, username or password is incorrect') # raise itu digunakan untuk mengeluarkan error, jadi kita bisa menangkapnya di bagian lain dari program kita.
    
def register(db):
    username = input('Username:')
    password1 = input('Password:')
    password2 = input('Confirm Password:')
    if password1 == password2 and username not in db:
        print('Register success')
        db[username] = {
            'name': username,
            'password1': password1,
            'password2': password2,
            'todos': []
        }
        save_json('db.json', db)
    else:
        raise ValueError('Register failed, password does not match or username already exists')


if __name__ == "__main__":
    # __name__ == "__main__" digunakan untuk readability
    db = read_json('db.json')
    intro()

    login_or_register = input("login or register): ")
    if login_or_register == 'login':
        user = login(db)
        # print(user)
    elif login_or_register == 'register':
        register(db)
    else:
        raise ValueError('Invalid input, please enter "login" or "register"')
    
    while True:
        main_menu()
        user_input = get_user_input()
        print(f"user input anda adalah: {user_input}")
        if user_input == 1:
            while True:
                user['todos'] = add_todo(user['todos']) #-> seperti ini disebut overriding variable
                exit_ = bool(input('Apakah and ingin keluar dari fitur memasukkan todo? (1 untuk Ya, 0 untuk Tidak): '))
                if exit_:
                    print("kembali ke menu utama")
                    break
        elif user_input == 2:
            show_todos(user['todos'])
        elif user_input == 3:
            show_todos(todos['user']['todos'])
            todos = delete_todo(todos)
            print("kembali ke menu utama")
        elif user_input == 4:
            todos = delete_all_todos(user['todos'])
        elif user_input == 5:
            exit_program(db)
        else:
            print('Pilihan tidak valid.')