import arts, logbook
types = ["Construction", "Renovation", "Demolition"]
statuses = ["Prep", "Ongoing", "Finished"]
construction = ['Permits','Design','Masonry','Carpentry','WindowWork','MetalWork','Furniture','ElectricalWork','Plumbing','PaintWork','SiteClearing','Earthwork']
renovation = ['Permits','Masonry','Carpentry','WindowWork',
'MetalWork','ElectricalWork','PaintWork']
demolition = ['Permits','SiteClearing','Earthwork']

def addProject(projectdic):
    print(arts.logo)
    proj_id = len(projectdic) + 1
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

    logbook.AddProject()

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

def deleteAllProject():