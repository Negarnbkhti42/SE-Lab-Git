def load_valid_words(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        return [line.strip() for line in file.readlines()]

def main():
    print("Hello World!")

    valid_words = load_valid_words('./assets/valid-wordle-words.txt')
    print(valid_words[:5])

    while True:
        guessed_word = input('Type your guess (press Enter to exit): ')
        
        if not guessed_word:
            break

        if len(guessed_word) != 5:
            print('Your guess should have exactly 5 letters.')
        else:
            # Your logic for processing the guessed word goes here.

if __name__ == '__main__':
    main()
