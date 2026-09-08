# Thinking process:

# Ek correct password store karo (jaise correct_password = "secure123")
# Ek counter rakho attempts ginne ke liye
# Loop chalao jab tak attempts 3 se kam hain
# Har baar user se password pucho, check karo sahi hai ya nahi
# Sahi ho toh "Access Granted" print karke loop rok do
# 3 baar galat ho toh "Account Locked" print karo

correct_password="secure@123"
attempts=0
max_attempts=3

while attempts < max_attempts:
    user=input("enter a password: ")
    if user==correct_password:
        print("Access Granted!")
        break
    else:
        attempts =attempts + 1 
        print(f"Incorrect password. You have {max_attempts - attempts} attempts left.")

if attempts == max_attempts:
    print("Account Locked. Too many failed attempts.")