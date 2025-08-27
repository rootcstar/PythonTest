import csv
import time
from src.Expense import Expense
from utils.constants import category_types, app_header_art, printMenu






def validate_expenses(existing_expense=None):

    expense = existing_expense or Expense()

    #Name
    while True:
        name = input("Enter the name/description of the expense: ").strip()
        if existing_expense and not name:  # Allow keeping old value
            break
        try:
            expense.set_name(name)
            break
        except Exception as e:
            print(f"Error: {e}")

    #Category
    while True:
        print(f"Available categories: {category_types}")
        category = input("Enter the category of the expense: ").strip()
        if existing_expense and not category:
            break
        try:
            expense.set_category(category)
            break
        except Exception as e:
            print(f"Error: {e}")

    #Amount
    while True:
        amount = input("Enter the amount of the expense: ").strip()
        if existing_expense and not amount:
            break
        try:
            expense.set_amount(amount)
            break
        except Exception as e:
            print(f"Error: {e}")

    #Date
    while True:
        date = input("Enter the date of the expense: ").strip()
        if existing_expense and not date:
            break
        try:
            expense.set_date(date)
            break
        except Exception as e:
            print(f"Error: {e}")

    #Notes
    while True:
        notes = input("Enter notes for the expense: ").strip()
        if existing_expense and not notes:
            break
        try:
            expense.set_notes(notes)
            break
        except Exception as e:
            print(f"Error: {e}")

    return expense


def insertExpense():
    # Validate and save new expense
    expense = validate_expenses()
    expense.save_expense()

    # Confirmation print
    print("\nExpense created successfully:")
    print(f"  Name       : {expense.name}")
    print(f"  Category   : {expense.category}")
    print(f"  Amount     : {expense.amount}")
    print(f"  Date       : {expense.date}")
    print(f"  Notes      : {expense.notes}")
    print(f"  Unique ID  : {expense.unique_id}")
    print(f"  Recorded At: {expense.recorded_at}\n")


def showMenu():

    print(app_header_art)
    printMenu()

    while True:
        # Get main menu choice
        choice = input("Select an option (1-6): ").strip()
        if not choice.isdigit():
            print("Invalid choice. Please enter a number.")
            continue

        choice_int = int(choice)
        if choice_int < 1 or choice_int > 6:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        print("\n")

        # check menu options
        if choice_int == 1:
            insertExpense()

        elif choice_int == 2:
            # Submenu for viewing expenses
            while True:
                sub_choice = input("Would you like to view all expenses (1) or a specific expense (2)? ").strip()

                if not sub_choice.isdigit():
                    print("Invalid choice. Please enter a number.")
                    continue

                sub_choice_int = int(sub_choice)
                if sub_choice_int == 1:
                    viewExpenses()
                    break
                elif sub_choice_int == 2:
                    view_unique_expense()
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")

        elif choice_int == 3:
            spendingAnalysis()

        elif choice_int == 4:
            editExpense()

        elif choice_int == 5:
            deleteExpense()

        elif choice_int == 6:
            print("Thank you for using this program.")
            break


def viewExpenses():
    with open("outputs/expenses.csv", "r") as f:
        reader = csv.reader(f)

        print("\n" + "=" * 50)
        print("                 YOUR EXPENSES")
        print("=" * 50)

        for row in reader:

            if len(row) < 7:
                continue

            print(f"Name        : {row[1]}")
            print(f"Category    : {row[3]}")
            print(f"Amount      : ${row[2]}")
            print(f"Date        : {row[4]}")
            print(f"Notes       : {row[5]}")
            print(f"Unique ID   : {row[0]}")
            print(f"Recorded At : {row[6]}")
            print("-" * 50)

        print("\n")


def view_unique_expense():

    unique_id = input("Please enter the unique ID of the expense you would like to view: ").strip()
    expense_found = False

    with open("outputs/expenses.csv", "r") as f:
        reader = csv.reader(f)

        for row in reader:

            if len(row) < 7:
                continue

            if row[0] == unique_id:
                expense = Expense(
                    name=row[1],
                    category=row[3],
                    amount=float(row[2]),
                    date=row[4],
                    notes=row[5]
                )
                expense.unique_id = row[0]
                expense.recorded_at = row[6]

                print("\n" + "=" * 50)
                print("                YOUR EXPENSE")
                print("=" * 50)
                print(f"Name        : {expense.name}")
                print(f"Category    : {expense.category}")
                print(f"Amount      : ${expense.amount:.2f}")
                print(f"Date        : {expense.date}")
                print(f"Notes       : {expense.notes}")
                print(f"Unique ID   : {expense.unique_id}")
                print(f"Recorded At : {expense.recorded_at}")
                print("-" * 50 + "\n")

                expense_found = True
                break

    if not expense_found:
        print("No expense found with that unique ID.\n")


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

            if lowestExpense is None or lowestExpense > amount:
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
            percent = int((categorySpent[i] / totalSpent) * 100)
            print(categories[i] + ": $" + str(categorySpent[i]) +
                  " (%" + str(percent) + ")")
            print()

        print("-" * 50)
        print()
        print("The highest expense is: $" + str(highestExpense) +
              ", recorded on " + highestRecorded)
        print("The lowest expense is: $" + str(lowestExpense) +
              ", recorded on " + lowestRecorded + "\n")


def editExpense():
    choose_edit = input("Please enter the unique ID of the expense you would like to edit: ")
    expenseFound = False
    rows = []

    with open("outputs/expenses.csv", "r") as f:
        print("\n")
        reader = csv.reader(f)

        for r in reader:
            if len(r) < 7:
                rows.append(r)
                continue

            if r[0] == choose_edit:
                expenseFound = True
                print("\nEnter new values (Leave blank to keep current values):")

                expense = Expense(
                    name=r[1],
                    category=r[3],
                    amount=float(r[2]),
                    date=r[4],
                    notes=r[5]
                )
                expense = validate_expenses(existing_expense=expense)

                rows.append([
                    r[0],
                    expense.name,
                    expense.amount,
                    expense.category,
                    expense.date,
                    expense.notes,
                    r[6]
                ])
            else:
                rows.append(r)

    if not expenseFound:
        print("No expense found with that unique ID.")
        return

    with open("outputs/expenses.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("Expense has been updated successfully.\n")


def deleteExpense():
    choose_del = input("Please enter the unique ID of the expense you would like to delete: ").strip()
    print("\n")
    expenseFound = False
    rows = []

    with open("outputs/expenses.csv", "r") as f:
        reader = csv.reader(f)
        for r in reader:
            if len(r) < 7:
                rows.append(r)
                continue

            if r[0] == choose_del:
                expenseFound = True
                print(f"Expense {r[0]} deleted\n")
            else:
                rows.append(r)

    if not expenseFound:
        print("No expense found with that unique ID.\n")
        return

    with open("outputs/expenses.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


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
