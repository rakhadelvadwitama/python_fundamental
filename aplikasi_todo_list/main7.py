import json

def intro():
    print("###############################################################################")
    print("##                          Aplikasi Todo List Python                        ##")
    print("-------------------------------------------------------------------------------")

def main_menu():
    print("******************************   Main Menu  ***********************************")
    print("                                                                               ")
    """
    cara 1 untuk menghindari DRY (Don't Repeat Yourself) principle
    main_menu = "add todo", "show todo", "delete todo", "delete all todo", "exit"
    for i, menu in enumerate(main_menu, start=1):
        print(f"({i}) {menu}")
    """
    print("(1) add todo | (2) show todo | (3) edit todo | (4) delete todo | (5) delete all todo | (6) exit")
    print("                                                                               ")
    print("*******************************************************************************")

def get_user_input():
    while True:
        try:
            user_input = int(input("Masukkan pilihan anda: "))
            if user_input in [1, 2, 3, 4, 5, 6]:
                return user_input
            else:
                print("Input tidak valid. Silakan masukkan angka sesuai pilihan yang tersedia.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka sesuai pilihan yang tersedia.")

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
    print("-------------------------------------------------------------------------------")
    print(f"✅ Todo '{name}' berhasil ditambahkan!")
    print("-------------------------------------------------------------------------------")
    return todos

def exit_program(db):
    print("-------------------------------------------------------------------------------")
    print("                              Exiting program                                  ")
    print("-------------------------------------------------------------------------------")
    save_json('db.json', db)
    exit()


def show_todos(todos):
    if len(todos) < 1:
        print("Anda belum memasukkan todo apapun.")
    else:
        print("Daftar Todo Anda:")
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo['name']} - {todo['description']}")
        print("-------------------------------------------------------------------------------")
        user_input = int(input("ketik salah satu nomor todo untuk melihat detail: "))
        if user_input > 0 and user_input <= len(todos):
            todo = todos[user_input-1]
            print("-------------------------------------------------------------------------------")
            for key in todo:
                # improvisasi untuk isImportant jika true maka tampilkan "Penting" jika false tampilkan "Tidak Penting" menggunakan isinstance
                if isinstance(todo[key], bool):
                    match todo[key]:
                        case True:
                            print(f"{key.upper()} : PENTING")
                        case False:
                            print(f"{key.upper()} : TIDAK PENTING")
                
                elif isinstance(todo[key], list):
                    print("EXTRA NOTE:")
                    for i, note in enumerate(todo[key], start = 1):
                        print(f"{i}. {note}")
                else:
                    print(f"{key.upper()} : {todo[key]}")
            print("-------------------------------------------------------------------------------")
        else:
            raise ValueError("Input tidak valid. Silakan masukkan nomor todo yang benar.")

def show_todos_simpler(todos):
    if len(todos) < 1:
        print("Anda belum memasukkan todo apapun.")
    else:
        print("Daftar Todo Anda:")
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo['name']} - {todo['description']}")

def delete_todo(todos):
    while True:
        todo_delete = int(input("Masukkan todo yang ingin dihapus, ketik 0 untuk batal: ")) - 1
        if todo_delete == -1:
            return todos
        elif todo_delete >= 0 and todo_delete < len(todos):
            deleted_todo = todos.pop(todo_delete)
            print(f"✅ Todo '{deleted_todo['name']}' berhasil dihapus!")
            print("-------------------------------------------------------------------------------")
        else:
            print("Input tidak valid. Silakan masukkan nomor todo yang benar.")


def delete_all_todos(todos, username):
    confirm = input("Apakah anda yakin ingin menghapus semua todo? (y/n): ")
    if confirm == 'y':
        todos.clear()
        print(f"✅ Semua todo punya {username} berhasil dihapus!")
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
    username = "admin" #input('Username: ')
    password = "admin" #input('Password: ')
    if username in db and db[username]['password1'] == password:
        print('Login Success, welcome', db[username]['name'])
        return db[username]
    else:
        raise ValueError('Login failed, username or password is incorrect') # raise itu digunakan untuk mengeluarkan error, jadi kita bisa menangkapnya di bagian lain dari program kita.
    
def register(db):
    username = input('Username: ')
    password1 = input('Password: ')
    password2 = input('Confirm Password: ')
    if password1 == password2 and username not in db:
        db[username] = {
            'name': username,
            'password1': password1,
            'password2': password2,
            'todos': []
        }
        save_json('db.json', db)
        exit("Register Success, silakan login kembali")
    else:
        raise ValueError('Register failed, password does not match or username already exists')


if __name__ == "__main__":
    # __name__ == "__main__" digunakan untuk readability 
    db = read_json('db.json')
    intro()

    login_or_register = "login" #input("login or register: ")
    match login_or_register:
        case 'login':
            user = login(db)
        case 'register':
            register(db)
        case _:
            raise ValueError('Invalid input, please enter "login" or "register"')
    
    while True:
        main_menu()
        user_input = get_user_input()
        print(f"User input anda adalah: {user_input}")
        match user_input:
            case 1:
                while True:
                    print("-------------------------------------------------------------------------------")
                    user['todos'] = add_todo(user['todos']) #-> seperti ini disebut overriding variable
                    exit_ = bool(input('Apakah and ingin keluar dari fitur memasukkan todo? (1 untuk Ya, 0 untuk Tidak): '))
                    print("-------------------------------------------------------------------------------")
                    if exit_:
                        save_json('db.json', db)
                        print("kembali ke menu utama")
                        break
            case 2:
                show_todos(user['todos'])
            case 3:
                print("edit todo")
                # print kembali show todos
                show_todos_simpler(user['todos'])
                todo_input = int(input("pilih todo yang ingin di edit (ketik nomor todo): "))-1
                # memilih todo yang ingin di edit berdasarkan nomor
                """ jika todo_input tidak valid, maka akan raise error"""
                if todo_input < 0 or todo_input >= len(user['todos']):
                    raise ValueError("Input tidak valid. Silakan masukkan nomor todo yang benar.")
                print(user['todos'][todo_input])
                """todo yang ditampilkan hanya name todo saja dengan menggunakan enumerate"""
                for i, todo in enumerate(user['todos'][todo_input], start=1):
                    print(f"{i}. {todo} : {user['todos'][todo_input][todo]}")
                user_input = int(input("pilih todo yang ingin di edit: "))
                match user_input:
                    case 1:
                        user['todos'][todo_input]['name'] = input("Enter updated todo name: ")
                    case 2:
                        user['todos'][todo_input]['description'] = input("Enter updated todo description: ")
                    case 3:
                        user['todos'][todo_input]['isImportant'] = bool(int(input("Enter updated todo isImportant (1 untuk Ya, 0 untuk Tidak): ")))
                    case 4:
                        for i, note in enumerate(user['todos'][todo_input]['notes'], start=1):
                            print(f"{i}. {note}")
                        # menampilkan input untuk mengedit note dan menambahkan note. input yang digunakaan adalah nomor note yang ingin di edit dan jika ingin menambahkan note maka inputnya adalah nomor note terakhir + 1 serta jika ingin menghapus no
                        total_notes = len(user['todos'][todo_input]['notes'])
                        print(f"Total notes: {total_notes}")

                        note_input = int(input(f"pilih note yang ingin di edit (1-{total_notes}) atau {total_notes+1} untuk menambahkan note baru: "))

                        if note_input < 1 or note_input > (total_notes + 1):
                            raise ValueError("Input tidak valid. Silakan masukkan nomor note yang benar.")
                        
                        if note_input == total_notes + 1:
                            user['todos'][todo_input]['notes'].append(input("Masukkan catatan extra: "))
                        else:
                            user['todos'][todo_input]['notes'][note_input - 1] = input("Enter updated note: ")
                            print("Note berhasil diupdate!")
                        save_json('db.json', db)
                        print("-------------------------------------------------------------------------------")

                        """
                        note_input = int(input("pilih note yang ingin di edit (ketik nomor note): "))-1
                        if note_input < 0 or note_input >= (len(user['todos'][todo_input]['notes'])+1):
                            raise ValueError("Input tidak valid. Silakan masukkan nomor note yang benar.")
                        if note_input == len(user['todos'][todo_input]['notes'])+1:
                            user['todos'][todo_input]['notes'].append(input("Masukkan catatan extra: "))
                        else:
                            user['todos'][todo_input]['notes'][note_input] = input("Enter updated note: ")
                        """    
                    case _:
                        raise ValueError("Input tidak valid. Silakan masukkan nomor todo yang benar.")
                print("Todo berhasil diupdate!")
                print("-------------------------------------------------------------------------------")
                save_json('db.json', db)

            case 4:
                show_todos_simpler(user['todos'])
                user['todos'] = delete_todo(user['todos'])
                print("kembali ke menu utama")
            case 5 :
                todos = delete_all_todos(user['todos'], user['name'])
            case 6:
                exit_program(db)
            case _:
                raise ValueError('Pilihan tidak valid')