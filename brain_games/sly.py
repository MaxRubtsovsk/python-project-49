from random import randint


def is_even():
    name = input('May I have your name?')
    print('Hello, ', name, '!', sep='')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    cnt = 0
    flag = True
    while flag == True:
        while cnt < 3:
            random_number = randint(-9999999999, 9999999999)
            print('Question:', random_number)
            answer = input()
            if random_number % 2 == 0 and answer == 'yes' or random_number % 2 != 0 and answer == 'no':
                print('Correct!')
                cnt += 1
            else:
                if random_number % 2 == 0:
                    print("'no' is wrong answer ;(. Correct answer was 'yes'.", f"Let's try again, {name}!", sep='\n')
                    break
                else:
                    print("'yes' is wrong answer ;(. Correct answer was 'no'.", f"Let's try again, {name}!", sep='\n')
                    break
            if cnt == 3:
                print('Congratulations, ', name, '!', sep='')
            flag = False
