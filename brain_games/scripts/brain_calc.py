from games.engine import core 
from random import randint, choice


def generate_question():
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    operator = choice(['+', '-', '*'])
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    question = f'{num1} {operator} {num2}'
    return question, str(correct_answer)

def main():
    game_description = "What is the result of the expression?"
    core(game_description, generate_question)

if __name__ == "__main__":
    main()

