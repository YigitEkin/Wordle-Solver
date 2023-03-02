from words import words

def filter_words_with_char_index(words, character, index):
    filtered_words = []
    for word in words:
        if word[index] == character:
            filtered_words.append(word)
    return filtered_words

def filter_words_without_char_index(words, character, index):
    filtered_words = []
    for word in words:
        if word[index] != character:
            filtered_words.append(word)
    return filtered_words

def filter_words_contains(words, character, index):
    filtered_words = []
    for word in words:
        if word[index] != character and character in word:
            filtered_words.append(word)
    return filtered_words

def filter_words_does_not_contain(words, character):
    filtered_words = []
    for word in words:
        if character not in word:
            filtered_words.append(word)
    return filtered_words

def get_character_list(list):
    return list.split(" ")


def main():
    print("Welcome to the Copilot!")

    print("If you are just starting out, you can use the following words: ")
    print ("""


React
Adieu
Later
Sired
Tears
Alone
Arise
About
Atone
Irate
Snare
Cream
Paint
Worse
Sauce
Anime
Prowl
Roast
Drape
Media


""")

    print("enter the operation you want to perform")
    print("1. filter words with character at an certain index")
    print("2. filter words without character at an certain index")
    print("3. filter words that contain character but not at the specified index")
    print("4. filter words that do not contain character")
    print("5. quit")

    filtered_words = words

    while True:
        operation = input("operation: ")

        if operation == "1":
            character = input("character: ")
            index = int(input("index: "))
            filtered_words = filter_words_with_char_index(filtered_words, character, index)

        elif operation == "2":
            character = input("character: ")
            index = int(input("index: "))
            filtered_words = filter_words_without_char_index(filtered_words, character, index)

        elif operation == "3":
            character = input("character: ")
            index = int(input("index: "))
            filtered_words = filter_words_contains(filtered_words, character, index)

        elif operation == "4":
            character = input("enter the character list that you want to filter with spaces in between: ")
            character_list = get_character_list(character)
            for character in  character_list:
                filtered_words = filter_words_does_not_contain(filtered_words, character)

        elif operation == "5":
            break

        print("filtered words: ", filtered_words)

if __name__ == "__main__":
    main()