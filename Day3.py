# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

T_count = 0
R_count = 0
U_count = 0
E_count = 0
total_true = 0

L_count = 0
O_count = 0
V_count = 0
total_love = 0

T_count += name1.lower().count("t")
T_count += name2.lower().count("t")
R_count += name1.lower().count("r")
R_count += name2.lower().count("r")
U_count += name1.lower().count("u")
U_count += name2.lower().count("u")
E_count += name1.lower().count("e")
E_count += name2.lower().count("e")

L_count += name1.lower().count("l")
L_count += name2.lower().count("l")
O_count += name1.lower().count("o")
O_count += name2.lower().count("o")
V_count += name1.lower().count("v")
V_count += name2.lower().count("v")
total_true = T_count + R_count + U_count + E_count
total_love = L_count + O_count + V_count + E_count
print(f"T occurs {T_count} times")
print(f"R occurs {R_count} times")
print(f"U occurs {U_count} times")
print(f"E occurs {E_count} times")
print(f"Total = {total_true}")

print(f"L occurs {L_count} times")
print(f"O occurs {O_count} times")
print(f"V occurs {V_count} times")
print(f"E occurs {E_count} times")
print(f"Total = {total_love}")

print(f"Love Score = {total_true}{total_love}")



