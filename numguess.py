from random import randint
from time import sleep

answer=randint(1,200)
print(answer)

username=input("input user's name >")
print(f"greeting {username}")

guess=int(input("assume user's guess"))


# Compare answer with user's guess
if guess==answer:
    print('************')
    sleep(1)
    print('************')
    sleep(1)
    print('************')
    sleep(1)
    print(f'You got it right!! The answer is {answer}!!')
elif guess>answer:
    print(f'keep going, man~! that was too high, {username}..')
elif guess<answer:
    print(f'keep going, man~! that was too low, {username}..')

