import os

class A:
    def __init__(self, uname, pwd):
        self.uname = uname
        self.pwd = pwd
    
    def print_all(self):
        print(f"my username is {self.uname}, password is {self.pwd}")
print(os.environ)
print("-"*40)
username = os.getenv("USERNAME")
print(username)
password = os.getenv("PASSWORD")
print(password)
print("-"*40)
a = A(username, password)
a.print_all()
