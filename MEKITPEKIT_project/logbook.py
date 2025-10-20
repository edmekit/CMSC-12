import arts

actions = ["add_project", "update_status", "change_supplier", "change_type", "add_supplier", "add_project_type", "remove_project_type", "add_service_provided", "remove_service_provided"]

def AddProject(logbookdic, projectdic):
    log_id = "L" + len(logbookdic)
    action = "add_project"
    project_id = input("Enter Project ID: ")

