class UserName:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname

    def user_name(self):
        print(f"{self.fname} {self.lname}")


first_name = input("Enter the first name:")
last_name = input("Enter the last name:")
obj=UserName(first_name, last_name)
obj.user_name()

