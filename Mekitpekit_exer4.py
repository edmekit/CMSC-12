'''
Edmarc Justine B. Mekitpekit
Y-1L
Python program where you can play as a blacksmith where you have an initial gold and then you can buy materials and craft weapons then sell those weapons,and you can also check your current inventory
'''

#set globals
day = 1
sword = 0
spear = 0
axes = 0
iron = 0
wood = 0

# main func which contains the main menu 
def main():
    global day
    gold = 20
    # runs until user exits
    while True:
        print()
        print("========== Day", day, "==========")
        print("Blacksmith Ed, what do you want to do?")
        print()
        print("Current gold:", gold)
        print()
        print("[1] Buy Materials")
        print("[2] Craft")
        print("[3] Sell All weapons")
        print("[4] Check Inventory")
        print("[0] Exit")
        choice = int(input("Choice: "))

        # runs the respective function based on the choice input
        # every action will add 1 day except checking the inventory and exit
        if choice == 1:
            # calls the function then stores the value to gold
            gold = buy_mats(gold)
            day += 1
        elif choice == 2:
            craft_weapons()
            day += 1
        elif choice == 3:
            # a bit different, it adds the return value to the gold
            gold += sell_all_weapons(gold)
            day += 1
        elif choice == 4:
            check_inventory(gold)
        elif choice == 0:
            print("For Day", day, "you have", gold, "gold(s).")
            break
        else: 
            print("Not in choices. Please try again.")

# contains the menu for the materials store
def buy_mats(gold):
    global iron, wood, day
    # runs until user exits
    while True:
        print()
        print("========== MATERIALS STORE ==========")
        print("Blacksmith Ed, what materials do you want to buy?")
        print()

        # show the current materials and gold
        print("Current Gold:", gold)
        print("Current Iron:", iron)
        print("Current Wood:", wood)
        print()

        print("[1] Iron [2G]")
        print("[2] Wood [1G]")
        print("[0] Exit Store")
        choice = int(input("Choice: "))

        # calls the function based on the choice then stores into gold variable
        if choice == 1:
            gold = buyIron(gold)     
        elif choice == 2:
            gold = buyWood(gold)  
        elif choice == 0:
            # breaks out of the store loop and returns to the main menu
            print("Thank you so much for helping my poor family.")
            break
        else: 
            print("Not in choices. Please try again.")
    
    # returns the value of gold
    return gold

# function for buying irons
def buyIron(gold):
    global iron    
    num_bought = int(input("How many iron? "))
    price = 2
    total = price * num_bought
    # checks for insufficient gold
    if total > gold:
        print("You don't have enough gold.")
    else:
        print("Successfully bought", num_bought, "iron(s)")
        # adds to the outside variable iron and subtracts from gold
        iron += num_bought
        gold -= total

    return gold

# function for buying woods
def buyWood(gold):
    global wood
    num_bought = int(input("How many woods? "))
    price = 1
    total = price * num_bought
    # checks for insufficient gold
    if total > gold:
        print("You don't have enough gold.")
    else:
        print("Successfully bought", num_bought, "wood(s)")
        # adds to the outside variable wood and subtracts from gold
        wood += num_bought
        gold -= total

    return gold

# crafting menu
def craft_weapons():
    global day, wood, iron
    print()
    print("========== CRAFTING ==========")
    print("Blacksmith Ed, what do you want to craft?")
    print()

    print("Current Iron:", iron)
    print("Current Wood:", wood)
    print()

    # menu and the requirement for crafting
    print("[1] Sword [2 Iron, 1 Wood]")
    print("[2] Spear [1 Iron, 2 Wood]")
    print("[3] Axe [3 Iron, 2 Wood]")
    choice = int(input("Choice: "))

    # calls the function based on the choice
    if choice == 1:
        craftSword()
    elif choice == 2:
        craftSpear()
    elif choice == 3:
        craftAxe()
    else: 
        print("Not in choices. Please try again.")

# function for crafting sword
def craftSword():
    global iron, wood, sword
    num_craft = 0
    # as long as materials are enough for a sword, it will craft
    while iron > 1 and wood > 0: 
        iron -= 2
        wood -= 1
        num_craft += 1
    sword += num_craft
    print("Successfully crafted", num_craft, "sword(s)")

# function for crafting spear
def craftSpear():
    global iron, wood, spear
    num_craft = 0
    # as long as materials are enough for a spear, it will craft
    while iron > 0 and wood > 1: 
        iron -= 1
        wood -= 2
        num_craft += 1
    spear += num_craft
    print("Successfully crafted", num_craft, "spear(s)")

# function for crafting axe
def craftAxe():
    global iron, wood, axes
    num_craft = 0
    # as long as materials are enough for an axe, it will craft
    while iron > 2 and wood > 1: 
        iron -= 3
        wood -= 2
        num_craft += 1
    axes += num_craft
    print("Successfully crafted", num_craft, "axe(s)")

# seel all menu 
def sell_all_weapons(gold):
    global sword, spear, axes
    print()
    print("========== Sell All ==========")
    print("Blacksmith Ed, do you want to sell all weapons?")
    print()

    print("Current gold:", gold)
    print()

    print("Sowrds:", sword, "[9G each]")
    print("Spears:", spear, "8G each")
    print("Axes:", axes, "[15G each]")
    print()
    # computes the total profit
    total = (sword * 9) + (spear * 8) + (axes * 15)
    print("Total profit:", total)


    choice = input("Sell all? [y/n] ")
    if choice == "y":
        print("Total profit received:", total)
    elif choice == "n": 
        print("No weapons sold today")
        total = 0
    
    return total

def check_inventory(gold):
    print()
    print("========== INVENTORY ==========")
    print("Blacksmith Ed, here are the current materials and weapons.")
    print()

    print("Current Gold (G):", gold)
    print()

    print("Iron:", iron)
    print("Wood:", wood)
    print("Sword:", sword)
    print("Spear:", spear)
    print("Axe:", axes)

main()