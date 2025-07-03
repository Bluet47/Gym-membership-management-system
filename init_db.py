from database import execute_query

def init_db():
    member_table = """
    CREATE TABLE IF NOT EXISTS Member (
        MembershipNo INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        Surname TEXT NOT NULL,
        PhoneNumber TEXT NOT NULL UNIQUE,
        MembershipType TEXT NOT NULL,
        Activity1 TEXT,
        Activity2 TEXT,
        Activity3 TEXT
    );
    """
    activity_table = """
    CREATE TABLE IF NOT EXISTS Activity (
        ActivityNo INTEGER PRIMARY KEY AUTOINCREMENT,
        ActivityName TEXT NOT NULL UNIQUE,
        Instructor TEXT,
        Day TEXT,
        Time TEXT,
        Duration REAL NOT NULL,
        Capacity INTEGER NOT NULL,
        MaxCapacity INTEGER NOT NULL
    );
    """
    login_table = """
    CREATE TABLE IF NOT EXISTS Login (
        MembershipNo INTEGER PRIMARY KEY,
        Username TEXT UNIQUE,
        Password TEXT,
        FOREIGN KEY (MembershipNo) REFERENCES Member(MembershipNo)
    );
    """
    execute_query(member_table)
    execute_query(activity_table)
    execute_query(login_table)
    print("Database initialized.")

if __name__ == "__main__":
    init_db()
