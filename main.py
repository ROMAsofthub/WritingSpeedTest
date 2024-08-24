import time
import random


def load_phrases():
    phrase_lines = open("phrases.txt", 'r').readlines()
    phrase_lines = [phrase.strip() for phrase in phrase_lines]
    return phrase_lines


def start_timer():
    return time.time()


def stop_timer(start_time):
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


def compare_phrases(phrase, usr_input) -> tuple[int, int, list[str], list[str]]:
    """

    :param phrase: The phrase to test against
    :param usr_input: The user's input
    :return: Tuple of correct words, incorrect words, list of inputted incorrect words, list of missed words
    """
    phrase_words = phrase.split(" ")  # split on spaces to get each word in a list
    usr_phrase = usr_input.split(" ")
    correct_count = 0
    incorrect_count = 0
    incorrect_words = []

    for word in usr_phrase:
        if word in phrase_words:
            phrase_words.remove(word)  # Don't let people cheat by writing the same word repeatedly!
            correct_count += 1
        else:
            incorrect_count += 1
            incorrect_words.append(word)
    return correct_count, incorrect_count, incorrect_words, phrase_words


def run_challenge(phrase):
    print('---- Target phrase: ----')
    print(phrase)
    print('----')
    print('Write it as fast as you can! The challenge starts in...')
    print('3!')
    time.sleep(1)
    print('2!')
    time.sleep(1)
    print('1!')
    time.sleep(1)
    print('GO!')
    start_time = start_timer()
    usr_input = input('-')
    elapsed_time = stop_timer(start_time)

    correct_count, incorrect_count, incorrect_words, missed_words = compare_phrases(phrase, usr_input)

    print('--Results--')
    print(f'Speed: {elapsed_time:.3f} seconds')
    print(f'{correct_count} correct words written and {incorrect_count} incorrect. ')
    if incorrect_words:
        print("Your incorrect words:", ', '.join(incorrect_words))
    if missed_words:
        print("Missed words:", ', '.join(missed_words))



if __name__ == '__main__':
    print(
        '         ,_  o_|_ o        _,      ,       _  _  _|      _|_  _  , _|_ \n'
        '|  |  |_/  | | |  | /|/|  / |     / \\_|/\\_|/ |/ / |       |  |/ / \\_|  \n'
        ' \\/ \\/     |/|/|_/|/ | |_/\\/|/     \\/ |_/ |_/|_/\\/|_/     |_/|_/ \\/ |_/\n'
        '                           (|        (|                               '
    )
    print('Welcome!')
    phrases = load_phrases()

    while True:
        choice = input('Do you want to List available phrases, Select a phrase, go Random, or Quit?  (l/s/r/q): ').lower()
        if choice in ['s', 'select']:
            phrase = phrases[int(input('Enter a phrase number: ')) - 1]
            run_challenge(phrase)
        elif choice in ['r', 'random']:
            phrase = random.choice(phrases)
            run_challenge(phrase)
        elif choice in ['l', 'ls', 'list']:
            for i, phrase in enumerate(phrases):
                print(f'{i+1}. {phrase}')
        elif choice in ['q', 'quit']:
            print("Goodbye")
            exit()
        else:
            pass  # bad input, try again
