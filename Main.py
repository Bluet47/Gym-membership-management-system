from admin import Admin
from member import MemberLogin
import os
import time

def main():
    while True:
        os.system('clear')
        print(" Welcome to CLEAN GYM")
        print("1. Member Login")
        print("2. Admin Login")
        print("3. Member Sign Up")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            MemberLogin().login()
        elif choice == "2":
            Admin().admin_login()
        elif choice == "3":
            MemberLogin().sign_up()
        elif choice == "4":
            print("Exiting System...")
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(2)

if __name__ == "__main__":
    main()
