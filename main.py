def main():
    print("Hello World!")
    words = []
    with open('./assets/valid-wordle-words.txt', 'r', encoding= 'UTF-8') as file:
        words = [line.strip() for line in file.readlines()]
    print(words[:5])

    while True: 
        guessed_word = input('type your guess (empty for exit):')
        if len(guessed_word) == 0:
            break
        
        if len(guessed_word) != 5:
            print('your guess should have 5 letters')

if __name__ == '__main__':
    main()
