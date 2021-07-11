import random


def binary_search():
    min_num = 1
    max_num = 100
    count = 0
    while True:
        num = random.randint(min_num, max_num)
        guess_num = int(input('Type your number: '))
        if guess_num < num:
            print('Your number is less than guessed number')
            max_num = num - 1
            count += 1
        elif guess_num > num:
            print('Your number is bigger than guessed number')
            guess_num += 1
            min_num = num + 1
        elif guess_num == num:
            print(f'I guessed your number, it is {guess_num}')
            print(f'I have guessed in {count} tries')
            break
        else:
            print('I can\'t guess your number' )

        

       
binary_search()



