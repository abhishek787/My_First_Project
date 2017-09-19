import re

# creating class to store spy data

class Spy:
    spy = None

    # init method
    def __init__(self):
        self.name = None
        self.age = None
        self.rating = None
        self.is_online = False

    # setter method
    def setDetail(self, name = "Bond", age = 30, rating = 3.5):
        self.name = name
        self.age = age
        self.rating = rating
        self.is_online = True
        Spy.spy = self

    # showing data to user
    def showDetail(self):
        print "Name : {} \nAge : {} \nRating : {}".format(self.name, self.age, self.rating)

    def get_user_info(self, string):
        name = raw_input("Provide {} Name here : ".format(string))

        if not re.match(r"^[a-zA-Z ]+$", name):
            print "Invalid Name . Provide correct details."
            return False

        salutation = raw_input(" Mr. or Ms.?: :")
        if salutation.capitalize() == "Mr" or salutation.capitalize() == "Ms":
            salutation = salutation + "."
        elif salutation.capitalize() == "Mr." or salutation.capitalize() == "Ms.":
            pass
        else:
            print "Enter correct salutation "
            return False

        age = raw_input("Enter {} Age : ".format(string))

        if not re.match(r"^[2-4]\d|1[2-9]|50$", age):
            print "Invalid age .Provide correct details."
            return False
        age = int(age)

        rating = raw_input("What {} Rating ? : ".format(string))

        if not re.match("^[1-4]\.\d*|[0]\.[1-9]*|5\.0*|[1-5]$", rating):
            print "Invalid rating .Provide correct details."
            return False
        rating = float(rating)
        name = name.capitalize()
        salutation = salutation.capitalize()
        name = "{0} {1}".format(salutation, name)

        self.setDetail(name,age,rating)
        return True
