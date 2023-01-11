from random import randint
from time import sleep

answer=randint(1,200)
print(answer)

username=input("input user's name >")
print(f"greeting {username}")


point = 0

def numguess():
    # Compare answer with user's guess
    global point
    guess=int(input("assume user's guess"))
    if guess==answer:
        print('************')
        sleep(1)
        print('************')
        sleep(1)
        print('************')
        sleep(1)
        print(f'You got it right!! The answer is {answer}!!')
        point+=5
    elif guess>answer:
        print(f'keep going, man~! that was too high, {username}..')
    elif guess<answer:
        print(f'keep going, man~! that was too low, {username}..')

times = int(input("how many times do you want >>"))
for _ in range(times):
    numguess()

print(f'{point} points you got')