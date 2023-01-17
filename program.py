# Create a dictionary to store the word pairs
words = {}

# Function to add new words to the dictionary
def add_word(native, foreign):
    words[native] = foreign

# Function to translate a native word to foreign
def translate(native):
    if native in words:
        return words[native]
    else:
        return "Word not found."

# Function to test user's knowledge of the words
def test():
    score = 0
    for native, foreign in words.items():
        answer = input(f"Translate {native}: ")
        if answer == foreign:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {foreign}.")
    print(f"You scored {score} out of {len(words)}.")

# Function to revise words
def revise():
    for native, foreign in words.items():
        print(f"{native} : {foreign}")

# Add some words to the dictionary
add_word("book", "livre")
add_word("table", "table")
add_word("car", "voiture")

while True:
    print("Welcome to the Word Reviewer.")
    print("1. Test your knowledge")
    print("2. Revise words")
    print("3. Add new word")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        test()
    elif choice == "2":
        revise()
    elif choice == "3":
        native = input("Enter native word: ")
        foreign = input("Enter foreign word: ")
        add_word(native, foreign)
    elif choice == "4":
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")