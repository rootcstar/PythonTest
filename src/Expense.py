from datetime import datetime
from utils.constants import category_types
import csv
import os
from config.settings import AppSettings
from utils.helper import generate_uuid, check_none_or_empty_string, checkAmount


class Expense:
    def __init__(self, name="", category="", amount=0.0, date=None, notes=""):
        self.unique_id = None
        self.category_types = category_types
        self.name = name
        self.category = category
        self.amount = amount
        self.date = date
        self.notes = notes
        self.recorded_at = datetime.now()

        # Ensure file exists
        folder = os.path.dirname(AppSettings.EXPENSES_CSV_PATH)
        os.makedirs(folder, exist_ok=True)
        with open(AppSettings.EXPENSES_CSV_PATH, "a") as f:
            pass

    def set_name(self, name):
        if not self.validate_name(name):
            raise ValueError("Invalid name provided.")
        self.name = name

    def validate_name(self, name):
        return check_none_or_empty_string(name, "name")

    def set_category(self, category):
        if not self.validate_category(category):
            raise ValueError(f"Invalid category. Must be one of: {', '.join(self.category_types)}")
        self.category = category.strip().title()

    def validate_category(self, category):
        valid_categories = [i.strip().lower() for i in self.category_types]
        return check_none_or_empty_string(category, "category") and category.strip().lower() in valid_categories

    def set_amount(self, amount_str):
        amount = self.validate_amount(amount_str)
        self.amount = amount

    def validate_amount(self, amount_str):
        if not check_none_or_empty_string(amount_str, "amount"):
            raise ValueError("Amount cannot be empty.")
        try:
            amount = float(amount_str)
        except ValueError:
            raise ValueError("Amount must be a valid number.")
        if not checkAmount(amount, "amount"):
            raise ValueError("Invalid amount provided.")
        return amount

    def set_date(self, date):
        self.validate_date(date)
        self.date = date

    def validate_date(self, date):
        if date is None:
            raise ValueError("Date cannot be None.")
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

    def set_notes(self, notes):
        if not self.validate_notes(notes):
            raise ValueError("Invalid notes provided.")
        self.notes = notes

    def validate_notes(self, notes):
        return check_none_or_empty_string(notes, "notes")

    def save_expense(self):
        # Generate unique ID
        while True:
            id = generate_uuid()
            try:
                with open(AppSettings.EXPENSES_CSV_PATH, "r") as f:
                    reader = csv.reader(f)
                    existing_ids = {row[0] for row in reader if row}
                    if id not in existing_ids:
                        self.unique_id = id
                        break
            except Exception as e:
                print(f"Error checking existing IDs: {e}")
                raise

        # Write to CSV
        try:
            with open(AppSettings.EXPENSES_CSV_PATH, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    self.unique_id,
                    self.name,
                    f"{self.amount:.2f}",
                    self.category,
                    self.date,
                    self.notes,
                    self.recorded_at.strftime("%Y-%m-%d %H:%M:%S")
                ])
        except Exception as e:
            print(f"Error saving expense: {e} with data {self.__dict__}")
            raise