import arts

actions = ["add_project", "update_status", "change_supplier", "change_type", "add_supplier", "add_project_type", "remove_project_type", "add_service_provided", "remove_service_provided"]


def addLogEntry(action, projID, suppID, remark, logbookdic):
    while action not in actions:
        print("Invalid action. Please try again.")
        action = input("Action: ")
    
    log_id = len(logbookdic) + 1
    logbookdic[log_id] = {
        "action": action,
        "project_id": projID,
        "supplier_id": suppID,
        "remark": remark
    }


    
        
            
    

