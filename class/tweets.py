peoples = [
    {"user_name": "Jonathan", "age": 30, "tweets": ["I love Pyhton"], "verified": False},
    {"user_name": "Funmi", "age": 29, "tweets": ["I love python", "Wowww", "Hello World", "Happy Birthday"],
     "verified": True},
    {"user_name": "Tolani", "age": 39, "tweets": ["Shut the fuck up!", "What a beautiful sky"], "verified": True},
    {"user_name": "Samsom", "age": 17, "tweets": ["Tatatata", "More tatatata", "Extra tatata"], "verified": True},
    {"user_name": "Ezekiel", "age": 15, "tweets": ["I love coding"], "verified": False},
    {"user_name": "Segun", "age": 17, "tweets": ["I love coding", "To the moon"], "verified": False},
    {"user_name": "Sikiru", "age": 24, "tweets": ["I LOVE ELON MUSK"], "verified": True},
    {"user_name": "Philip", "age": 32, "tweets": ["Pass it", "Pass another one", "Pass another one"],
     "verified": False},
    {"user_name": "Florennce", "age": 22, "tweets": ["I'm single"], "verified": False},
    {"user_name": "Amaka", "age": 27, "tweets": ["Wowww", "Are you joking with me"], "verified": False},
]
age = [30, 29, 39, 17, 15, 17, 24, 32]
print(([people["user_name"] for people in peoples if people["verified"] == True]))
a2 = map (lambda y: y['user_name'], filter(lambda x: x['verified'], peoples))
a3 = filter(lambda x: x, map(lambda x: x['user_nme'] if x['verified'] else False, peoples))





print([people["user_name"] for people in peoples if people["age"] <= 25])
user_age = ([people["age"] for people in peoples])
age_max = max(user_age)
print(age_max)
user_age_min = ([people["age"] for people in peoples])
age_min = min(user_age_min)
print(age_min)

age_average = ([people["age"] for people in peoples])
age_sum = sum(age_average) / len(age_average)
print(age_sum)

print(sorted([people["user_name"] for people in peoples]))
descending = (sorted([people["user_name"] for people in peoples]))
print(sorted(descending, reverse= True ))

print(sorted([people[age] for people in peoples]))

length_of_name = (len([people["user_name"] for people in peoples]))
# name_len = len(length_of_name)
print(length_of_name)