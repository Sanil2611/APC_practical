import re

text = "Contact us at support@example.com"
email = re.search(r"[\w.-]+@[\w.-]+\.\w+", text)

print("Email found:", email.group() if email else "No email found")
