from database import execute_query, fetch_one
from utils import hash_password, verify_password

class MemberLogin:
    def login(self):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        row = fetch_one("SELECT Password FROM Login WHERE Username = ?", (username,))
        if row and verify_password(password, row[0]):
            print("Login successful!")
        else:
            print("Invalid credentials.")

    def sign_up(self):
        print("Enter new member details:")
        fname = input("First Name: ").strip()
        lname = input("Surname: ").strip()
        phone = input("Phone Number: ").strip()
        mtype = input("Membership Type (Gold/Silver): ").strip()
        act1 = input("Activity 1: ").strip()
        act2 = input("Activity 2 (optional): ").strip()
        act3 = input("Activity 3 (optional): ").strip()
        password = input("Set your password: ").strip()
        username = fname + phone[-3:]

        execute_query("""
            INSERT INTO Member (FirstName, Surname, PhoneNumber, MembershipType, Activity1, Activity2, Activity3)
            VALUES (?, ?, ?, ?, ?, ?, ?)""", (fname, lname, phone, mtype, act1, act2 or None, act3 or None))

        member_id = fetch_one("SELECT MembershipNo FROM Member WHERE PhoneNumber = ?", (phone,))
        if member_id:
            execute_query("INSERT INTO Login (MembershipNo, Username, Password) VALUES (?, ?, ?)",
                          (member_id[0], username, hash_password(password)))
            print(f"Signup successful! Your username is {username}")
        else:
            print("Signup failed.")
