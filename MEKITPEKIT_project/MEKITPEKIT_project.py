import arts, plants, logbook, supplier
logbookdic = {}
projectdic = {}
supplierdic = {}
blacklisted = []
print(arts.logo)

while True:
	print("Welcone!")
	print("What would you like to do?")
	print()
	
	print("\t[1] Project Section")
	print("\t[2] Supplier Section")
	print("\t[3] Logbook Section")
	print("\t[0] Exit")
	print()

	choice = int(input("Choice: "))
	print()
	
	if choice == 1:
		plants.menu(projectdic,supplierdic,logbookdic, blacklisted)
	elif choice == 2:
		supplier.menu()
	elif choice == 3:
		logbook.menu()
	elif choice == 0:
		print("Goodbye!")
		break
    
        