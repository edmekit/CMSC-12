'''
Edmarc Justine B. Mekitpekit
Y-1L
Python program where you can manage a terminal library, you can add books, view all books, change book status, add note to book, remove book, clear book catalogue.
'''

def menu():
	lib = {}
	while True:
		print()
		print("======== MENU =======")
		print("[1] Add a Book")
		print("[2] View All Books")
		print("[3] Change Book Status")
		print("[4] Add Note to Book")
		print("[5] Remove Book")
		print("[6] Clear Book Catalogue")
		print("[0] Exit")
		print("=====================")
		print()

		choice = int(input("Choice: "))
		print()

		if choice == 1:
			lib = addBook(lib)
		elif choice == 2:
			viewCatalogue(lib)
		elif choice == 3:
			lib = changeStatus(lib)
		elif choice == 4:
			lib = addNote(lib)
		elif choice == 5:
			lib = removeBook(lib)
		elif choice == 6:
			lib = clearLibrary(lib)
		elif choice == 0:
			print("Have a great day hihi!")
			break
		else:
			print("PLease choose from 0-6") # input check

def addBook(lib):
	print("========== ADD A BOOK ==========")
	statuses = ["to-read", "currently-reading", "finished"]
	while True:
		book_code = input("Book code: ") 
		if book_code in lib: # check if book code already exist
			print("Book code already exist.")
			continue
		break
	book_name = input("Book name: ")
	author = input("Author: ")
	price = float(input("Price: "))
	date_bought = input("Date bought: ")
	while True: 
		status = input("Status: ")
		if status in statuses: # check if input status is valid
			break
		else:
			print("Please choose from to-read, currently-reading, finished.")
	print("Book added hihi.")
	print("==========================")

	lib[book_code] = [  # add new key to the dictionary
		book_name,
		author,
		price,
		date_bought,
		status,
		[]
	] 
	return lib


def viewCatalogue(lib):
	print("========== MY LIBRARY ==========")
	if len(lib) == 0: 
		print("No books in library. Add some.")
	for i in lib: # loop through the keys getting the respective values
		print(i)
		print("Book name:", lib[i][0])
		print("Author:", lib[i][1])
		print("Price:", lib[i][2])
		print("Date bought:", lib[i][3])
		print("Status:", lib[i][4])
		print("My notes: ")
		if len(lib[i][5]) == 0: # check if the list for notes is empty
			print("\tNo notes yet.")
		else: 
			for note in lib[i][5]:
				print("\t >", note)
		print()
	print("===============================")

def changeStatus(lib):
	statuses = ["to-read", "currently-reading", "finished"]
	print("======== CHANGE STATUS ========")
	book_code = input("Choose which book to change status: ")
	if book_code in lib:
		print("New status of", lib[book_code][0], end="")
		new_stat = input(" is: ")
		while True:
			if new_stat in statuses: # check if input status is valid
				lib[book_code][4] = new_stat
				print("Status changed.")
				print("===============================")
				return lib
			else:  # if not valid
				print("Status can only be to-read, currently-reading, finished. PLease try again")
				new_stat = input("New status: ")
	else:
		print("Book code not existing yet.")
		print("===============================")
		return lib

def addNote(lib):
	print("======== ADD A NOTE ========")
	book_code = input("Enter a Book to add a note to: ")
	if book_code in lib: # check if book code exist
		print("Add note to", lib[book_code][0], end=" ")
		new_note = input(": ")
		lib[book_code][5].append(new_note) # add to the list for notes
		print("Note added hihi.")
		print("===============================")
		return lib
	else: 
		print("Book not existing.")
		print("===============================")
		return lib

def removeBook(lib):
	print("========= REMOVE BOOK =======")
	book_code = input("Select which book to remove: ")
	if book_code in lib:	
		print("Deleted", lib[book_code][0], "by", lib[book_code][1])
		del lib[book_code] # delete the key in dictionary
		print("===============================")
		return lib
	else:
		print("Book not existing.")
		print("===============================")
		return lib

def clearLibrary(lib):
	lib = {} # clear the dictionary
	print("Library is now empty..")
	return lib

menu()
