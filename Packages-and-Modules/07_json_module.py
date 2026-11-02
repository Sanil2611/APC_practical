import json

student = {"name": "Asha", "marks": 88, "course": "CSE"}
json_text = json.dumps(student, indent=2)
print("JSON data:")
print(json_text)

loaded = json.loads(json_text)
print("Student name:", loaded["name"])
