inventory = ["apple", "banana", "orange", "apple", "mango", "banana"]
applecount = 0
for i in inventory:
    if i == "apple":
        applecount += 1
print(applecount)
inventory.append("grapes")
print(inventory)