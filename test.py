
def add_expense():
    while True:
        description = input("What is the description of your expense?\n").strip()
        if not description:
            print("########################")
            print("No description provided")
            print("########################")
            continue

        while True:
            try:
                amount = float(input("What is the amount of your expense? \n"))
                if not amount:
                    print("No amount provided")
                    continue

                break
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                continue
            except IOError:
                print("Error reading input. Please try again.")
                continue
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                continue

            print(f"Expense Description: {description}")
            print(f"Expense Amount: {amount}")

if __name__ == '__main__':

        add_expense()

        # todo: SAVE EXPENSE TO CSV



