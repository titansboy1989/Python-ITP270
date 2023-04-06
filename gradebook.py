#!/usr/bin/python3

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = []
for i in range(len(subjects)):
  gradebook.append([subjects[i], grades[i]])
print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

gradebook[5][1] += 5

poetry_grade = grades[2]

gradebook.remove(["poetry", poetry_grade])
gradebook.append(["poetry", "Pass"])

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
