# sign_up = [{"Username": "Jona", "Password": "pass123"},
#          {"Username": "Mercy", "Password": "kolo123"},
#           {"Username": "Funke", "Password": "sample123"}]


# def login(username, password):
#    for user, value in sign_up.item():
#        print(user[username])
# if user[username] == username and user[password] == password:
#   return "Login"
# else:
#   return False


# if __name__ == "__main__":
#    print(login("Mercy", "kolo123"))

saved_profile = {}


def sign_up():
    user_profile = {
        "First Name": input("enter your first name"),
        "Last Name": input("enter your your last name"),
        "Email Address": input("enter your email address"),
        "Password": input("enter your password")
    }
# saved_profile.update(user_profile.)

def log_in():
    user_profile = {
        "Email Address": input("enter your email address"),
        "Password": input("enter your password")
    }
sign_up()
for user in saved_profile.items():
    print(user,end="")