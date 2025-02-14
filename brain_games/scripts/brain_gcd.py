from games.engine import core 
from random import randint
from math import gcd


def generate_question():
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    correct_answer = gcd(num1, num2)
    question = f'{num1} {num2}'
    return question, str(correct_answer)

def main():
    game_description = "Find the greatest common divisor of given numbers."
    core(game_description, generate_question)

if __name__ == "__main__":
    main()
