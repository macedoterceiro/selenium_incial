

users = [
    {"username": "invalid", "email": "invalidemail", "password": "invalidpass"},
    {"username": "valid", "email": "validemail@gmail.com", "password": "validpass"},
    {"username": "empty", "email": "emptyemail", "password": ""},
    {"username": "", "email": "noreply@qa-practice.com", "password": "emptypass"},
    {"username": "admin", "email": "admin@qa-practice.com", "password": "special!@#pass"}
]

def get_user(name):
    try:
        return next(user for user in users if user["username"] == name)
    except:
        print("User not found")
        return None