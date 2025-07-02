def intro():
    print("###############################")
    print("## Aplikasi Todo List Python ##")
    print("###############################")
    print("-------------------------------")

def name_input():
    front_name = input("Masukkan nama depan anda: ")
    back_name = input("Masukkan nama belakang anda: ")
    return f"{front_name} {back_name}"

def main_menu():
    print("ketik 1 untuk memasukkan todo")
    print('ketik 2 untuk melihat todo anda')
    print("ketik 3 untuk menghapus todo anda")
    print("ketik 4 untuk keluar dari aplikasi")

def get_user_input():
    while True:
        try:
            user_input = int(input("Masukkan pilihan anda: "))
            if user_input in [1, 2, 3, 4]:
                break
            else:
                print("Input tidak valid. Silakan masukkan angka sesuai pilihan yang tersedia.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka sesuai pilihan yang tersedia.")
    
def user_input_check(user_input):
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

def show_username(full_name):
    print(f"Welcomeg, {full_name}!")

def add_todos():
    todos = []  # list untuk menyimpan todo
    while True:
        todo = input("Masukkan todo (atau 'exit' untuk keluar): ")
        if todo.lower() == 'exit':
            break
        else:
            todos.append(todo)

def exit_app():
    exit_ = input("Apakah anda ingin keluar dari aplikasi? (y/n): ")
    if exit_ == 'y':
        print("Terima kasih telah menggunakan aplikasi Todo List Python!")
        exit()
    elif exit_ == 'n':
        print("Anda memilih untuk tetap menggunakan aplikasi.")
    else:
        print("Pilihan tidak valid. Silakan masukkan 'y' untuk keluar atau 'n' untuk tetap menggunakan aplikasi.")

intro()
full_name = name_input()
show_username(full_name)
main_menu()
user_input = get_user_input()
user_input_check(user_input)
add_todos()
exit_app()