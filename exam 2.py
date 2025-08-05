def Data():
    print("=====Welcome to Inventory List Analyzer!=====\n")
    items = []

    while True:
        item_name = input("Enter item name: ").strip()
        item_category = input("Enter category: ").strip().lower()
        quantity = int(input("Enter quantity: "))

        items.append({
            'name': item_name,
            'category': item_category,
            'quantity': quantity
        })

        cont = input("\nDo you want to add more items? (y/n): ").lower()
        if cont != 'y':
            break

    print("\n********** INVENTORY SUMMARY **********")

    
    total_items = len(items)
    print(f"\nTotal Different Items: {total_items}")
    item_names = [item['name'] for item in items]
    print(f"Explanation: You entered {total_items} different items: {', '.join(item_names)}.")

    
    total_quantity = sum(item['quantity'] for item in items)
    print(f"\nTotal Quantity in Stock: {total_quantity}")
    quantities = " + ".join(str(item['quantity']) for item in items)
    print(f"Explanation: Sum of all quantities: {quantities} = {total_quantity}")

  
    average = total_quantity / total_items
    print(f"\nAverage Quantity per Item: {average:.2f}")
    print(f"Explanation: Average = {total_quantity} total / {total_items} items")

    
    most_stocked = max(items, key=lambda x: x['quantity'])
    least_stocked = min(items, key=lambda x: x['quantity'])

    print(f"\nMost Stocked Item: {most_stocked['name']} ({most_stocked['quantity']} units)")
    print(f"Explanation: {most_stocked['name']} has the highest quantity among all items.")

    print(f"\nLeast Stocked Item: {least_stocked['name']} ({least_stocked['quantity']} units)")
    print(f"Explanation: {least_stocked['name']} has the lowest quantity.")

   
    categories = {item['category'] for item in items}
    print(f"\nUnique Categories in Inventory: {categories}")
    print("Explanation: Categories are taken from user input and converted to lowercase.\nNo duplicates are shown here.")


    sorted_items = sorted(items, key=lambda x: x['quantity'], reverse=True)
    print("\n Items Sorted by Quantity (High to Low):")
    for idx, item in enumerate(sorted_items, 1):
        print(f"{idx}. {item['name']} - {item['quantity']} units")
    print("\nExplanation: Items are sorted using the quantity field from highest to lowest.")

   
    sorted_categories = sorted(categories)
    print("\n Categories in Alphabetical Order:")
    for idx, cat in enumerate(sorted_categories, 1):
        print(f"{idx}. {cat}")
    print("\nExplanation: The set of unique categories was sorted alphabetically for display.")

    print("\n========== END OF REPORT ==========")


Data()

'''
=====Welcome to Inventory List Analyzer!=====

Enter item name: Milk
Enter category: dairy
Enter quantity: 10

Do you want to add more items? (y/n): y
Enter item name: Rice
Enter category: Grain
Enter quantity: 50

Do you want to add more items? (y/n): y
Enter item name: salt
Enter category: Spice
Enter quantity: 40

Do you want to add more items? (y/n): y
Enter item name: Sugar
Enter category: Grain
Enter quantity: 40

Do you want to add more items? (y/n): n

********** INVENTORY SUMMARY **********

Total Different Items: 4
Explanation: You entered 4 different items: Milk, Rice, salt, Sugar.

Total Quantity in Stock: 140
Explanation: Sum of all quantities: 10 + 50 + 40 + 40 = 140

Average Quantity per Item: 35.00
Explanation: Average = 140 total / 4 items

Most Stocked Item: Rice (50 units)
Explanation: Rice has the highest quantity among all items.

Least Stocked Item: Milk (10 units)
Explanation: Milk has the lowest quantity.

Unique Categories in Inventory: {'dairy', 'grain', 'spice'}
Explanation: Categories are taken from user input and converted to lowercase.
No duplicates are shown here.

 Items Sorted by Quantity (High to Low):
1. Rice - 50 units
2. salt - 40 units
3. Sugar - 40 units
4. Milk - 10 units

Explanation: Items are sorted using the quantity field from highest to lowest.

 Categories in Alphabetical Order:
1. dairy
2. grain
3. spice
'''

Explanation: The set of unique categories was sorted alphabetically for display.

========== END OF REPORT ==========


