def main():
    print("Hello World!")
    while True: 
        guessed_word = input('type your guess (empty for exit):')
        if len(guessed_word) == 0:
            break
        
        if len(guessed_word) != 5:
            print('your guess should have 5 letters')

if __name__ == '__main__':
    main()
