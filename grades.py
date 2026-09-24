grades = {"Alice": 88, "Bob": 65, "Charlie": 92, "Diana": 45}


grades["Ethan"] = 80
grades["Bob"] = 70

for name, grade in grades.items():
    if grade >= 70:
        print(name, "has passed! Excellent!")
    else:
        failed = 70 - grade
        print(name, "didn't pass by", failed, "points")