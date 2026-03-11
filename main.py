# Get monthly income from user and convert to float
income = float(input("Enter your monthly income: "))

# Get individual expense amounts from user and convert to float
rent = float(input("Enter rent amount: "))
food = float(input("Enter food amount: "))
transportation = float(input("Enter transportation amount: "))
entertainment = float(input("Enter entertainment amount: "))
other = float(input("Enter other expenses amount: "))

# Calculate total expenses by adding all expense categories
total_expenses = rent + food + transportation + entertainment + other
# Calculate remaining balance by subtracting total expenses from income
balance = income - total_expenses

# Print a header for the budget summary
print("\n--- Budget Summary ---")
# Display the user's monthly income
print("Income: $", income)
# Display the total of all expenses
print("Total Expenses: $", total_expenses)
# Display the remaining balance after expenses
print("Remaining Balance: $", balance)

# Check if balance is positive (user has money left over)
if balance > 0:
    print("Good job! You are within your budget.")
# Check if balance is exactly zero (all income used)
elif balance == 0:
    print("You used all of your income exactly.")
# Otherwise balance is negative (user overspent)
else:
    print("Warning: You are over budget.")
