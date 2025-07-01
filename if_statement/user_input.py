# user input digunakan untuk meminta user memasukkan input(input ketikan di dalam terminal)
# kedalam program kita, input yang dimasukkan akan selalu berupa string,
# tetapi kita bisa mengubahnya menjadi tipe data lain jika diperlukan

age = input("How old are you? ")
print(type(age))  # Output: <class 'str'>, karena input selalu berupa string
age = int(age)  # mengubah string menjadi integer
print(type(age))  # Output: <class 'int'>, karena sudah diubah menjadi
hoby = input("What is your hobby? ")
print(f"Your hobby is {hoby}")
print(type(hoby))  # Output: <class 'str'>, karena input selalu berupa string

print(f"You are {age} years old and your hobby is {hoby}")
after_10_years = age + 10
print(f"After 10 years, you will be {after_10_years} years old and your hobby will still be {hoby}. It will be great to see how your hobby evolves!")

