print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_total = (tip/100) + 1

print(tip_total)

split = ((bill * tip_total) / people)

pay_per_person = round(split, 2)

print(pay_per_person)

print(f"Each person should pay: {pay_per_person:.2f}")