# mathfacts.py
# Review addition, subtraction, and multiplication facts
import random
import time

correct_msg = """

   * * * *
 *         *
*   *   *   *  YOU ARE CORRECT!
*           *
 *  \___/  *
   * * * * 
"""

incorrect_msg = """

* * * * * * * * * * * * 
*                     *
*  SORRY! TRY AGAIN!  * 
*                     *
* * * * * * * * * * * *
"""


class Flashcard:
    def __init__(self, front, back, max_recall_time):
        self.front = front
        self.back = back
        self.max_recall_time = max_recall_time

    # Flashcard.attempt(self, answer, answer_seconds)
    # Update flashcard stats.
    # Returns (is_correct, is_mastered)
    def attempt(self, answer, answer_seconds):
        if (answer == self.back and answer_seconds <= self.max_recall_time):
            return (True, True)
        elif answer == self.back:
            return (True, False)
        else:
            return (False, False)

class FlashcardDeck:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards += [card]

    # FlashcardDeck.next(self)
    # Draw a flashcard at random from the deck and remove it.
    # If the card needs to be replaced, use the add method to
    # replace it.
    def next(self):
        if len(self.cards) == 0:
            return None
        else:
            i = random.randint(0, len(self.cards) - 1)
            card = self.cards[i]
            self.cards = self.cards[0:i] + self.cards[i+1:]
            return card

# create_addition_deck(min_num, max_num, max_seconds)
# Create addition flashcards with numbers min_num, ..., max_num
# return a FlashcardDeck
def create_addition_deck(min_num, max_num, max_seconds):
    deck = FlashcardDeck()
    for i in range(min_num, max_num + 1):
        for j in range(i + 1):
            deck.add(Flashcard(f'{j} + {i-j} = ', f'{i}', max_seconds))
    return deck

# create_subtraction_deck(min_num, max_num, max_seconds)
# Create subtraction flashcards with numbers min_num, ..., max_num
# return a FlashcardDeck
def create_subtraction_deck(min_num, max_num, max_seconds):
    deck = FlashcardDeck()
    for i in range(min_num, max_num + 1):
        for j in range(i + 1):
            deck.add(Flashcard(f'{i} - {j} = ', f'{i-j}', max_seconds))
    return deck

# create_addition_subtraction_deck(min_num, max_num, max_seconds)
# Create addition and subtraction flashcards with numbers min_num, ..., max_num
# return a FlashcardDeck
def create_addition_subtraction_deck(min_num, max_num, max_seconds):
    deck = FlashcardDeck()
    for i in range(min_num, max_num + 1):
        for j in range(i + 1):
            deck.add(Flashcard(f'{j} + {i-j} = ', f'{i}', max_seconds))
            deck.add(Flashcard(f'{i} - {j} = ', f'{i-j}', max_seconds))
    return deck

# create_multiplication_deck(min_num, max_num, max_seconds)
# Create multiplication flashcards with numbers min_num, ..., max_num
# return a FlashcardDeck
def create_multiplication_deck(min_num, max_num, max_seconds):
    deck = FlashcardDeck()
    for i in range(min_num, max_num + 1):
        for j in range(1, max_num + 1):
            deck.add(Flashcard(f'{i} x {j} = ', f'{i*j}', max_seconds))
    return deck

# create_division_deck(min_num, max_num, max_seconds)
# Create division flashcards with numbers min_num, ..., max_num
# return a FlashcardDeck
def create_division_deck(min_num, max_num, max_seconds):
    deck = FlashcardDeck()
    for i in range(min_num, max_num + 1):
        for j in range(1, max_num + 1):
            deck.add(Flashcard(f'{i*j} / {j} = ', f'{i}', max_seconds))
    return deck

# prompt_for_int(prompt, min_int, max_int, error_msg)
# Prompt for a positive integer between min_int and max_int (inclusive) and return it.
def prompt_for_int(prompt, min_int, max_int, error_msg='Invalid number.'):
    if min_int >= max_int:
        raise Exception(f'Invalid bounds: min_int={min_int}, max_int={max_int}')
    s = input(prompt)
    num = min_int - 1
    while num < min_int or num > max_int:
        try:
            num = int(s)
        except:
            pass
        if num < min_int or num > max_int:
            print(error_msg)
    return num

# Prompt for addition/subtraction or multiplication
operation = prompt_for_int('Enter 1 for addition, 2 for subtraction, 3 for addition and subtraction, 4 for multiplication, 5 for division: ', 1, 5)

# Prompt for min_num
min_num = prompt_for_int('What is the smallest number we should use? Enter a number between 1 and 20: ', 1, 20)

# Prompt for max_num
max_num = prompt_for_int(f'What is the largest number we should use? Enter a number between {min_num} and 20: ', min_num, 20)

# Prompt for max seconds per fact
max_seconds = prompt_for_int('How many seconds per fact? ', 1, 10000)

# Create deck
if operation == 1:
    deck = create_addition_deck(min_num, max_num, max_seconds)
elif operation == 2:
    deck = create_subtraction_deck(min_num, max_num, max_seconds)
elif operation == 3:
    deck = create_addition_subtraction_deck(min_num, max_num, max_seconds)
elif operation == 4:
    deck = create_multiplication_deck(min_num, max_num, max_seconds)
else:
    deck = create_division_deck(min_num, max_num, max_seconds)
    

# Main loop
quit_game = False
attempts = 0
correct = 0
mastered = 0
total_seconds = 0
card = deck.next()
while not quit_game and card != None:
    start_time = time.time()
    print('')
    answer = input(f'Enter your answer or Q to quit. {card.front}').strip()
    if answer.upper() == 'Q':
        quit_game = True
    else:
        end_time = time.time()
        attempts += 1
        answer_seconds = end_time - start_time
        total_seconds += answer_seconds
        (is_correct, is_mastered) = card.attempt(answer, answer_seconds)
        if is_mastered:
            mastered += 1
        else:
            deck.add(card)
        if is_correct:
            correct += 1
            print(correct_msg)
            card = deck.next()
        else:
            print(incorrect_msg)

# Show stats and exit
if attempts == 0:
    pct_correct = 0.0
    pct_mastered = 0.0
    seconds_per_answer = 0.0
else:
    pct_correct = round(correct * 100.0 / attempts, 1)
    pct_mastered = round(mastered * 100.0 / attempts, 1)
    seconds_per_answer = round(total_seconds * 1.0 / attempts, 1)
print(f"""

Attempted: {attempts}
Correct: {correct} ({pct_correct}%)
Mastered: {mastered} ({pct_mastered}%)
Avg Seconds per Answer: {seconds_per_answer}

Goodbye!
""")