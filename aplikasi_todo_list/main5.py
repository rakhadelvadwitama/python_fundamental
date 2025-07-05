def get_notes():
    """Function terpisah untuk mengumpulkan notes"""
    notes = []
    print("Masukkan catatan extra (ketik 'exit' untuk selesai):")
    while True:
        note = input("Catatan: ")
        if note == 'exit':
            break
        notes.append(note)
    return notes

def add_single_todo(todos):
    """Function untuk menambah satu todo"""
    name = input("Masukkan nama todo: ")
    description = input("Masukkan deskripsi todo: ")
    
    # Validasi input untuk isImportant
    while True:
        important_input = input(f"Apakah todo '{name}' penting? (1 untuk ya, 0 untuk tidak): ")
        if important_input in ['0', '1']:
            isImportant = bool(int(important_input))
            break
        print("Input tidak valid. Masukkan 1 atau 0.")
    
    notes = get_notes()
    
    todo = {
        "name": name,
        "description": description,
        "isImportant": isImportant,
        "notes": notes
    }
    todos.append(todo)
    print(f"Todo '{name}' berhasil ditambahkan!")
    return todos

def add_todos(todos):
    """Function utama untuk menambah todos"""
    while True:
        choice = input("\nPilih aksi:\n1. Tambah todo baru\n2. Selesai menambah todo\nPilihan (1/2): ")
        
        if choice == '1':
            todos = add_single_todo(todos)
        elif choice == '2':
            print("Selesai menambah todo.")
            break
        else:
            print("Pilihan tidak valid. Masukkan 1 atau 2.")
    
    return todos

# ALTERNATIF: Versi yang lebih sederhana dengan single function
def add_todos_simple(todos):
    """Versi sederhana tanpa nested while loop"""
    print("=== MENAMBAH TODO ===")
    
    # Input basic info
    name = input("Nama todo: ")
    if name.lower() == 'exit':
        return todos
        
    description = input("Deskripsi: ")
    
    # Input importance dengan validasi
    important_input = input("Penting? (y/n): ").lower()
    isImportant = important_input in ['y', 'yes', '1']
    
    # Input notes dengan cara yang lebih sederhana
    notes_input = input("Catatan (pisahkan dengan koma jika lebih dari 1): ")
    notes = [note.strip() for note in notes_input.split(',')] if notes_input else []
    
    # Buat todo object
    todo = {
        "name": name,
        "description": description,
        "isImportant": isImportant,
        "notes": notes
    }
    
    todos.append(todo)
    print(f"✅ Todo '{name}' berhasil ditambahkan!")
    
    # Tanya apakah ingin menambah lagi
    add_more = input("Tambah todo lagi? (y/n): ").lower()
    if add_more in ['y', 'yes']:
        return add_todos_simple(todos)  # Recursion instead of while loop
    
    return todos
