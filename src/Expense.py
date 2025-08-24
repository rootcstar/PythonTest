from datetime import datetime
from utils.constants import category_types
import csv
from config.settings import AppSettings
from utils.helper import generate_uuid, check_none_or_empty_string


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


        #ensure file exists
        with open(AppSettings.EXPENSES_CSV_PATH, "a") as f:
            pass


    def validate_data(self,name="", category="", amount=0.0, date=None, notes=""):
        # Basic validation for None and empty values
        params = locals()
        params.pop("self")
        for key, value in params.items():
            if value is None:
                raise ValueError(f"{key} cannot be None.")
            if isinstance(value,str):
                if value.strip() == "":
                    raise ValueError(f"{key} cannot be empty or whitespace.")

        # Validate date format
        try:
            datetime.strptime(self.date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

        # Validate amount
        if self.amount <= 0:
            raise ValueError("Expense amount must be greater than zero.")

        #validate category
        valid_categories = self.category_types
        if self.category not in valid_categories:
            raise ValueError(f"Invalid category. Must be one of: {', '.join(valid_categories)}")


    def set_name(self, name):
        if not self.validate_name(name):
            raise ValueError("Invalid name provided.")
        self.name = name


    def validate_name(self, name):
        if not check_none_or_empty_string(name):
            return False




    def save_expense(self):
        while True:
            #get the records, unique ids and create one
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


        try:
            with open(AppSettings.EXPENSES_CSV_PATH, "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerow([self.unique_id, self.name, f"{self.amount:.2f}", self.category, self.date, self.notes, self.recorded_at.strftime("%Y-%m-%d %H:%M:%S")])
        except Exception as e:
            print(f"Error saving expense: {e} with data {self.__dict__}")
            raise




















'''
try:

    Expense(name="Lunch", category="Food", amount=12.50, date="2024-10-01", notes="Business meeting")

except Exception as e:
    print(f"Unexpected error during validation: {e}")
    raise

Expense("Taxi", "Transport", 30.00, "2024-10-02", "Airport to hotel")'''