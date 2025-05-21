import os
import time
import sqlite3

# Code Smell: hardcoded credentials
USERNAME = "admin"
PASSWORD = "admin123"

# Bug: unused variable
temporary_value = 42

# Duplication: aynı fonksiyon iki kere benzer şekilde tanımlanmış
def greet_user(user):
    if user == "admin":
        print("Welcome admin")
    elif user == "guest":
        print("Welcome guest")
    else:
        print("Access denied")

def greet_user_copy(user):
    if user == "admin":
        print("Welcome admin")
    elif user == "guest":
        print("Welcome guest")
    else:
        print("Access denied")

# Code Smell: long function with multiple responsibilities
def handle_login_and_data(user, password):
    # check login
    if user == USERNAME and password == PASSWORD:
        print("Login successful")
    else:
        print("Login failed")
        return

    # process data
    print("Processing data...")
    time.sleep(1)  # Code smell: sleep in production code
    print("Data processed.")

    # Security Hotspot: system command
    if user == "admin":
        os.system("echo 'Admin accessed system'")

# Bug: catching broad exception without handling
def read_file(path):
    try:
        with open(path, 'r') as f:
            content = f.read()
            return content
    except:
        pass  # Bug: silently swallowing errors

# Vulnerability: unvalidated file delete
def delete_file(filename):
    os.remove(filename)

# Security Hotspot: eval used on user input
def dangerous_eval(data):
    result = eval(data)
    print(result)

# Vulnerability: naive SQL injection example
def login_db(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # ⚠️ Vulnerable query
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user

# Main logic
if __name__ == "__main__":
    users = ["admin", "guest", "user1"]
    
    for user in users:
        greet_user(user)

    greet_user_copy("admin")

    handle_login_and_data("admin", "admin123")
    
    print(read_file("missing_file.txt"))  # Will cause exception

    delete_file("important_data.txt")  # Risk: file can be deleted without check

    dangerous_eval("2 + 2")  # eval used

    login_db("admin", "1234")  # SQL injection risk
