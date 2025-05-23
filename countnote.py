# Taking total amount as input from user
amount = int(input("Please enter amount for withdraw : "))

# Calculating the number of notes of different denominators
note_1 = int(input("Select note : "))
note_2 = int(input("Select note : "))
note_3 = int(input("Select note : "))

kosto1 = amount//note_1
kosto2 = (amount%note_1)//note_2
kosto3 = ((amount%note_1)%note_2)//note_3

print("Notes of ", note_1, ",", kosto1)
print("Notes of ", note_2, ",", kosto2)
print("Notes of ", note_3, ",", kosto3)