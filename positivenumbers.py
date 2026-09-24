print("¿Which numbers are positive and wich numbers are not positive?")
locations = [(1, 2), (4, 0), (-2, 5), (3, 3)]
print(locations)
print()

for one, two in locations:
    if one >= 0:
        print(one, "is positive")
        if two >= 0:
            print(two, "is also positive")
            print("Both numbers are positive")
            print("Next!")
            print()
    else:
        print(one, "isn't positive")
        print("Let's check the next one!")
        print()