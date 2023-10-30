import random
print("hello world!")

def load_valid_words(path):
    words = []
    with open(path, 'r', encoding='UTF-8') as file:
        words = [word.strip() for word in file.readlines()]

    return words

def main():
    valid_words = load_valid_words('./assets/valid-wordle-words.txt')
    answer = random.choice(valid_words)

    while True:
        guessed_word = input('Type your guess (press Enter to exit): ')
        
        if not guessed_word:
            break

        if len(guessed_word) != 5:
            print('Your guess should have exactly 5 letters.')
        else:
            # Your logic for processing the guessed word goes here.
            if guessed_word == answer:
                print('you guessed right!')
                break
            else:
                print("try again!")
    print('the answer was:', answer)

if __name__ == '__main__':
    main()
