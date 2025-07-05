import json

def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
    
def save_json(filename, db):
    with open(filename, 'w') as file:
        json.dump(db, file)

def login(db):
    username = input('Username:')
    password = input('Password:')
    if username in db and db[username]['password1'] == password:
        print('login success, welcome', db[username]['name'])
        return db[username]
    else:
        raise ValueError('login failed, username or password is incorrect') # raise itu digunakan untuk mengeluarkan error, jadi kita bisa menangkapnya di bagian lain dari program kita.
    
def register(db):
    username = input('Username:')
    password1 = input('Password:')
    password2 = input('Confirm Password:')
    if password1 == password2 and username not in db:
        print('Register success')
        db[username] = {
            'name': username,
            'password1': password1,
            'password2': password2,
            'todos': []
        }
        save_json('db.json', db)
    else:
        raise ValueError('Register failed, password does not match or username already exists')

if __name__ == "__main__":
    db = read_json('db.json')
    register(db)
    # user = login(db)
    # print(user)