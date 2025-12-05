# Festival Inventory Disaster – Real‑World Python Collections Challenge
# Scenario
# You are hired as the Data Assistant for the Chicago Fall Music & Food Festival.
# The festival opens in 3 hours, but the digital system has scrambled the inventory lists, vendor data, and safety rules. Your job is to fix the data using Python lists, sets, and tuples.
# If you fail, the festival cannot legally open.

# Starting Data
    # foods = ["pizza", "tacos", "bbq", "tacos", "sushi", "corn", "bbq", "ice cream"]
    # stages = ("Main Stage", "Hip-Hop Zone", "Jazz Corner", "Indie Alley")
    # restricted = {"glass bottles", "weapons", "alcohol", "alcohol"}
    # attendance = [120, 130, 125, 145, 150, 148, 155, 160, 158, 162]

# Task 1 — Clean the Food Vendor List
    # 1. Remove duplicates while keeping only the first occurrence.
    # 2. Add "ramen" and "fried rice".
    # 3. Insert "smoothies" at index 2.
    # 4. Sort the list alphabetically.
    # 5. Print the final vendor list.

foods = ["pizza", "tacos", "bbq", "tacos", "sushi", "corn", "bbq", "ice cream"]
foods = list(dict.fromkeys(foods))
foods.extend(["ramen", "fried rice"])
foods.insert(2, "smoothies")
foods.sort()
print(foods)


#Task 1.5 
    # combine all the list into a nested list called festival_data
    #print out the new nested list(use a for loop to print each item on a new line)

festival_data = ["foods", "stages", "restricted", "attendance"]
for i in range(4):
    print(festival_data)


# Task 2 — Stage Map
    # 1. Print the second stage.
    # 2. Print the last two stages.
    # 3. Convert the tuple into a list and add "Rock Arena".
    # 4. Convert it back into a tuple.
    # 5. Print the updated tuple.

stages = ["Main Stage", "Hip-Hop Zone", "Jazz Corner", "Indie Alley"]
print(stages[1])
print(stages[-1], "and", stages[-2])
stages = list(stages)
stages.append("Rock Arena")
stages = tuple(stages)
print(stages)


# Task 3 — Restricted Items
    # 1. Add "fireworks".
    # 2. Try adding "weapons" again.
    # 3. Remove "alcohol".
    # 4. Check if "glass bottles" is still restricted.
    # 5. Print the final restricted set.

restricted = ["glass bottles" "weapons", "alcohol", "alcohol"]
restricted.append("fireworks")
restricted.append("weapons")
restricted.remove("alcohol")
print("glass bottles" in restricted)
print(restricted)


# Task 4 — Attendance Analysis
    # 1. Print the first three hours.
    # 2. Print the last hour.
    # 3. Print every 2nd hour.
    # 4. Remove the 5th hour using pop().
    # 5. Add five projected values using extend(range(...)).
    # 6. Delete every 3rd value using del attendance[::3].
    # 7. Print the length and cleaned list.

attendance = ["120", "130", "125", "145", "150", "148", "155", "160", "158", "162"]
print(attendance[0], " ", attendance[1], "and", attendance[2])
print(attendance[-1])
print(attendance[::2])
attendance.pop(4)
attendance.extend(i+100 for i in range(5))
del attendance [::3]
print(attendance)


# Task 5 — Festival Master List
    # 1. Convert vendors, restricted set, and stages into lists.
    # 2. Combine everything into festival_data.
    # 3. Print: total items, first 10, last 10.
    # 4. Remove duplicates.
    # 5. Print final cleaned festival_data.

stages = list(stages)
restricted = list(restricted)
attendance = list(attendance)
foods = list(foods)
festival_data = [foods, restricted, stages, attendance]
print(len(festival_data), "items")
print(festival_data[0] [0:], festival_data[1] [0:1])
print(festival_data[-2] [-1:], festival_data[-1] [:-1], festival_data[-1] [-1:])
festival_data[0] = list(dict.fromkeys(foods))
festival_data = list(dict.fromkeys(stages))
festival_data = list(dict.fromkeys(attendance))
festival_data = list(dict.fromkeys(restricted))
print(festival_data)

# Extension
# Write a function festival_search(item) that returns True/False if item appears in festival_data.

n = int(input("How many items are you looking for?: "))
for _ in range(n):
    search_list = input("What list are you looking for?: ")
    search_item = input("What items are you looking for?: ")
    if search_item in search_list:
        print("True")
    else:
        print("False")
