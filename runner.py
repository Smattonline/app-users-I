from classes.user import User

user = User('Students App')

while True:
    begin = int(input("\n\nWelcome to the Student App! Please, signup to get started\n\n1. Signup\n"))

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
        User.signup(signup_info)
    else:
        print("Please, enter '1' to signup!")

