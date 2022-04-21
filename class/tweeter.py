tweets = [{"username": "bayer loop", "age": 35, "tweets": ["hello class", "i am bored"], "verify": "false"},
          {"username": "law loop", "age": 27, "tweets": ["hello class", "i am bored"], "verify": "false"},
          {"username": "bayer hope", "age": 25, "tweets": ["hello class", "i am bored"], "verify": "false"},
          {"username": "joy loop", "age": 34, "tweets": ["hello class", "i am bored", "i feel fine", "how was class"],
           "verify": "true"},
          {"username": "hope loop", "age": 20, "tweets": ["hello class", "i am happy", "how are you ?"],
           "verify": "false"},
          {"username": "love hope", "age": 22, "tweets": ["i am bored"], "verify": "false"},
          {"username": "love peace", "age": 32, "tweets": ["hello everyone", "i want to eat", "what do u have to say"],
           "verify": "true"}]

print([tweet["username"] for tweet in tweets  if tweet["verify"] == "true"])
print([tweet["username"] for tweet in tweets if tweet["age"] > 30 and tweet["verify"] == "true"])
print(sorted([tweet["age"] for tweet in tweets]))
print(sorted([tweet["age"] for tweet in tweets], reverse=True))

print(max([tweet["tweets"] for tweet in tweets]))

user_age = [tweet["age"] for tweet in tweets]
print(max(user_age))

print(min(user_age))

from statistics import mean

user_age_average = sum(user_age) / len(user_age)
print(f"the average age of the users {user_age_average: .2f}")
al = filter(lambda x: x["username"], tweets)
a2 = map(lambda y: y["username"], filter(lambda x: x["username"], tweets))
a3 = [user["username"] for user in tweets if user["verify"]]
a4 = filter(lambda x: x, map(lambda x: x["username"] if x["verify"] else False, tweets))
print(mean(user["age"] for user in tweets))

print(al)
print(a2)
print(a3)
print(a4)
most_tweet = max(tweets, key=lambda user: len(user["tweets"]))["username"]
most_tweet1 = max(tweets, key=lambda user: len(user["tweets"]))["tweets"]
most_tweet2 = max(tweets, key=lambda user: len(user["tweets"]))["age"]
most_tweet3 = max(tweets, key=lambda user: len(user["tweets"]))
print(most_tweet)
print(most_tweet1)
print(most_tweet2)
print(most_tweet3)
