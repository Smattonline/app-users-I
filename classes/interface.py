from classes.user import User
import csv
import os.path

class Record:
    def __init__(self, name):
        self.name = name
        self.users = []
        
    def list_of_user(self, signup_info):
        self.users.append(User(**signup_info))
        self.save()
    
    def user_profile(self, signin_phone):
        res = dict((phone, self.users[phone]) for phone in [self.users] if phone in self.users)
        return str(res)

    def save(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/info_store.csv")

        with open(path, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['name','email','phone','drivers_licence','city','state','zipcode'])
            for each_person in self.users:
                output = [each_person.name, each_person.email, each_person.phone, each_person.drivers_licence, each_person.city, each_person.state, each_person.zipcode]
                csvwriter.writerow(output)

        return output
       