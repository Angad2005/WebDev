import sqlite3
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute("SELECT username, password FROM users")
users = cursor.fetchall()
print("\nRegistered Users:")
for user in users:
    print(f"Username: {user[0]}, Password: {user[1]}")
conn.close()