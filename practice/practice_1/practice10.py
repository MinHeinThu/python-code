class User:
    def __init__(self, name, password):
        self._name = name
        self._password = password
        # self._store = {1: self._name}

    def access(self,password):
        if password == self._password:
            self._name = (input("Update your name: "))
            return
        else:
            print("You are not allow to update name")

    def show_detail(self):
        # print(self._store[1])
        print(f"Name: {self._name}")


user = User("Joli", 445)
user.show_detail()
user.access(445)
user.show_detail()

class OldUser(User):
    def __init__(self, name, password):
        super().__init__(name, password)

old_user = OldUser("Min", 2234)
old_user.show_detail()
