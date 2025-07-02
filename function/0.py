"""
f(x)=x+1
f(10)=10+1
f(10)=11
"""

"""
Fungsi di dalam python sebuah block kode yang dapat di eksekusi berulang kali.
Fungsi dapat menerima input (parameter / argumen) dan mengembalikan output (return value).
fungsi biasa digunakan untuk mengorganisir kode dan memecahkakn kode menjadi bagian-bagian yang lebih kecil dan mudah dipahami/dikelola. ini membuat kode lebih mudah dibaca, dipelihara, dan digunakan kembali. selain itu fungsi juga dapat digunakan untuk menghindari duplikasi kode yang sama di beberapa tempat / beberapa bagian program.
"""

def addition(x):
    output = x + 10
    return output # jika tidak ada return, maka outputnya None 
#calling function
addition_5 = addition(5)
print(addition_5)
print('-------')
print(addition(10))

#parameter dalam function boleh 0
def greet():
    print("Hello, World!")
#calling function
print(greet())  # outputnya None karena tidak ada return value

#parameter dalam function boleh lebih dari 1
def greet_user(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")
#calling function
greet_user("John", "Doe")  # output: Hello, John Doe!

# jika parameter berupa integer, maka dalam calling function untuk mencetak output 
