import prompt


def greet():
    name = prompt.string('May I have your name?')
    print('Hello, ', name, '!', sep='')
