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
        print("\t4. Back")

        choice = int(input("Choice: "))
        if choice == 1:
            addProject(projectdic, logbookdic)
        elif choice == 2:
            deleteAllProject(projectdic, logbookdic)
        elif choice == 3:
            deleteProject(projectdic, logbookdic)
        elif choice == 4:
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
    print("Choose services for", proj_type, "project: ")
    
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
        "project_status": proj_status,
        "services" : services
    }

    logbook.addLogEntry("add_project", proj_id, "NA", "NA", logbookdic)

    return projectdic

def deleteProject(projectdic, logbookdic):
    while True:
        project_id = input("Enter Project ID you want to delete: ")

        if project_id in projectdic:
            del projectdic[project_id]
            for key in logbookdic:
                if logbookdic[key]["project_id"] == project_id:
                    del logbookdic[key]
            print("Project has been deleted.")
            break
                
        else:
            print("Project ID does not exist.")

def deleteAllProject(projectdic, logbookdic):
    for key in logbookdic:
        if logbookdic[key]["project_id"] != "NA": #mali
            del logbookdic[key]
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
            print("\tType:", k, "Supplier:", v)
