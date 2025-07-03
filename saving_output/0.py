# kata kunci with open as
# mode read dan mode write, read -> nilainya adalah 'r' -> untuk membaca file, write -> nilai nya adalah 'w' untuk menulis file
with open('saving_output/output.txt', 'w') as file:
    # Menulis ke file
    file.write('Hello, World!')
    # writeline juga bisa digunakan untuk menulis ke file, namun akan menambahkan newline di akhir string
    file.writelines(['Hello, World!\n', 'This is a test.\n', 'Goodbye, World!\n'])

todos = ["todo1", "todo2", "todo3"]
with open('saving_output/output2.txt', 'w') as file:
    for todo in todos:
        file.write(todo + '\n')  # Menulis setiap todo di baris baru. \n adalah karakter newline yang digunakan untuk memisahkan setiap todo di dalam file.

# Membaca dari file
with open('saving_output/output2.txt', 'r') as file:
    # data = file.read()  # Membaca seluruh isi file
    data = file.readlines()  # Membaca seluruh isi file dan mengembalikannya sebagai list, dimana setiap elemen adalah satu baris dari file
print(data)