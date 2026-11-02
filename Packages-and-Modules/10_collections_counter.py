from collections import Counter

votes = ["Python", "Java", "Python", "C++", "Python", "Java"]
counts = Counter(votes)

print("Vote counts:", counts)
print("Most popular:", counts.most_common(1))
