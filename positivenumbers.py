print("¿Which numbers are positive and wich numbers are not positive?")
locations = [(1, 2), (4, 0), (-2, 5), (3, 3)]
print(locations)
print()
number = 0
numberneg = 0
for one, two in locations:
    if one >= 0:
        print(one, "is positive")
        number = number + one
        if two >= 0:
            print(two, "is also positive")
            print("Both numbers are positive")
            print("Next!")
            print()
    else:
        print(one, "isn't positive")
        numberneg = numberneg + 1
        print("Let's check the next one!")
        print()


print("The total amount of positive numbers are: ", number)
print("And the total amount of negative numbers are: ", numberneg)
