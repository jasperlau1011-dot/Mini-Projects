print("The Current List of Spendings are Shown Bellow:")
count = True
spendings = {}
print("\tThere is nothing currently in list")
while count:
    question = input("\nwould you like to add? Enter in its congruent form etc: 'yes' or 'no'")
    if question == "yes":
        in_list = input("\nenter your purchased item and price, sepperated by a space and comma in between, etc: sugar 12, flour 20")
        list_split = in_list.split(", ")
        for lists in list_split:
            item = lists.split(" ")[0]
            values = lists.split(" ")[1]
            spendings[item] = values
        print("Here is the currently updated list of items:")
        for key, value in spendings.items():
            print(f"\t- {key} : ${value}")
    elif question == "no":
        count = False
print("\nHere is the final list of purchased items:")
for key, value in spendings.items():
            print(f"\t- {key} : ${value}")