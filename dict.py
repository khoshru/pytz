
def get_dict():
    name = input("Enter your name")

    email = input("Enter your email")

    phone = input("Enter your phone")

    birthday = input("Enter your birthday")
    user = {
    "username": name,
    "email": email,
    "phone":phone ,
    "birtday": birthday
    }
    print(user)
get_dict()
