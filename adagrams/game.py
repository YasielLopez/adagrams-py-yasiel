from random import randint

LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12,
    'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1,
    'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8,
    'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6,
    'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2,
    'Z': 1
}

def draw_letters():
    # Create a list with the correct distribution of letters
    all_letters = []
    for letter, count in LETTER_POOL.items():
        all_letters += [letter] * count

    hand = []
    used_indices = set()

    while len(hand) < 10:
        index = randint(0, len(all_letters) - 1)
        if index not in used_indices:
            hand.append(all_letters[index])
            used_indices.add(index)

    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass