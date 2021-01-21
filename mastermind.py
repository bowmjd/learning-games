# mastermind.py
# Create a code and allow the user to guess
import random

colors = ['black', 'white', 'red', 'blue', 'green', 'yellow', 'purple', 'orange', 'teal', 'pink']
short_colors = ['B', 'W', 'R', 'L', 'G', 'Y', 'P', 'O', 'T', 'N']

# get_code(code_length, num_colors)
# Generate a code with the given length and number of colors
def get_code(code_length, num_colors):
    code = ''
    for i in range(code_length):
        code += short_colors[random.randint(0, num_colors - 1)]
    return code

# print_colors(num_colors)
# Show list of valid colors
def show_colors(num_colors):
    print('Available colors: ')
    for i in range(num_colors):
        print(f'{short_colors[i]} = {colors[i]}', end='')
        if i == num_colors - 1:
            print()
        else:
            print(', ', end='')

# check_colors(guess, num_colors)
# Check whether the colors in the guess are valid.
def check_colors(guess, num_colors):
    for i in range(len(guess)):
        if not guess[i] in short_colors[0:num_colors]:
            print(f'{guess[i]} is an invalid color.')
            return False
    return True

# check_code(guess, answer)
# Print a message describing how well the guess matches.
# Return (guess correct?, # red, # white)
def check_code(guess, answer):
    if guess == answer:
        return (True, 4, 0)
    # Count exact matches
    red = 0
    guess_unmatched = ''
    answer_unmatched = ''
    for i in range(len(answer)):
        if guess[i] == answer[i]:
            red += 1
        else:
            guess_unmatched += guess[i]
            answer_unmatched += answer[i]
    # Count colors in the wrong position
    white = 0
    color_counts = dict(zip(short_colors, [0] * 10))
    for i in range(len(answer_unmatched)):
        color_counts[answer_unmatched[i]] += 1
    for j in range(len(guess_unmatched)):
        if color_counts[guess_unmatched[j]] > 0:
            white += 1
            color_counts[guess_unmatched[j]] -= 1
    return (False, red, white)

# print_history(guess_history, red_history, white_history)
def print_history(guess_history, red_history, white_history):
    for i in range(len(guess_history)):
        if red_history[i] == 1:
            red_text = '1 red'
        else:
            red_text = f'{red_history[i]} reds'
        if white_history[i] == 1:
            white_text = '1 white'
        else:
            white_text = f'{white_history[i]} whites'
        print(f'Guess: {guess_history[i]} >>> {red_text}, {white_text}')

# Prompt for length of code
s = input('How long should the code be? Enter a number between 1 and 10: ')
code_length = 0
while code_length < 1 or code_length > 10:
    try:
        code_length = int(s)
    except:
        pass
    if code_length < 1 or code_length > 10:
        s = input('Invalid number. How long should the code be? Enter a number between 1 and 10: ')

# Prompt for number of colors
s = input('How many colors? Enter a number between 1 and 10: ')
num_colors = 0
while num_colors < 1 or num_colors > 10:
    try:
        num_colors = int(s)
    except:
        pass
    if num_colors < 1 or num_colors > 10:
        s = input('Invalid number. How many colors? Enter a number between 1 and 10: ')

# Main loop
quit_game = False
solved = 0
while not quit_game:
    answer = get_code(code_length, num_colors)
    correct_guess = False
    guess_history = []
    red_history = []
    white_history = []
    print(f'You have solved {solved} codes correctly. Creating a new code...')
    while not correct_guess and not quit_game:
        show_colors(num_colors)
        guess = input('Enter your guess, Q to quit, or X to skip. Example: BBB for 3 black colors in a row. >>>')
        guess = guess.upper().strip()
        if guess == 'Q' or guess == 'QUIT':
            quit_game = True
        elif guess == 'X' or guess == 'SKIP':
            print(f'Skipping this code. The answer was: {answer}')
            correct_guess = True
        else:
            if not check_colors(guess, num_colors):
                print(f'The code is {len(answer)} colors long!')
            elif len(guess) != len(answer):
                print(f'The code is {len(answer)} colors long!')
            else: 
                (correct_guess, red, white) = check_code(guess, answer)
                if correct_guess:
                    solved += 1
                    print('You are correct!')
                else:
                    guess_history += [guess]
                    red_history += [red]
                    white_history += [white]
                    print_history(guess_history, red_history, white_history)
print(f'You have solved {solved} codes correctly. Goodbye!')

