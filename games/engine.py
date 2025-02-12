def greet():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f'Hello, {name}!')
    return name

def core(game_description, generate_question):
    name = greet()
    print(game_description)
    cnt = 0
    while cnt < 3:
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        your_answer = input("Your answer: ")
        if your_answer == correct_answer:
            print("Correct!")
            cnt += 1
        else:
            print(f"'{your_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            cnt = 0
    if cnt == 3:
        print(f"Congratulations, {name}!")
