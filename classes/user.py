import csv
import os.path

class User:
    def __init__(self, name, email,phone,drivers_licence,city,state,zipcode):
        self.name = name
        self.email = email
        self.phone = phone
        self.drivers_licence = drivers_licence
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        return f'Welcome {self.name}!\n.....................\nAddress: {self.city}, {self.state} {self.zipcode}\n'

    @classmethod
    def objects(cls):
        user_obj = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/info_store.csv")

        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user_obj.append(User(**dict(row)))
        return user_obj
    