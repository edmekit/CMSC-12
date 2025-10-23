import arts, logbook
types = ["Construction", "Renovation", "Demolition"]
statuses = ["Prep", "Ongoing", "Finished"]
construction = ['Permits','Design','Masonry','Carpentry','WindowWork','MetalWork','Furniture','ElectricalWork','Plumbing','PaintWork','SiteClearing','Earthwork']
renovation = ['Permits','Masonry','Carpentry','WindowWork',
'MetalWork','ElectricalWork','PaintWork']
demolition = ['Permits','SiteClearing','Earthwork']

def menu(projectdic,supplierdic, logbookdic):
    while True:
        print(arts.logo)
        print("\tProject Section")
        print("\t1. Add Project")
        print("\t2. Delete All Projects")
        print("\t3. Delete Project")
        print("\t4. View Project")
        print("\t0. Exit")
        print()

        choice = int(input("Choice: "))
        if choice == 1:
            addProject(projectdic, logbookdic)
        elif choice == 2:
            deleteAllProject(projectdic, logbookdic)
        elif choice == 3:
            deleteProject(projectdic, logbookdic)
        elif choice == 4:
            viewProject(projectdic)
        elif choice == 0:
            break
def addProject(projectdic, logbookdic):
    print(arts.logo)
    proj_id = "P" + str(len(projectdic) + 1)
    while True:
        proj_type = input("Enter project type: ")
        if proj_type in types:
            break
        else:
            print("Type can only be Construction, Renovation, or Demolition.")

    while True:
        proj_status = input("Enter project status: ")
        if proj_status in statuses:
            break
        else:
            print("Status can only be Prep, Ongoing, or Finished.")
    
    services = {}

    if proj_type == "Construction":
        for i in range(0, len(construction)):
            services[construction[i]] = ""
    elif proj_type == "Renovation":
        for i in range(0, len(renovation)):
            services[renovation[i]] = ""
    elif proj_type == "Demolition":
        for i in range(0, len(demolition)):
            services[demolition[i]] = ""
    

    projectdic[proj_id] = {
        "project_type": proj_type,
        "description": "",
        "project_status": proj_status,
        "services" : services
    }

    logbook.addLogEntry("add_project", proj_id, "NA", "NA", logbookdic)

def deleteProject(projectdic, logbookdic):
    project_id = input("Enter Project ID you want to delete: ")

    if project_id in projectdic:
        del projectdic[project_id]
        project_delete = []
        for key in logbookdic:
            if logbookdic[key]["project_id"] == project_id:
                project_delete.append(key)
        for i in project_delete:
            del logbookdic[i]
        print("Project has been deleted.")
    else:
        print("Project ID does not exist. View projects info.")

def deleteAllProject(projectdic, logbookdic):
    projects_delete = []
    for key in logbookdic:
        if logbookdic[key]["project_id"] != "NA": # check if log entry has a project ID
            projects_delete.append(key)

    for i in projects_delete:
        del logbookdic[i]

    projectdic.clear()    
    print("All projects have been deleted.")

def viewProject(projectdic):
    proj_id = input("Enter Project ID you want to view: ")

    if proj_id in projectdic:
        print("\t Project ID:", proj_id)
        print("\t Project Type:", projectdic[proj_id]["project_type"])
        print("\t Project Status:", projectdic[proj_id]["project_status"])
        print("\t Services: ")
        for k,v in projectdic[proj_id]["services"].items():
            print(f"\t\tType: {k}, Supplier: {v}")
    else: 
        print("Project ID does not exist.")
    
def viewAllprojects(projectdic):
    for key in projectdic:
        print("\t Project ID:", key)
        print("\t Project Type:", projectdic[key]["project_type"])
        print("\t Project Status:", projectdic[key]["project_status"])
        print("\t Services: ")
        for k,v in projectdic[key]["services"].items():
            print(f"\t\tType: {k}, Supplier: {v}")

def updateStatus(projectdic):
    proj_ID = input("Enter Project ID: ")
    if proj_ID in projectdic:
        while True:
            proj_status = input("Enter project status: ")
            if proj_status in statuses:
                break
            else:
                print("Status can only be Prep, Ongoing, or Finished.")
        projectdic[proj_ID]["project_status"] = proj_status
    else:
        print("Project ID does not exist. Check projects info.")

def changeSupplier(projectdic, supplierdic, blacklisted):
    proj_id = input("Enter Project ID you want to change supplier: ")

    if proj_id in projectdic:
        if projectdic["project_status"] != "Finished":
            service = input("Enter which service you want to change supplier: ")
            if service in projectdic[proj_id]["services"]:
                print("Here are the suppliers that can provide",service ,"service: ")
            else:
                print("Service does not exist. Check project info.")

            for key in supplierdic: # loop the supplier dictionary and look for suppliers that can provide the service
                if service in supplierdic[key]["services_provided"]:
                    print("\t", supplierdic[key]["supplier_name"])
            while True:
                change_supplier = input("Choose which supplier to change service to: ")
                if change_supplier in blacklisted:
                    print("Supplier is blacklisted. Please choose another supplier.")
                else:
                    projectdic[proj_id]["services"][service] = change_supplier
                    break
        else:
            print("Project is finished. Cannot change supplier.")
    else:
        print("Project ID does not exist. Check projects info.")
                


