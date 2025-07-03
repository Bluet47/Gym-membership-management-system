from database import fetch_all
import time

class Admin:
    def __init__(self, username="admin", password="admin123"):
        self.__username = username
        self.__password = password

    def admin_login(self):
        attempts = 3
        while attempts > 0:
            username = input("Admin Username: ").strip()
            password = input("Admin Password: ").strip()
            if username == self.__username and password == self.__password:
                print("Login successful.")
                self.main_menu()
                return
            else:
                attempts -= 1
                print(f"Incorrect credentials. {attempts} attempt(s) left.")
                time.sleep(2)

    def main_menu(self):
        while True:
            print("""
            ADMIN MENU
            1. View All Members
            2. View All Activities
            3. Exit
            """)
            choice = input("Select an option: ").strip()
            if choice == "1":
                self.view_all("Member")
            elif choice == "2":
                self.view_all("Activity")
            elif choice == "3":
                break
            else:
                print("Invalid option.")

    def view_all(self, table):
        results = fetch_all(f"SELECT * FROM {table}")
        for row in results:
            print(row)
