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
    
    if proj_type == "Construction":
        services = construction
    elif proj_type == "Renovation":
        services = renovation
    elif proj_type == "Demolition":
        services = demolition
    

    projectdic[proj_id] = {
        "project_id": proj_id,
        "project_type": proj_type,
        "project_status": proj_status,
        "services" : services
    }

    logbook.AddProject()

    return projectdic

