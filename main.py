import csv
import numpy
import pandas as pd





def addExpenses():
    while True:
        description = input("Enter the description of the expense: ").strip()
        if description == "":
            description = input("No valid description entered")
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
    with open("expenses.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([description, expenseAmount])




def viewExpenses():
    with open("expenses.csv", "r") as f:
        text = f.readlines()
        for text in text:
            print(text)





if __name__ == '__main__':
    addExpenses()
    viewExpenses()


