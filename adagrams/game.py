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
    letter_bank_copy = letter_bank[:]

    for char in word.upper():
        if char in letter_bank_copy:
            letter_bank_copy.remove(char)
        else:
            return False

    return True

def score_word(word):
    score_chart = {
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: ['K'],
        8: ['J', 'X'],
        10: ['Q', 'Z']
    }

    letter_points = {}
    for points, letters in score_chart.items():
        for letter in letters:
            letter_points[letter] = points

    total_score = 0
    for char in word.upper():
        if char in letter_points:
            total_score += letter_points[char]

    if 7 <= len(word) <= 10:
        total_score += 8

    return total_score  

def get_highest_word_score(word_list):
    highest_score = 0
    best_word = None

    for word in word_list:
        score = score_word(word)

        if score > highest_score:
            highest_score = score
            best_word = word

        elif score == highest_score:
            if len(best_word) != 10 and len(word) == 10:
                best_word = word
            elif len(best_word) != 10 and len(word) < len(best_word):
                best_word = word
                
    return (best_word, highest_score)