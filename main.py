import csv
import time

from src.Expense import Expense
from utils.constants import category_types, app_header_art, printMenu


def insertExpense():
    '''FOR ADD EXPENSE'''
    expense = Expense()

    while True:
        name = input("Enter the name/description of the expense: ").strip()
        try:
            expense.set_name(name)
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

    while True:
        print(f"Available categories: {category_types}")
        category = input("Enter the category of the expense: ").strip()
        try:
            expense.set_category(category)
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

    while True:
        amount = input("Enter the amount of the expense: ").strip()
        try:
            expense.set_amount(amount)
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

    while True:
        date = input("Enter the date of the expense: ").strip()
        try:
            expense.set_date(date)
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

    while True:
        notes = input("Enter notes for the expense: ").strip()
        try:
            expense.set_notes(notes)
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

    expense.save_expense()

    print("\nExpense created successfully:")
    print(f"Name: {expense.name}")
    print(f"Category: {expense.category}")
    print(f"Amount: {expense.amount}")
    print(f"Date: {expense.date}")
    print(f"Notes: {expense.notes}")
    print(f"Unique ID: {expense.unique_id}")
    print(f"Recorded At: {expense.recorded_at}\n")



def showMenu():
    print(app_header_art)
    printMenu()

    while True:
        choose = input("Select an option (1-6): ").strip()
        if not choose.isdigit():
            print("Invalid choice. Please enter a number.")
            continue

        choose_int = int(choose)
        if choose_int < 1 or choose_int > 6:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        print("\n")

        if choose_int == 1:
            insertExpense()
        elif choose_int == 2:
            while True:
                chooseView = input("Would you like to view all expenses (1) or a specific expense (2)? ")
                if not chooseView.isdigit():
                    print("Invalid choice. Please enter a number.")
                    continue
                if int(chooseView) == 1:
                    viewExpenses()
                    break
                elif int(chooseView) == 2:
                    view_unique_expense()
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
        elif choose_int == 3:
            spendingAnalysis()
        elif choose_int == 4:
            editExpense()
        elif choose_int == 5:
            deleteExpense()
        elif choose_int == 6:
            print("Thank you for using this program")
            break

def viewExpenses():
    with open("outputs/expenses.csv", "r") as f:
        print("\n")
        reader = csv.reader(f)
        print("=" * 50)
        print("           YOUR EXPENSES")
        print("=" * 50)
        for r in reader:
            if len(r) < 7:
                continue
            print("Name         : " + r[1])
            print("Category     : " + r[3])
            print("Amount       : " + "$" + r[2])
            print("Date         : " + r[4])
            print("Notes        : " + r[5])
            print("Unique ID    : " + r[0])
            print("Recorded At  : " + r[6])
            print("-" * 50)
        print("\n")

def view_unique_expense():
    uniqueExpense = input("Please enter the unique ID of the expense you would like to view: ")
    expenseFound = False
    with open("outputs/expenses.csv", "r") as f:
        print("\n")
        reader = csv.reader(f)

        for r in reader:
            if len(r) < 7:
                continue

            if r[0] == uniqueExpense:
                expense = Expense(name = r[1], category = r[3], amount = float(r[2]), date = r[4], notes = r[5])
                expense.unique_id = r[0]
                print("\n" + "=" * 50)
                print("           YOUR EXPENSE")
                print("=" * 50)
                print(f"Name: {expense.name}")
                print(f"Category: {expense.category}")
                print(f"Amount: {expense.amount}")
                print(f"Date: {expense.date}")
                print(f"Notes: {expense.notes}")
                print(f"Unique ID: {expense.unique_id}")
                print(f"Recorded At: {expense.recorded_at}")
                print("-" * 50 + "\n")

                expenseFound = True
                break

    if not expenseFound:
        print("No expense found with that unique ID.")
        print()


def spendingAnalysis():
    with open("outputs/expenses.csv", "r") as f:
        reader = csv.reader(f)
        highestExpense = 0
        lowestExpense = None
        highestRecorded = ""
        lowestRecorded = ""
        categories = []
        categorySpent = []
        totalSpent = 0

        for r in reader:
            if len(r) < 7:
                continue

            amount = float(r[2])
            totalSpent += amount
            category = r[3].strip().lower()

            if amount > highestExpense:
                highestExpense = amount
                highestRecorded = r[6]

            if lowestExpense == None or lowestExpense > amount :
                lowestExpense = amount
                lowestRecorded = r[6]

            if category not in categories:
                categories.append(category)
                categorySpent.append(amount)
            else:
                i = categories.index(category)
                categorySpent[i] += amount

        print("=" * 50)
        print("           SPENDING ANALYSIS")
        print("=" * 50)
        for i in range(len(categories)):
            percent = int((categorySpent[i]/totalSpent)*100)
            print(categories[i] + ": $"+ str(categorySpent[i]) + " (%" + str(percent) + ")")
            print()
        print("-" * 50)
        print()
        print("The highest expense is: $" + str(highestExpense) + ", recorded on "+ highestRecorded)
        print("The lowest expense is: $" + str(lowestExpense) + ", recorded on " + lowestRecorded+"\n")

def editExpense():
    while True:
        edit_or_delete = input("Would you like to edit or delete an expense (E/D): ").lower()
        if edit_or_delete == "e":
            desc = input("Enter description of the expense you would like to edit: ").lower()
            break
        elif edit_or_delete == "d":
            desc = input("Enter description of the expense you would like to delete: ").lower()
            break
        else:
            print("Invalid option, please try again")

    with open("database/expenses.csv", "r") as f:
        reader = csv.reader(f)
        if(edit_or_delete == "e"):
            for r in reader:
                if len(r) < 5:
                    continue
                if r[1].lower() == desc:
                    d = input("Enter new description (or leave blank to keep it): ")
                    a = input("Enter new amount (or leave blank to keep it): ")
                    c = input("Enter new Category (or leave blank to keep it): ")
                    e = input("Enter new expense date (or leave blank to keep it): ")

                    if d != "":
                        r[1] = d
                    if a != "":
                        r[2] = a
                    if c != "":
                        r[3] = c
                    if e != "":
                        r[4] = e

                    print("Expenses have been edited")

def deleteExpense():
    pass
if __name__ == '__main__':
    # TODO: ADD MENU FUNCTIONALITY
    # 1. Add expense
    # a. validate inputs from user one by one and validate them in the Expense class individaully AND CLEAN THE CODE
    # 2. View expense
    # View All expenses
    # View by unique id (find unique id, get expense, fill into expense object and print it out)
    # 3. Spending analysis
    # 4. Edit/Delete expense
    # 5. Exit
    showMenu()
