# Login System
username = "ec2-user"
password = "DevOps321"

in_username = input("Please enter your username: ")
in_password = input("Please enter your_password: ")

if (in_username == username) and (in_password == password):
    print("Login is successful")
else:
    print("Please check your credentials")