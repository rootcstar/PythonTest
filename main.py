import csv
import time

from src.Expense import Expense
from utils.constants import category_types

def insertExpense():
    '''FOR ADD EXPENSE'''
    expense = Expense()
    while True:
        name = input("Enter the name/description of the expense: ").strip()
        try:
            expense.set_name(name)
        except Exception as e:
            print(f"Error: {e}")
            continue

    while True:
        print(f"Available categories: {category_types}")
        category = input("Enter the category of the expense: ").strip()
        try:
            expense.set_category(category)
        except Exception as e:
            print(f"Error: {e}")
            continue



    print("Expense created successfully:")
    print(f"Name: {expense.name}")
    print(f"Category: {expense.category}")
    print(f"Amount: {expense.amount}")
    print(f"Date: {expense.date}")
    print(f"Notes: {expense.notes}")
    print(f"Unique ID: {expense.unique_id}")
    print(f"Recorded At: {expense.recorded_at}")

    expense.save_expense()


def showMenu():
    #TODO: ADD MENU FUNCTIONALITY
    #1. Add expense
        #a. validate inputs from user one by one and validate them in the Expense class individaully AND CLEAN THE CODE
    #2. View expense
        # View All expenses
        # View by unique id (find unique id, get expense, fill into expense object and print it out)
    #3. Spending analysis
    #4. Edit/Delete expense
    #5. Exit
    pass

def old_addExpenses():
    while True:
        description = input("Enter the description of the expense: ").strip()
        if description == "":
            print("No valid description entered")
            continue
        break

    while True:
        category = input("Enter category (e.g., Food, Transport): ").strip()
        if category == "":
            print("No valid category entered")
            continue
        break

    while True:
        try:
            expenseAmount = float(input("Enter expense amount: "))
            if expenseAmount == 0.0:
                print("No expense amount provided")
                continue
            break
        except ValueError:
            print("Invalid amount, please choose a valid number")

    while True:
        userDate = input("Enter the date of the expense (MM/DD/YYYY): ").strip()
        if userDate == "":
            print("No valid date entered")
            continue

        dateLength = userDate.split("/")

        if len(dateLength) == 3 and dateLength[0].isdigit() and dateLength[1].isdigit() and dateLength[2].isdigit():
            if len(dateLength[0])== 2 and len(dateLength[1])==2 and len(dateLength[2])==4 and int(dateLength[0]) <= 12 and int(dateLength[1]) <= 31:
                break
            else:
                print("invalid date, enter (MM/DD/YYYY)")
        else:
            print("invalid date, enter (MM/DD/YYYY)")
            continue

    recordDate = time.ctime(int(time.time()))
    with open("database/expenses.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([recordDate,description, expenseAmount,category, userDate])

def viewExpenses():
    with open("database/expenses.csv", "r") as f:
        reader = csv.reader(f)
        print("=" * 50)
        print("           YOUR EXPENSES")
        print("=" * 50)
        for r in reader:
            if len(r) < 5:
                continue
            print("Recorded date: " + r[0])
            print("Description  : " + r[1])
            print("Amount       : " + "$" + r[2])
            print("Category     : " + r[3])
            print("Expense date : " + r[4])
            print("-" * 50)

def spendingAnalysis():
    with open("database/expenses.csv", "r") as f:
        reader = csv.reader(f)
        highestExpense = 0
        lowestExpense = None
        highestRecorded = ""
        lowestRecorded = ""
        categories = []
        categorySpent = []
        totalSpent =0

        for r in reader:
            if len(r) <5:
                continue
            if float(r[2]) > highestExpense:
                highestExpense = float(r[2])
                highestRecorded = r[0]
            if lowestExpense == None or lowestExpense > float(r[2]) :
                lowestExpense = float(r[2])
                lowestRecorded = r[0]

            totalSpent += float(r[2])
            category = r[3].strip().lower()
            amountSpent = float(r[2])
            if category not in categories:
                categories.append(category)
                categorySpent.append(amountSpent)
            else:
                i = categories.index(category)
                categorySpent[i] += amountSpent

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
        print("The lowest expense is: $" + str(lowestExpense) + ", recorded on " + lowestRecorded)

def edit_delete_expenses():
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

if __name__ == '__main__':

    exit(0)


    while True:
        add = input("Would you like to add a new expense? (Y/N): ")
        if add.lower() == "y":
            old_addExpenses()
            print()
        elif add.lower() == "n":
            while True:
                view = input("Would you like to view the expenses and spending analysis? (Y/N): ")
                if view.lower() == "y":
                    viewExpenses()
                    print("\n")
                    spendingAnalysis()
                    print()
                    break
                elif view.lower() == "n":
                    print("Thank you for using this program")
                    exit()
                else:
                    print("Invalid input, please try again")
        else:
            print("Invalid input, please try again")