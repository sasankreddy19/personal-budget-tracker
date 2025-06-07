Personal Budget Tracker 
================================

Overview
--------

The **Personal Budget Tracker** is a Python program created as a final project for Stanford’s Code in Place 2025. This beginner-friendly tool helps users manage their finances by tracking income and expenses, categorizing transactions, and providing summaries and visualizations. It uses core Python concepts (lists, dictionaries, loops, conditionals, functions, and user input/output) taught in the six-week introductory course, making it accessible for those new to programming.

Purpose
-------

The program allows users to:

*   Record income and expenses with descriptions and categories.
    
*   View their total income, expenses, and balance.
    
*   See spending or income totals by category.
    
*   Visualize expenses with a simple text-based chart.
    
*   List all transactions for review.
    

It’s designed to be practical, user-friendly, and a showcase of fundamental Python skills for the Code in Place portfolio.

Features
--------

1.  **Add Transaction**:
    
    *   Users input a transaction’s description (e.g., “Grocery”), amount (positive for income, negative for expenses), and category (e.g., “Food”).
        
    *   Transactions are stored in a list of dictionaries.
        
    *   Includes error handling for invalid numeric inputs.
        
2.  **View Balance**:
    
    *   Calculates and displays total income, total expenses, and net balance, formatted to two decimal places for currency.
        
3.  **View Spending by Category**:
    
    *   Shows the total amount (income or expense) for each category, aggregated from all transactions.
        
4.  **Display Spending Chart**:
    
    *   Creates a text-based bar chart of expenses by category, using asterisks (\*) scaled to the largest expense (up to 20 characters).
        
    *   Only expenses (negative amounts) are included in the chart.
        
5.  **List All Transactions**:
    
    *   Displays all recorded transactions with their index, description, category, and amount.
        
6.  **Menu-Driven Interface**:
    
    *   A numbered menu (1–6) lets users select actions or exit the program.
        
    *   Clear prompts guide the user through each step.
        

How It Works
------------

The program runs in a loop, displaying a menu with six options:

1.  **Add Transaction**: Prompts for description, amount, and category, then stores the data.
    
2.  **View Balance**: Sums positive amounts (income) and negative amounts (expenses) to show the financial overview.
    
3.  **View Spending by Category**: Aggregates transaction amounts by category using a dictionary.
    
4.  **Display Spending Chart**: Scales expenses to create a proportional text-based bar chart.
    
5.  **List All Transactions**: Shows all stored transactions in a numbered list.
    
6.  **Exit**: Ends the program.
    

The program uses a list of dictionaries to store transactions, where each transaction is a dictionary with keys description, amount, and category. Functions handle specific tasks (e.g., add\_transaction, view\_balance), keeping the code modular and readable. Error handling ensures robustness, such as catching non-numeric inputs for amounts.

Requirements
------------

*   **Python Version**: Python 3.x (compatible with Code in Place’s environment).
    
*   **Libraries**: No external libraries are required; uses only standard Python (built-in modules like sum).
    
*   **Environment**: Any Python-compatible environment (e.g., IDLE, VS Code, or online IDEs like Repl.it).
    

How to Run
----------

1.  **Save the Code**:
    
    *   Copy the program code into a file named budget\_tracker.py.
        
2.  **Run the Program**:
    
    *   Open a terminal or Python IDE.
        
    *   Navigate to the directory containing budget\_tracker.py.
        
    *   Run the command: python budget\_tracker.py (or python3 budget\_tracker.py on some systems).
        
3.  **Interact with the Program**:
    
    *   Follow the on-screen menu to select options (1–6).
        
    *   For example, choose “1” to add a transaction, enter details like “Salary, 1000, Income,” then explore other options to view summaries or charts.
        

Example Usage
-------------
# === Personal Budget Tracker ===

## 1. Add Transaction  
## 2. View Balance  
## 3. View Spending by Category  
## 4. Display Spending Chart  
## 5. List All Transactions  
## 6. Exit  

---

### ➤ Enter your choice (1-6): **1**

**Enter transaction description (e.g., Grocery, Salary):** Salary  
**Enter amount (positive for income, negative for expense):** 1000  
**Enter category (e.g., Food, Bills, Income):** Income  

✅ Transaction added successfully!

---

### ➤ Enter your choice (1-6): **1**

**Enter transaction description (e.g., Grocery, Salary):** Grocery  
**Enter amount (positive for income, negative for expense):** -50  
**Enter category (e.g., Food, Bills, Income):** Food  

✅ Transaction added successfully!

---

### ➤ Enter your choice (1-6): **2**

**Total Income:** $1000.00  
**Total Expenses:** $-50.00  
**Current Balance:** $950.00

---

### ➤ Enter your choice (1-6): **4**

## Spending by Category (Chart):
Food | ******************** $50.00

--------------

*   budget\_tracker.py: The main Python program containing all code and functions.
    
*   No additional files are needed, as the program stores data in memory during runtime.
    

Limitations
-----------

*   **Data Persistence**: Transactions are not saved to a file, so they reset when the program closes. (File I/O was not covered in Code in Place’s core curriculum.)
    
*   **Chart Simplicity**: The chart is text-based, as graphical libraries like tkinter were not used to keep the project beginner-friendly.
    
*   **Input Validation**: Basic error handling is included, but advanced validation (e.g., checking for empty descriptions) could be added.
    

Future Enhancements
-------------------

*   Add file I/O to save transactions to a file (e.g., CSV) for persistence.
    
*   Include budget alerts (e.g., warn when spending exceeds a threshold).
    
*   Enhance the chart with colors using a library like termcolor.
    
*   Add the ability to edit or delete transactions.
    

Why This Project?
-----------------

This project demonstrates mastery of Code in Place 2025’s Python fundamentals while creating a practical tool for financial management. Its modular design, clear user interface, and creative chart feature make it a strong addition to my Stanford-hosted code portfolio. It’s both functional and engaging, reflecting the course’s emphasis on coding with purpose and creativity.

Contact
-------

For questions or feedback about this project, feel free to reach out via the Code in Place community or Stanford’s course platform.

_Developed by Dwarampudi Sasank Reddy for Code in Place 2025_
