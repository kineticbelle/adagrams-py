from random import randint

def draw_letters():
    #returns an array of ten strings each containing one letter
    #randomly drawn letters from pool of letters for the correct amount of letters available 
    #this function should **not** change the pool of letters

    LETTER_BANK_COUNT = {
        'A': 9, 
        'B': 2, 
        'C': 2, 
        'D': 4, 
        'E': 12, 
        'F': 2, 
        'G': 3, 
        'H': 2,
        'I': 9, 
        'J': 1, 
        'K': 1, 
        'L': 4, 
        'M': 2, 
        'N': 6, 
        'O': 8, 
        'P': 2,
        'Q': 1, 
        'R': 6, 
        'S': 4, 
        'T': 6, 
        'U': 4, 
        'V': 2, 
        'W': 2, 
        'X': 1,
        'Y': 2, 
        'Z': 1
    }
    letter_pool = []
    for letter, count in LETTER_BANK_COUNT.items(): 
        for _ in range(count):
            letter_pool.append(letter)
    
    remaining_letters = {letter: count for letter, count in LETTER_BANK_COUNT.items()}
    
    player_tiles = []
    for _ in range(10):
        while True:
            index = randint(0, len(letter_pool)-1)
            letter = letter_pool[index]
        
            if remaining_letters[letter] > 0:
                player_tiles.append(letter_pool[index])
                remaining_letters[letter] -= 1
                break

    return player_tiles

print(draw_letters())

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass