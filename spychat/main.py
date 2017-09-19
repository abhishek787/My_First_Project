# importng modules

from spy import Spy
from start_chat import start_chat

# only call by main
if __name__ == "__main__":
    print "Let's get started"
    # want to know user choice about login
    choice = raw_input('You want to start as guest Y/N : ')

    obj = Spy()

    if choice == "y" or choice == "Y":
        # getting guest user data
        # setting user data
        obj.setDetail()

    elif choice == "n" or choice == "N":
        # getting user data
        info = obj.get_user_info("your")
        # checking for error
        if info is False:
            print "Error in getting spy detail"
            exit(-1)

    else:
        print "Wrong Input"
        exit(-1)

    print "Authentication complete. Welcome"
    obj.showDetail()
    print "Proud to have you onboard"

    # sending to start chat for further execution
    start_chat()
