age = input("What is your current age?")

remaining_age = 90 - int(age)
remaining_mon = remaining_age * 12
remaining_weeks = remaining_age * 52
remaining_days = remaining_age * 365

print(f"You have {remaining_days} days, {remaining_weeks} weeks,  {remaining_mon} months and {remaining_age} years left.")
