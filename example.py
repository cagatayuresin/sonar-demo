# example.py

import os
import time

# Code Smell: hardcoded password
USERNAME = "admin"
PASSWORD = "123456"

# Bug: unused variable
x = 42

# Code Smell: long function
def process_data(users):
    for user in users:
        print(f"Processing {user}")
        time.sleep(1)
        if user == "admin":
            print("Full Access")
        else:
            print("Restricted")

# Vulnerability: unvalidated input
def delete_file(filename):
    os.remove(filename)

# Security Hotspot
def execute(cmd):
    eval(cmd)

# Run
if __name__ == "__main__":
    users = ["admin", "guest"]
    process_data(users)
    delete_file("test.txt")
    execute("print('Demo')")
