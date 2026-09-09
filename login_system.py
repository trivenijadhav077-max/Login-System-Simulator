
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
