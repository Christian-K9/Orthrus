#pip install mariadb

import mariadb
import getpass
import subprocess

#connect to database

password = getpass.getpass("Password For Alert User")
conn = mariadb.connect(
    user="alerts_user",
    password = password,
    host="127.0.0.1",
    database="my_database"
)

cursor = conn.cursor()

cursor.execute("SHOW TABLES")

tables = cursor.fetchall()

print("Tables:")

for table in tables:
    print(table[0])

#Values:
#   message
#   host    
#   user
#   ip_address
#   port

#functions to search by value
def search_by_field(field_name):
    value = input(f"{field_name} To Search By: ")

    query = f"SELECT * FROM alerts WHERE {field_name} LIKE ?"
    cursor.execute(query, (f"%{value}%",))

    results = cursor.fetchall()
    for row in results:
        print(row)

#remove items
def remove_item():
    item = input("Item To Remove (Search By ID): ")

    cursor.execute("DELETE FROM alerts WHERE id = ?", (item,))
    conn.commit()

    print("Item removed (if it existed).")

#emulator
while True:
    print("1.   Search Message By Keyword")
    print("2.   Search By Hostname")
    print("3.   Search By Username")
    print("4.   Search By IP Address")
    print("5.   Search By Port Number")
    print("6.   Remove Item By ID")
    print("Ctrl + C: Quit")
    option = input("Enter Function To Choose From: ")
    
    if option == "1":
        search_by_field("message")
    elif option == "2":
        search_by_field("host")
    elif option == "3":
        search_by_field("user")
    elif option == "4":
        search_by_field("ip_address")
    elif option == "5":
        search_by_field("port")
    elif option == "6":
        remove_item()
    

