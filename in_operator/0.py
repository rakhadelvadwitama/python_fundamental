# in digunakan untuk mengecek apakah suatu nilai ada di dalam sebuah iterable/sequence (seperti list, tuple, string, dll).
fruits = ["apel", "jeruk", "pisang"]
if "apel" in fruits:
    print("Apel ada di dalam daftar buah.")
else:
    print("Apel tidak ada di dalam daftar buah.")

numbers = [1, 2, 3, 4, 5]
if 3 in numbers:
    print("Angka 3 ada di dalam daftar angka.")
else:
    print("Angka 3 tidak ada di dalam daftar angka.")

email_str = "contoh@email.com"
if "@" in email_str and "." in email_str:
    print("Email valid.")
else:
    print("Email tidak valid.")