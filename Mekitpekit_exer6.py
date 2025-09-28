'''
Edmarc Justine B. Mekitpekit
Y-1L
'''

books = [{
    'name': "Sherlock Holmes",
    'author': "Arthur Conan Doyle",
    'status': "Read",
    'start_date': '2025-09-28',
    'end_date': '---------',
    'notes': "---------"
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
            break
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
        print("Start Date:", books[i]['start_date'])
        print("End Date:", books[i]['end_date'])
        print("Notes:", books[i]['notes'])
        print()

def addBook():
    print()
    print("===== Add New Book =====")
    print()

    name = input("Name: ")
    author = input("Author: ")
    status = input("Status: ")
    start_date = input("Start Date: ")
    end_date = input("End Date: ")
    notes = input("Notes: ")

    books.append({
        'name': name,
        'author': author,
        'status': status,
        'start_date': start_date,
        'end_date': end_date,
        'notes': notes
    })

    print()
    print("Book added successfully!")
    print()

def addNotes():
    print()
    print("===== Add Notes =====")
    print()

    book = int(input("Which book to add notes: ")) - 1
    print("Book", book + 1)
    print("Name:", books[book]['name'])
    print("Author:", books[book]['author'])
    print("Status:", books[book]['status'])
    print("Start Date:", books[book]['start_date'])
    print("End Date:", books[book]['end_date'])
    print("Notes:", books[book]['notes'])

    notes = input("Notes: ")

    books[book]['notes'] = notes

    print()
    print("Notes added successfully!")
    print()

def editStatus():
    print()
    print("===== Edit Status =====")
    print()

    book = int(input("Which book to edit status: ")) - 1
    print("Book", book + 1)
    print("Name:", books[book]['name'])
    print("Author:", books[book]['author'])
    print("Status:", books[book]['status'])
    print("Start Date:", books[book]['start_date'])
    print("End Date:", books[book]['end_date'])
    print("Notes:", books[book]['notes'])
    print()

    status = input("Status: ")
    date_end = input("End Date: ")

    books[book]['status'] = status
    books[book]['end_date'] = date_end

    print()
    print("Status edited successfully!")
    print()
    
main()