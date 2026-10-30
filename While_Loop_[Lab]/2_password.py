username = str(input())
password = str(input())
new_password = str(input())

while new_password != password:
    new_password = str(input())

print(f"Welcome {username}!")