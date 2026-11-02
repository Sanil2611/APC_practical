"""Application settings and demo accounts."""
STATUSES = ("Submitted", "In Progress", "Resolved")
CATEGORIES = ("Facilities", "Hostel", "Cafeteria", "IT / Wi-Fi", "Safety", "Other",)
INK = "#33243b"
PLUM = "#55345f"
CORAL = "#e8795b"
PAPER = "#fbf4e9"
MUTED = "#817484"
#this are used to add colours to our application
#Next, INK, PLUM, CORAL, PAPER and MUTED are colour variables used to maintain the application's colour theme.

# Demo accounts for a classroom project. Change these before real use.
DEMO_USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "student": {"password": "student123", "role": "student"},
}
#this code is used to create the demo admin and student account to our system
