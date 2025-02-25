from games.engine import core 
from random import randint


def generate_question():
    start = randint(1, 100)
    step = randint(1, 5)
    length = randint(5, 10)
    progression = [start + step * i for i in range(length)]
    hidden_index = randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, str(correct_answer)


def main():
    game_description = "What number is missing in the progression?"
    core(game_description, generate_question)

if __name__ == "__main__":
    main()
