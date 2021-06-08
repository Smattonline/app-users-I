import csv
import os.path

class User:
    def __init__(self, name):
        self.name = name
    
    def signup(self, signup_info):
        self.signup_data = signup_info
        return self.signup_data

    def save(self):
        output = []
        for each_person in self.signup_data:
            output.append([each_person.name, each_person.email, each_person.phone, each_person.drivers_licence, each_person.city, each_person.state, each_person.zipcode])
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, "../data/infor_store.csv")

        with open(path, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['name','email','phone','drivers_licence','city','state','zipcode'])
            csvwriter.writerows(output)

        return output

