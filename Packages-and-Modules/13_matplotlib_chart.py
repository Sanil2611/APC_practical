import matplotlib.pyplot as plt

subjects = ["Python", "DBMS", "OS", "CN"]
marks = [88, 76, 82, 91]

plt.bar(subjects, marks)
plt.title("Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()
