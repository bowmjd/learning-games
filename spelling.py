# spelling.py
# Practice spelling
import random
import time
import playsound

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

wordlist_path = r"data/english-top-3000.txt"
mp3_path = "download"
max_tries = 3
max_seconds = 30

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

# create_spelling_deck(wordlist_path, max_seconds)
# Create spelling deck from wordlist file.
# Return a FlashcardDeck.
def create_spelling_deck(wordlist_path, mp3_path, max_seconds):
    deck = FlashcardDeck()
    with open(wordlist_path, 'r') as f:
        line = f.readline()
        while line:
            deck.add(Flashcard(f'{mp3_path}/{line.lower().strip()}.mp3', line.strip(), max_seconds))
            line = f.readline()
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
# operation = prompt_for_int('Enter 1 for addition, 2 for subtraction, 3 for addition and subtraction, 4 for multiplication: ', 1, 4)

# Create deck
deck = create_spelling_deck(wordlist_path, mp3_path, max_seconds)

# Main loop
quit_game = False
total_attempts = 0
correct = 0
mastered = 0
total_seconds = 0
card = deck.next()
tries = 0
while not quit_game and card != None:
    sound_played = False
    while not sound_played:
        try:
            playsound.playsound(card.front)
            sound_played = True
        except:
            card = deck.next()
    start_time = time.time()
    answer = input('\nType the spelling here: ').strip()
    if answer.upper() == 'Q':
        quit_game = True
    else:
        end_time = time.time()
        total_attempts += 1
        tries += 1
        answer_seconds = end_time - start_time
        total_seconds += answer_seconds
        (is_correct, is_mastered) = card.attempt(answer, answer_seconds)
        # If mastered, do not return the card to the deck
        if is_mastered:
            mastered += 1
            card = deck.next()
        # If not mastered and tries > max_tries, return the card to the deck
        elif tries >= max_tries:
            deck.add(card)
            card = deck.next()
        if is_correct:
            correct += 1
            tries = 0
            print(correct_msg)
        else:
            print(incorrect_msg)

# Show stats and exit
if total_attempts == 0:
    pct_correct = 0.0
    pct_mastered = 0.0
    seconds_per_answer = 0.0
else:
    pct_correct = round(correct * 100.0 / total_attempts, 1)
    pct_mastered = round(mastered * 100.0 / total_attempts, 1)
    seconds_per_answer = round(total_seconds * 1.0 / total_attempts, 1)
print(f"""

Attempted: {total_attempts}
Correct: {correct} ({pct_correct}%)
Mastered: {mastered} ({pct_mastered}%)
Avg Seconds per Answer: {seconds_per_answer}

Goodbye!
""")