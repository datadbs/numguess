import random

rand=random.randint(1,200)
print(rand)

username=input("input user's name >")
print(f"greeting {username}")

guess=input("assume user's guess")
print(guess==username)
