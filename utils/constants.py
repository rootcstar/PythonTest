
#ASCII Art for the application header
app_header_art: str = r"""
 ███████╗███╗   ███╗ █████╗ ██████╗ ████████╗███████╗███████╗██╗     ██╗     
 ██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝██║     ██║     
 ███████╗██╔████╔██║███████║██████╔╝   ██║   ███████╗█████╗  ██║     ██║     
 ╚════██║██║╚██╔╝██║██╔══██║██╔══██╗   ██║   ╚════██║██╔══╝  ██║     ██║     
 ███████║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║   ███████║███████╗███████╗███████╗
 ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚══════╝
 
                 by Fiki Tech Solutions LLC  @2024
                        
 ════════════════════════════════════════════════════════════════════════════
"""


category_types = [
    "Food",
    "Transport",
    "Utilities",
    "Entertainment",
    "Healthcare",
    "Education",
    "Personal Care"
]


def printMenu():
    print("\n===== Expense Manager Menu =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Spending Analysis")
    print("4. Edit Expense")
    print("5. Delete Expense")
    print("6. Exit\n")
