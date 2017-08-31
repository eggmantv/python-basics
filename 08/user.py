"""User class test"""

class User:

    def __init__(self, name):
        self.name = name

    def hi(self):
        print("hello ", self.name)

    def __hello(self):
        self.hi()


user = User('eggman.tv')
user.hi()
user.__hello() # exception
