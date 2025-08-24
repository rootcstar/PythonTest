import os
class AppSettings:

    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


    EXPENSES_CSV_PATH: str = os.path.join(PROJECT_ROOT, 'outputs', 'expenses.csv')