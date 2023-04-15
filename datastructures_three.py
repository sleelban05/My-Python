# Start by asking the numbers the user has
numbers = input("How numbers do you have?\n")
# Conver the number to integer
numbers = int(numbers)
# Ask the user to enter the numbers
print("Enter the", numbers, "betting_numbers")
# prepare an empty list to receive the numbers
betting_number = []
# Write a loop to receive the numbers one by one
counter = 0
while counter < numbers:
    betting_number.append(input())
    counter += 1
# Ask the user to give the number he/she wants to bet with
picked_number = input("Enter the number you wish to bet with\n")
# Check if the number exists on the list of numbers received
# Write a loop to navigate through the list as you check
for nambari in betting_number:
    if nambari == picked_number:
        print("Congrats!!! You won")
        break
