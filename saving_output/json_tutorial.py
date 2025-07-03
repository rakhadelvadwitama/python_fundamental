# library JSON untuk menyimpan data ke dalam file JSON. karena dalam python kita tidak bisa membaca file Excel secara langsung, kita bisa mengkonversi data kita ke dalam format JSON dan menyimpannya ke dalam file .json

import json

with open('data.json', 'r') as f:
    data = json.load(f)

print(data)
print(type(data))
print(data['members'][0]['name'])  # Mengakses nilai dari key 'members'
print(type(data['members'][0]['name']))  # Mengakses nilai dari key 'name'

todos = {'todos': ['todo1', 'todo2', 'todo3']}
with open('todos.json', 'w') as f:
    json.dump(todos, f)  # Menyimpan set todos ke dalam file JSON
    # json.dump(todos, f, indent=4)  # Untuk format yang lebih rapi dengan indentasi
with open('todos.json', 'r') as f:
    data = json.load(f)  # Membaca data dari file JSON
print(data['todos'][0])  # Mengakses nilai dari key 'todos'