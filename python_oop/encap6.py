class GmailAccount:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def change_password(self, old_pass, new_pass):
        if self.__password == old_pass:
            self.__password = new_pass
            return True
        else:
            return False
    def get_email(self):
        return self.__email
    

acc = GmailAccount("hello@gmail.com",1123)

print(acc.change_password(1123, 8852))

print(acc.get_email())
