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

mastery_seconds = 2.0

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

# create_addition_deck(level)
# Create addition/subtraction flashcards with numbers 0, 1, ..., level
# return a FlashcardDeck
def create_addition_deck(level, max_seconds):
    deck = FlashcardDeck()
    for i in range(level + 1):
        for j in range(i + 1):
            deck.add(Flashcard(f'{j} + {i-j} = ', f'{i}', max_seconds))
            deck.add(Flashcard(f'{i} - {j} = ', f'{i-j}', max_seconds))
    return deck

# create_multiplication_deck(level)
# Create multiplication flashcards with numbers 1, ..., level
# return a FlashcardDeck
def create_multiplication_deck(level, max_seconds):
    deck = FlashcardDeck()
    for i in range(1, level + 1):
        for j in range(1, level + 1):
            deck.add(Flashcard(f'{i} x {j} = ', f'{i*j}', max_seconds))
    return deck

# Prompt for addition/subtraction or multiplication
s = input('Enter 1 for addition/subtraction or 2 for multiplication: ')
operation = 0
while operation < 1:
    try:
        operation = int(s)
    except:
        pass
    if operation < 1:
        s = input('Invalid number.')

# Prompt for level
s = input('What is the largest number we should use? Enter a number between 1 and 20: ')
level = 0
while level < 1 or level > 20:
    try:
        level = int(s)
    except:
        pass
    if level < 1 or level > 20:
        s = input('Invalid number.')

# Prompt for max seconds per fact
s = input('How many seconds per fact? ')
max_seconds = 0
while max_seconds < 1:
    try:
        max_seconds = int(s)
    except:
        pass
    if max_seconds < 1:
        s = input('Invalid number.')

# Create deck
if operation == 1:
    deck = create_addition_deck(level, max_seconds)
else:
    deck = create_multiplication_deck(level, max_seconds)

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