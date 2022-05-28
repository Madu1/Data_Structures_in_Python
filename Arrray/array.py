# Exercise 1
expences = [2200, 2350, 2600, 2130, 2190]

income_j = expences[0]
income_f = expences[1]
extra_income = income_f - income_j
print(extra_income)

# Loop
for i in range(len(expences)):
    if i == 0:
        income_1 = expences[i]
    if i == 1:
        income_2 = expences[i]
ex_income = income_2 - income_1

print(f"Extra Income: ${ex_income}")

# Total Income of first quarter
total_expence =0
for j in range(len(expences)):
    total_expence += expences[j]
    if j  == 2:
        break

print(f"Total income of first quarter: ${total_expence}")

# Find out if you spent exactly 2000 dollars in any month
for a in range(len(expences)):
    if expences[a] == 2000:
        print("You have spent $2000")
        break
    else:
        print("You don't have spent $2000")
        break

# Add 1980 to 5th position
expences.append(1980)
print(expences)

# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

total_expences = 0
for c in range(len(expences)):
    if c == 3:
        new_expense_April = expences[3] - 200
        expences[c] = new_expense_April

    total_expences += expences[c]

print(expences)
print(f"Updated total expenses: ${total_expences}")
