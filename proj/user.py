class Authentication:
    def __init__(self, username = ''):
        self.username = username

    def __lower(self):
        lower = any(c.islower() for c in self.username)
        return lower

    def __upper(self):
        upper = any(c.isupper() for c in self.username)
        return upper

    def __digit(self):
        digit = any(c.isdigit() for c in self.username)
        return digit

    def validate(self):
        lower = self.__lower()
        upper = self.__upper()
        digit = self.__digit()

        length = len(self.username)

        report = lower and upper and digit and length >= 6

        if report:
            print("username passed all checks")
            return True

        elif not lower:
            print("you didnt use lower case letter")
            return False

        elif not upper:
            print("you didnt use upper case letter")
            return False

        elif length<6:
            print("username should atleast have six characters")
            return False

        elif not digit:
            print("you didnt use digit")
            return False
        else:
            pass

C = Authentication("Td1abcd")
print(C.validate())
