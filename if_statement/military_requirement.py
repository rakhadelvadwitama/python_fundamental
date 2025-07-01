name = input("What is your name? ")
age = input("How old are you? ")
age = int(age)  # mengubah string menjadi integer
height = input("What is your height in cm? ")
height = int(height)  # mengubah string menjadi integer

if 100 > age >= 18 and height >= 170:
    print(f"{name}, you are eligible to join the military.")
elif 100 > age >=18 and height <= 170:
    print(f"{name}, you are not eligible to join the military due to height.")
else:
    print(f"{name}, you are not eligible to join the military due to age.")