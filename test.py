import os

print(os.environ)
print("-"*40)
username = os.getenv("USERNAME")
print(username)
password = os.getenv("PASSWORD")
print(password)
print("-"*40)
