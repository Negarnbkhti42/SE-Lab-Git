def main():
    print("Hello World!")
    words = []
    with open('./assets/valid-wordle-words.txt', 'r', encoding= 'UTF-8') as file:
        words = [line.strip() for line in file.readlines()]
    print(words[:5])
    

if __name__ == "__main__":
    main()
