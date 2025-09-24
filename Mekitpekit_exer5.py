import random
def toLower(str):
    #make strings with similar index for similar chars
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    lowered = ''

    #loop for the str
    for i in range(len(str)):
        #check if char not a letter 
        if str[i] not in lowercase and str[i] not in uppercase:
            lowered += str[i]
        #check if the char is already lowercase
        elif str[i] in lowercase:
            lowered += str[i]
        else:
        #loop for checking uppercase
            for j in range(len(uppercase)):
                #if the char matches with an uppercase, add the value in lowercase with similar index
                if uppercase[j] == str[i]:
                    lowered += lowercase[j]
    
    return lowered

def game():
    while True:
        print("===== welcome to Terminal Wordle =====")
        print()
        print("\t[1] Play Game")
        print("\t[2] Manage word pool")
        print("\t[0] Exit")
        print()

        choice = int(input("Choice: "))
        if choice == 1:
            playGame()
        elif choice == 2:
            managePool()
        elif choice == 0:
            print("Goodbye!")
            break
        else:
            print("Please choose from the choices only.")
  
def playGame():    
    attempts = 1
    copy_words = words.copy()
    while True:
        random_word = random.choice(copy_words)
        random_display = list("_ " * len(random_word))
        print("===== Attempt", attempts, "=====")
        
        for i in random_display:
            print(i, end="")

        guess = input("Guess: ")

        if guess == random_word:
            print("So good, you got it in", attempts, "attempts")
            choice = input("Do you want to play again? (y/n): ")
            if choice == "y":
                copy_words.remove(random_word)
                attempts = 1
                continue
            else:
                break
        else: 
            for i in range(len(guess)):
                if guess[i] in random_word:
                    for j in range(len(random_word)):
                        if guess[i] == random_word[j]:
                            random_display[j] = guess[i]
                        else:
                            random_display[j] = "*"

        


def managePool():
     global words
     while True:
        print("===== Manage Word Pool =====")
        print()
        print("\t[1] Print Word Pool")
        print("\t[2] Insert new word")
        print("\t[3] Delete new word")
        print("\t[4] Reset word pool")
        print("\t[0] Exit")
        print()

        choice = int(input("Choice: "))
        if choice == 1:
            print("Words: ")
            for i in words:
                print("\t", i)
        elif choice == 2:
            new_word = toLower(input("Enter new word to insert: "))
            words.append(new_word)
            print(new_word,"inserted.")
        elif choice == 3:
            del_word = toLower(input("Enter word to delete: "))
            if len(words) == 0:
                print("Word pool is empty.")
            elif del_word in words:
                words.remove(del_word)
                print(del_word, "deleted.")
            else:
                print(del_word, "is not in the word pool.")
        elif choice == 4:
            words = []
            print("Word pool cleared.")
        elif choice == 0:
            print("Have fun!")
            break
        else:
            print("Please choose from the choices only.")

words = []

game()