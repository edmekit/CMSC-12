'''
Edmarc Justine B. Mekitpekit
Y-1L
'''

books = [{
    'name': "Sherlock Holmes",
    'author': "Arthur Conan Doyle",
    'status': "Read"
}]

def main ():
    while True:
        print()
        print("===== Welcome to Edmarc's Archive =====")
        print()

        print("\t[1] Show all books")
        print("\t[2] Add new book")
        print("\t[3] Edit Status")
        print("\t[4] Add Notes")
        print("\t[0] Exit")
        print()

        choice = int(input("Choice: "))

        if choice == 1:
            showAll()
        elif choice == 2:
            addBook()
        elif choice == 3:
            editStatus()
        elif choice == 4:
            addNotes()
        elif choice == 0:
            print("Goodbye!")
        else:
            print("Please choose from the choices only.")

def showAll():
    print()
    print("===== All Books =====")
    print()

    for i in range(len(books)):
        print("Book", i + 1)
        print("Name:", books[i]['name'])
        print("Author:", books[i]['author'])
        print("Status:", books[i]['status'])
        print()

def addBook():
    print()
    print("===== Add New Book =====")
    print()

    name = input("Name: ")
    author = input("Author: ")
    status = input("Status: ")

    books.append({
        'name': name,
        'author': author,
        'status': status,
    })

    print()
    print("Book added successfully!")
    print()

def addNotes():
    print()
    print("===== Add Notes =====")
    print()

    book = int(input("Which book to add notes: "))
    print("Book", book)
    print("Name:", books[book - 1]['name'])
    print("Author:", books[book - 1]['author'])
    print("Status:", books[book - 1]['status'])
    print()

    notes = input("Notes: ")

    books[book - 1]['notes'] = notes

    print()
    print("Notes added successfully!")
    print()
    
main()