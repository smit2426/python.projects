



def main():
    """Main menu interface for the Data Analyzer and Transformer Program."""
    while True:
        print("\n___Welcome to the Data Analyzer and Transformer Program___")
        print("")
        print("---Main Menu---")
        print("1. Input Data")
        print("2. Display Data Summary ")
        print("3. Calculate Factorial ")
        print("4. Filter Data by Threshold ")
        print("5. Sort Data")
        print("6. Display Dataset Statistics ")
        print("7. Exit Program")

        choice = input("Please enter your choice: ")

        if choice == '1':
            input_data()
        elif choice == '2':
            display_data_summary()
        elif choice == '3':
            calculate_factorial()
        elif choice == '4':
            filter_by_threshold()
        elif choice == '5':
            sort_data()
        elif choice == '6':
            display_data_summary()
        elif choice == '7':
            print("Exiting program!")
            break
        else:
            print("Invalid choice. Please try again.")


def input_data():
    """Takes input from the user for a 1D array."""
    global data
    data = list(map(int, input("Enter data for a 1D array (separated by spaces): ").split()))
    print("Data has been stored successfully!")

def display_data_summary():
    """Displays sum and average of the dataset."""
    print(f"Sum: {sum(data)}")
    print(f"Average: {sum(data)/len(data):.2f}")

def calculate_factorial():
    """Calculates factorial of a number using recursion."""
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

    num = int(input("Enter a number to calculate factorial: "))
    print(f"Factorial of {num} is {factorial(num)}")

def filter_by_threshold():
    """Filters the dataset using a lambda function and user-defined threshold."""
    threshold = int(input("Enter threshold value: "))
    filtered = list(filter(lambda x: x >= threshold, data))
    print(f"Filtered data (≥ {threshold}): {filtered}")

def sort_data():
    """Sorts the dataset and displays it."""
    order = input("Sort in ascending or descending (a/d)? ").lower()
    if order == 'a':
        sorted_data = sorted(data)
    else:
        sorted_data = sorted(data, reverse=True)
    print(f"Sorted data: {sorted_data}")

def display_data_summary():
    """Displays full data summary using built-in functions."""
    if not data:
        print("No data found. Please input data first (Option 1).")
        return
    
    print("\nData Summary:")
    print(f"- Total elements: {len(data)}")
    print(f"- Minimum value: {min(data)}")
    print(f"- Maximum value: {max(data)}")
    print(f"- Sum of all values: {sum(data)}")
    average = sum(data) / len(data)
    print(f"- Average value: {average:.2f}")




data = []
main()

'''
___Welcome to the Data Analyzer and Transformer Program___

---Main Menu---
1. Input Data
2. Display Data Summary 
3. Calculate Factorial 
4. Filter Data by Threshold 
5. Sort Data
6. Display Dataset Statistics 
7. Exit Program
Please enter your choice: 1
Enter data for a 1D array (separated by spaces): 35 13 54 78 43 22 89
Data has been stored successfully!

___Welcome to the Data Analyzer and Transformer Program___

---Main Menu---
1. Input Data
2. Display Data Summary 
3. Calculate Factorial 
4. Filter Data by Threshold 
5. Sort Data
6. Display Dataset Statistics 
7. Exit Program
Please enter your choice: 2

Data Summary:
- Total elements: 7
- Minimum value: 13
- Maximum value: 89
- Sum of all values: 334
- Average value: 47.71

___Welcome to the Data Analyzer and Transformer Program___

---Main Menu---
1. Input Data
2. Display Data Summary 
3. Calculate Factorial 
4. Filter Data by Threshold 
5. Sort Data
6. Display Dataset Statistics 
7. Exit Program
Please enter your choice: 3
Enter a number to calculate factorial: 5
Factorial of 5 is 120

___Welcome to the Data Analyzer and Transformer Program___

---Main Menu---
1. Input Data
2. Display Data Summary 
3. Calculate Factorial 
4. Filter Data by Threshold 
5. Sort Data
6. Display Dataset Statistics 
7. Exit Program
Please enter your choice: 4
Enter threshold value: 2
Filtered data (≥ 2): [35, 13, 54, 78, 43, 22, 89]

___Welcome to the Data Analyzer and Transformer Program___

---Main Menu---
1. Input Data
2. Display Data Summary 
3. Calculate Factorial 
4. Filter Data by Threshold 
5. Sort Data
6. Display Dataset Statistics 
7. Exit Program
Please enter your choice: 5
Sort in ascending or descending (a/d)? 1
Sorted data: [89, 78, 54, 43, 35, 22, 13]

___Welcome to the Data Analyzer and Transformer Program___

---Main Menu---
1. Input Data
2. Display Data Summary 
3. Calculate Factorial 
4. Filter Data by Threshold 
5. Sort Data
6. Display Dataset Statistics 
7. Exit Program
Please enter your choice: 6

Data Summary:
- Total elements: 7
- Minimum value: 13
- Maximum value: 89
- Sum of all values: 334
- Average value: 47.71

___Welcome to the Data Analyzer and Transformer Program___

---Main Menu---
1. Input Data
2. Display Data Summary 
3. Calculate Factorial 
4. Filter Data by Threshold 
5. Sort Data
6. Display Dataset Statistics 
7. Exit Program
Please enter your choice: 7
Exiting program!
'''


