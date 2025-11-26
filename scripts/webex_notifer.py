# scripts/webex_notifier.py
import sys
import os
from webexteamssdk import WebexTeamsAPI
from datetime import datetime

def send_notification(action, first_name, last_name, email, department=None):
    # Initialize Webex API
    token = os.getenv('WEBEX_BOT_TOKEN')
    room_id = os.getenv('WEBEX_ROOM_ID')
    
    if not token or not room_id:
        print("[ERROR] Webex credentials not found!")
        sys.exit(1)
        
    api = WebexTeamsAPI(access_token=token)
    
    # Create msg based on action
    if action == "onboard":
        msg = f"""
        [SUCCESS] New Employee Onboarded!
        **Name:** {first_name} {last_name}
        **Email:** {email}
        **Department:** {department}
        **Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        - LDAP account created
        - Groups assigned
        - Home directory created
        - Welcome email generated
        """
    else: #offboard
        msg: f"""
        [SUCCESS] Employee Offboarded!
        **Name:** {first_name} {last_name}
        **Email:** {email}
        **Department:** {department}
        **Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        - Account disbaled
        - Groups removed
        - Data archived
        """
    # Send msg
    try:
        api.messages.create(roomId=room_id, markdown=msg)
        print(f"Webex notification sent successfully for {action}")
    except Exception as e:
        print(f"[ERROR] Sending Webex notification: {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: webex_notifier.py <action> <first_name> <last_name> <email> [department]")
        sys.exit(1)
        
    action = sys.argv[1]
    first_name = sys.argv[2]
    last_name = sys.argv[3]
    email = sys.argv[4]
    department = sys.argv[5] if len(sys.argv) > 5 else None
    
    send_notification(action, first_name, last_name, email, department)
        