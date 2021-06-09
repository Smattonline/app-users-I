from classes.user import User
from classes.interface import Record

record = Record('Students App')

while True:
    begin = int(input("\n\nWelcome to the Student App! Please, signup to get started\n\n1. Signup\n2. Sign-in\n3. Exit\n"))

    if begin == 1:
        signup_info = {}
        signup_info['name'] = input("Enter first and last name: ")
        signup_info['email'] = input("Enter email address: ")
        signup_info['phone'] = int(input("Enter phone number: "))
        signup_info['drivers_licence'] = int(input("Enter driver's licence number: "))
        signup_info['city'] = input("Enter city: ")
        signup_info['state'] = input("Enter state: ")
        signup_info['zipcode'] = input("Enter zipcode: ")
        print("Thanks for signing up!")
        record.list_of_user(signup_info)
    elif begin == 2:
        signin_phone = int(input('Enter your phone number: '))
        User_Profile = record.user_profile(signin_phone)
        print(str(User_Profile))
    elif begin == 3:
        break
    else:
        print("Please, enter '1' to signup!")

