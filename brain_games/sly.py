from random import randint


def is_even():
    name = input('May I have your name?')
    print('Hello, ', name, '!', sep='')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    cnt = 0
    while cnt < 3:
        random_number = randint(-99, 99)
        print('Question:', random_number)
        answer = input('Your answer: ')
        if (random_number % 2 == 0 and answer == 'yes') or (random_number % 2 != 0 and answer == 'no'):
            print('Correct!')
            cnt += 1
        else:
            # Определяем правильный ответ
            correct_answer = 'yes' if random_number % 2 == 0 else 'no'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print('Congratulations,', name + '!')