# integer -> bilangan bulat ex: 1, 2, 3, -1, -2, -3
# float -> bilangan pecahan ex: 1.5, 2.3, -1.5, -2.3

# integer dan float support operasi matematika meliputi penjumlahan, pengurangan, perkalian, pembagian, modulus, pangkat
# integer dan float untuk operasi matematika mengikuti aturan yang dihitung awal adalah operasi di dalam kurung, perkalian dan pembagian, kemudian baru penjumlahan dan pengurangan. jika memiliki beberapa kurung, maka kurung yang paling dalam akan dihitung terlebih dahulu.
# jika ada operasi yang memiliki prioritas yang sama, maka operasi tersebut akan dihitung dari kiri

number_x = 10
number_y = 5
result = number_x + number_y # penjumlahan
print(result) # -> 15

float_value_x = 10.5
float_value_y = 5.5
float_result = float_value_x + float_value_y # penjumlahan
print(float_result) # -> 16.0

result = number_x - number_y # pengurangan
print(result) # -> 5

float_result = float_value_x - float_value_y # pengurangan
print(float_result) # -> 5.0

result = number_x * number_y # perkalian
print(result) # -> 50

float_result = float_value_x * float_value_y # perkalian
print(float_result) # -> 57.75

result = number_x / number_y # pembagian
print(result) # -> 2.0 # disini hasilnya float karena pembagian jika tidak ingin menjadi float bisa menggunakan // (floor division)
result = number_x // number_y # floor division
print(result) # -> 2

float_result = float_value_x / float_value_y # pembagian
print(float_result) # -> 1.9090909090909092 # hasilnya float
float_result = float_value_x // float_value_y # floor division. walaupun menggunakan floor division, hasilnya tetap float karena float_value_x dan float_value_y adalah float
print(float_result) # -> 1.0 # hasilnya float

result = number_x % number_y # modulus
print(result) # -> 0 # modulus adalah sisa bagi, jadi 10 % 5 adalah 0 karena 10 habis dibagi 5
float_result = float_value_x % float_value_y # modulus
print(float_result) # -> 4.0 # sisa bagi dari 10.5 dan 5.5 adalah 4.0

result = number_x ** number_y # pangkat
print(result) # -> 100000 # 10 pangkat 5 adalah 100000
float_result = float_value_x ** float_value_y # pangkat
print(float_result) # -> 419.4510000000001 # 10.5 pangkat 5.5 adalah 419.4510000000001

#untuk merubah dari float ke integer bisa menggunakan int()
int_result = int(float_result)
print(int_result) # -> 4 # hasilnya 4