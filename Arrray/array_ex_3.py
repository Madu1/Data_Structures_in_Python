# Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user
# using input() function
max_num = int(input("Enter the maximum number: "))
odd_num = []

for i in range(max_num):
    if i % 2 == 1:
        odd_num.append(i)

print(odd_num)


