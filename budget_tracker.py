# Personal Budget Tracker
# A program to track income and expenses, categorize transactions, and display summaries.

def add_transaction(transactions):
    """Add a new transaction to the list."""
    try:
        description = input("Enter transaction description (e.g., Grocery, Salary): ")
        amount = float(input("Enter amount (positive for income, negative for expense): "))
        category = input("Enter category (e.g., Food, Bills, Income): ")
        transactions.append({"description": description, "amount": amount, "category": category})
        print("Transaction added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_balance(transactions):
    """Calculate and display total income, expenses, and balance."""
    income = sum(t["amount"] for t in transactions if t["amount"] > 0)
    expenses = sum(t["amount"] for t in transactions if t["amount"] < 0)
    balance = income + expenses  # Expenses are negative, so addition works
    print(f"\nTotal Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Current Balance: ${balance:.2f}")

def view_by_category(transactions):
    """Display total spending or income by category."""
    categories = {}
    for t in transactions:
        category = t["category"]
        amount = t["amount"]
        if category not in categories:
            categories[category] = 0
        categories[category] += amount
    
    print("\nSummary by Category:")
    for category, total in categories.items():
        print(f"{category}: ${total:.2f}")

def display_chart(transactions):
    """Display a simple text-based chart of spending by category."""
    categories = {}
    for t in transactions:
        category = t["category"]
        amount = t["amount"]
        if amount < 0:  # Only include expenses for the chart
            if category not in categories:
                categories[category] = 0
            categories[category] += abs(amount)  # Use absolute value for expenses
    
    if not categories:
        print("\nNo expenses to display in chart.")
        return
    
    max_amount = max(categories.values())
    if max_amount == 0:
        print("\nNo expenses to display in chart.")
        return
    
    print("\nSpending by Category (Chart):")
    for category, amount in categories.items():
        bar_length = int((amount / max_amount) * 20)  # Scale to 20 characters
        bar = "*" * bar_length
        print(f"{category:15} | {bar} ${amount:.2f}")

def list_transactions(transactions):
    """List all transactions."""
    if not transactions:
        print("\nNo transactions recorded.")
        return
    print("\nAll Transactions:")
    for i, t in enumerate(transactions, 1):
        print(f"{i}. {t['description']} ({t['category']}): ${t['amount']:.2f}")

def main():
    """Main function to run the budget tracker."""
    transactions = []  # List to store all transactions
    while True:
        print("\n=== Personal Budget Tracker ===")
        print("1. Add Transaction")
        print("2. View Balance")
        print("3. View Spending by Category")
        print("4. Display Spending Chart")
        print("5. List All Transactions")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_balance(transactions)
        elif choice == "3":
            view_by_category(transactions)
        elif choice == "4":
            display_chart(transactions)
        elif choice == "5":
            list_transactions(transactions)
        elif choice == "6":
            print("Thank you for using the Budget Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
