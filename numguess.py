import random
import time

answer=random.randint(1,200)
print(answer)

username=input("input user's name >")
print(f"greeting {username}")

guess=int(input("assume user's guess"))


# Compare answer with user's guess
if guess==answer:
    print('************')
    print(1)
    print('************')
    print(1)
    print('************')
    print(1)
    print(f'You got it right!! The answer is {answer}!!')
elif guess>answer:
    print(f'keep goning, man~! that was too high, {username}..')
elif guess<answer:
    print(f'keep goning, man~! that was too low, {username}..')

