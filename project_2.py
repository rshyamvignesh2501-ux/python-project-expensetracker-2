expense = 0.0
budget = 0.0
difference = 0.0
expenseTotal = 0.0

total_expense = 0
keep_going = 'y'


budget = float(input("enter budget of this month:"))
print("Please begin entering budgets of each of your monthly expenses:")

while keep_going == 'y':
    expense = float(input("Monthly expense amount?$ "))
    total_expense = total_expense + expense
    keep_going = input("Do you have any other expenses? (Enter y for yes.)")

if expense < budget:
    difference = budget - expense
    print("You were $", difference, " under budget.")

elif expense > budget:
    difference = expense - budget
    print("You were $", difference, " over budget.")

else:
    print("You were right on budget. Great Job!!!")


input("Press enter to exit.")