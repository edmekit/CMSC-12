def saveCatalogue(lib):
    print("======= SAVING BOOKS TO books.dat ======= ")

    if len(lib) == 0:
        print("No books in library. Add some.")
        return lib
    save_file = open("books.dat", "w")

    # loop through the dictionary and write the respective infos to the file
    for i in lib:
        print("Added " + i + " (" + lib[i][0] + ") to books.dat"    )
        save_file.write(i + "|")
        save_file.write(lib[i][0] + "|")
        save_file.write(lib[i][1] + "|")
        save_file.write(str(lib[i][2]) + "|")
        save_file.write(lib[i][3] + "|")
        save_file.write(lib[i][4] + "|\n")
        if len(lib[i][5]) == 0:
            save_file.write("\n")
        else:
            for note in lib[i][5]:
                save_file.write(note + "|")
            save_file.write("\n")
    print("=======================================")
    save_file.close()

def loadCatalogue(lib):
    print("====== LOADING BOOKS FROM books.dat =====")

    load_file = open("books.dat", "r")
    print("Loaded book catalogue containing:")

    file_lines = load_file.readlines()

    counter = 0

    while counter < len(file_lines):
        # check if the notes line exist
        if counter + 1 <= len(file_lines):
            if file_lines[counter + 1] == "\n":
                notes = []
            else:
                # remove \n and pop the empty string
                notes = file_lines[counter + 1][:-1].split("|")
                notes.pop()
        else:
            notes = []
        attrs = file_lines[counter].split("|")
        print("Added " + attrs[0] + " (" + attrs[1] + " by " + attrs[2] + ")")

        # add the infos to the dictionary
        lib[attrs[0]] = [
        attrs[1],
        attrs[2],
        attrs[3],
        attrs[4],
        attrs[5],
        notes
        ]
        counter += 2
    print("===============================")
    load_file.close()

    return lib