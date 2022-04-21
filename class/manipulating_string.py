user_access = [{"Username": "Jona", "Password": "pass123"},
               {"Username": "Mercy", "Password": "kolo123"},
               {"Username": "Funke", "Password": "sample123"}]

# user_access = {
#     "favourite_food": ["rice", "beans", "dodo"],
#     "favourite_players": {"Arsenal": "Busayo", "Chelsea": "Lukaku", "Dekanorbs": "Shege"},
#     "favourite_girl": "Funke",
#     "favourite_music": ["last last", "buga", "azonto"],
#     "favourite_language": {"Programming": "Python", "Dialect": "Yoruba", "Slang": "Breakfast"}
# }1`


def lst_checker(username, password):
    for user in user_access:
        if user["Username"] == username and user["Password"] == password:
            return True
    else:
        return False

# def type_checker():
#     for value in user_access.values():
#         if type(value) == str:
#             print("This is a string")
#         elif type(value) == dict:
#             print( "This is a dictionary")
#         else:
#             print( "This is a list")
# contact_details = {
#     "fullname": "Adebayo Steven",
#     "phone_number": ["08012334522"],
#     "school": {"cohort10": "semicolon", "cohort9": "jonaa"}
# }
#
#
# def number(number1):
#     for details in contact_details.values():
#         if type(details) == list:
#             details.append(number1)
#     return contact_details


# if __name__ == "__main__":
#     print(number("09863221346"))
