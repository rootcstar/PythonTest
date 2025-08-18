import csv
import numpy
import pandas as pd
import time





def addExpenses():
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
            if len(dateLength[0])== 2 and len(dateLength[1])==2 and len(dateLength[2])==4:
                break
            else:
                print("invalid date, enter (MM/DD/YYYY)")
        else:
            print("invalid date, enter (MM/DD/YYYY)")
            continue

    recordDate = time.ctime(int(time.time()))
    with open("expenses.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([recordDate,description, expenseAmount,category, userDate])

def viewExpenses():
    with open("expenses.csv", "r") as f:
        reader = csv.reader(f)

        print("="*50)
        print("           YOUR EXPENSES")
        print("=" * 50)
        for r in reader:
            if len(r) <5:
                continue
            print("Recorded date: " + r[0])
            print("Description  : " + r[1])
            print("Amount       : " + "$" + r[2])
            print("Category     : " + r[3])
            print("Expense date : " + r[4])
            print("-" * 50)

def spendingAnalysis():
    with open("expenses.csv", "r") as f:
        reader = csv.reader(f)
        highestExpense = 0
        lowestExpense = None
        highestRecorded = ""
        lowestRecorded = ""

        for r in reader:
            if len(r) <5:
                continue
            if float(r[2]) > highestExpense:
                highestExpense = float(r[2])
                highestRecorded = r[0]
            if lowestExpense == None or lowestExpense > float(r[2]) :
                lowestExpense = float(r[2])
                lowestRecorded = r[0]





        print("The highest expense is: $" + str(highestExpense) + ", recorded on "+ highestRecorded)
        print("The lowest expense is: $" + str(lowestExpense) + ", recorded on " + lowestRecorded)




if __name__ == '__main__':
    addExpenses()
    print()
    viewExpenses()
    print()
    spendingAnalysis()
    print()


