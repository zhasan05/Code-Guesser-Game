import random

CODES = ['R', 'B', 'G', 'W', 'Y', 'O']
CODE_LENGTH = 4
MAX_TRIES = 10

def generate_code():
    code_list = []
    for _ in range(CODE_LENGTH):
        ran_code = random.choice(CODES)
        code_list.append(ran_code)
    print(code_list)
    return code_list

def guess_code():
    while True:
        player_guess = input(f'Please guess the {CODE_LENGTH} digit code.').upper().split(' ')

        if len(player_guess) != CODE_LENGTH:
            print(f'Your code length is incorrect! You need to enter {CODE_LENGTH} digits code.')
            continue

        for code in player_guess:
            if code not in CODES:
                print(f'You have guessed the wrong code {code}! Please try again!')
                break
        else:
            break

    print(player_guess)
    return player_guess

def check_code(guessed_code, real_code):
    code_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for code in real_code:
        code_counts[code] = code_counts.get(code, 0) + 1

    # First pass: exact matches, consume from the pool
    for guess, real in zip(guessed_code, real_code):
        if guess == real:
            correct_pos += 1
            code_counts[guess] -= 1

    # Second pass: right color, wrong position (skip exact matches)
    for guess, real in zip(guessed_code, real_code):
        if guess != real and code_counts.get(guess, 0) > 0:
            incorrect_pos += 1
            code_counts[guess] -= 1

    return correct_pos, incorrect_pos

def play_game():
    print(f'Welcome to the code guesser game! You have {MAX_TRIES} tries only.')
    print(f'The valid code colors are {CODES}')

    system_code = generate_code()

    for attempts in range(1, MAX_TRIES+1):
        player_code = guess_code()
        corr_pos, incorr_pos = check_code(player_code, system_code)

        if corr_pos == CODE_LENGTH:
            print(f'You guessed the code in {attempts} tries!')
            break

        print(f'Incorrect position: {incorr_pos} | Correct position: {corr_pos}')

    else:
         print(f'You ran out of the max {MAX_TRIES}, the code is: {player_code}')

if __name__  ==  '__main__':
    play_game()