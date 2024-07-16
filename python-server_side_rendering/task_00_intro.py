import os

def generate_invitations(template, attendees):
    
    if not isinstance(template, str):
        print("Invalid input type for template")
    
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Invalid input type for attendees")
        return
    
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees, start=1):

        personal_invitation = template
        
        personal_invitation = personal_invitation.replace("{ name }", attendee.get("name", "N/A"))
        personal_invitation = personal_invitation.replace("{ event_title }", attendee.get("event_title", "N/A"))
        personal_invitation = personal_invitation.replace("{ event_date }", attendee.get("event_date", "N/A"))
        personal_invitation = personal_invitation.replace("{ event_location }", attendee.get("event_location", "N/A"))
        
        filename = "output_{}.txt".format(index)

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(personal_invitation)
