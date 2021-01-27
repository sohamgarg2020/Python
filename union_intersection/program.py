first_set = []
second_set = []
union = []
intersection = []

while True:
    x = input("Enter a number or Q to exit to add in your first set: ")
    if str(x).lower() == "q":
        break
    else:
        try:
            x = int(x)
            first_set.append(int(x))
            print(f"{int(x)} has been added to the first list.")
            continue
        except:
            print("Please enter an integer, or Q to exit.")
            continue

print(f"This is your first set: {first_set}")

while True:
    x = input("Enter a number or Q to exit to add in your second set: ")
    if str(x).lower() == "q":
        break
    else:
        try:
            x = int(x)
            second_set.append(int(x))
            print(f"{int(x)} has been added to the first second.")
            continue
        except:
            print("Please enter an integer, or Q to exit.")
            continue

print(f"This is your second set: {second_set}")

f_list = []
s_list = []

for i in first_set:
    if i in f_list:
        f_list = f_list
    else:
        f_list.append(i)

for i in second_set:
    if i in s_list:
        f_list = f_list
    else:
        s_list.append(i)

def intersect():
    for i in f_list:
        if i in s_list:
            f_list.remove(i)
            s_list.remove(i)
            intersection.append(i)
    return intersection

def union():
    union = intersection + f_list + s_list
    return union

print(f"Here is the intersection of the two sets: {intersect()}")
print(f"Here is the union of the two sets: {union()}")





