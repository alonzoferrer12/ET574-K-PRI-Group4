income = float(input("Enter your monthly income: "))

rent = float(input("Enter rent amount: "))
food = float(input("Enter food amount: "))
transportation = float(input("Enter transportation amount: "))
entertainment = float(input("Enter entertainment amount: "))
other = float(input("Enter other expenses amount: "))

total_expenses = rent + food + transportation + entertainment + other
balance = income - total_expenses

print("\n--- Budget Summary ---")
print("Income: $", income)
print("Total Expenses: $", total_expenses)
print("Remaining Balance: $", balance)

if balance > 0:
    print("Good job! You are within your budget.")
elif balance == 0:
    print("You used all of your income exactly.")
else:
    print("Warning: You are over budget.")
