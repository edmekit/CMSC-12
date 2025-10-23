import arts, logbook

def menu():
    while True:
        print(arts.logo)
        print("\tSupplier Section")
        print("\t1. Add Supplier")
        print("\t2. View Supplier")
        print("\t3. View All Suppliers")
        print("\t0. Exit")
        print()

        choice = int(input("Choice: "))
        if choice == 1:
            addSupplier(supplierdic)
        elif choice == 2:
            addProjectTypes()
        elif choice == 3:
            removeProjectTypes()
        elif choice == 4:
            addServiceProvided()
        elif choice == 5:
            removeServiceProvided()
        elif choice == 6:
            viewSupplier()
        elif choice == 7:
            viewAllSuppliers()
        elif choice == 0:
            print("Goodbye!")
            break

def addSupplier(supplierdic):
    supp_id = "S" + str(len(supplierdic) + 1)
    supp_name = input("Enter supplier name: ")

    for key in supplierdic: #loop the dic and check if supplier already exists
        if supplierdic[key]["supplier_name"] == supp_name:
            print("Supplier already exists. Update supplier info instead.")
            return
    
    service_types = []
    while True:
        service_type = input(f"Enter service provided by {supp_name}: ").capitalize()
        if service_type in service_types: # avoid duplicates
            print("Supplier already provides this service.")
            continue
        elif service_type in logbook.types:
            service_types.append(service_type)
            choice = input("Do you want to add another service? (y/n): ")
            if choice == "n":
                break
        else:
            print("Type can only be Construction, Renovation, or Demolition.")

    services_provided = []

    while True:
        services_provided = input(f"Enter service provided by {supp_name}: ").capitalize()
        if services_provided in service_types: # avoid duplicates
            print("Supplier already provides this service.")
            continue
        elif services_provided in logbook.construction:
            service_types.append(services_provided)
            choice = input("Do you want to add another service? (y/n): ")
            if choice == "n":
                break
        else:
            print("Service provided can only be  Permits, Design, Masonry, Carpentry, WindowWork, MetalWork, Furniture, ElectricalWork, Plumbing, PaintWork, SiteClearing, Earthwork.")

    supplierdic[supp_id] = {
        "supplier_name": supp_name, 
        "services_types": service_types, "services_provided": services_provided
    }

    print("Supplier added successfully.")

           
        