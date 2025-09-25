





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

#main menu
def game():    
    while True:
        print()
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
            print("I hope you had fun!")
            break
        else:
            print("Please choose from the choices only.")
  
#wordle game
def playGame():  
    copy_words = words.copy()
    if len(copy_words) == 0:
        print("Word pool is empty. Add words to play the game.")
        return
    while True:  
        attempts = 1
        random_word = random.choice(copy_words)
        random_display = list("_" * len(random_word)) # generates a list with of "_" with length of random word
        while True:
            print()
            print("===== Attempt", attempts, "=====")
            print("\t", end="")
            for i in random_display:
                print(i, end=" ") #displays the "_"
            
            print()

            guess = toLower(input("Guess: ")) # get guess
            if guess == random_word: # check if guess is correct 
                print("============================")
                print("\t", guess)
                print("So good, you got it in", attempts, "attempt(s)")
                choice = input("Do you want to play again? (y/n): ")
                if choice == "y":
                    copy_words.remove(random_word)
                    if len(copy_words) == 0:
                        print("No words left in the word pool. Play again latur.")
                        return # returns to the main menu
                    break # breaks out of the inner while loop and starts a new game
                else:
                    return 
            else: 
                for i in range(len(random_display)): 
                    if guess[i] in random_word: # check if the letter in guess is in the random word
                        if guess[i] == random_word[i]: # check if the letter is in the right index
                            random_display[i] = guess[i] # replace the "_" in the right index with the correct letter
                        else:
                            random_display[i] = "*" # if the letter is in the wrong index, replace "_" with "*"
                    else:
                        random_display[i] = "-" # if the letter is not in the random word at all

            attempts += 1


def managePool():
     global words
     while True:
        print()
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
                print("\t", i) # loop and print each in the list
        
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
            print("Have fun playing!")
            break
        
        else:
            print("Please choose from the choices only.")

words = ['keep', 'feel', 'reel', 'reap', 'flow']

game()