print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n"))
tip = float(input("How much tip in percents would you like to give?\n"))
amount_of_people = int(input("How many people to split the bill?\n"))
owed_per_person = (total_bill/amount_of_people)*(1+tip/100)
formatted_final_result = "{:.2f}".format(owed_per_person)
print(f"Each person should pay: ${formatted_final_result}")
