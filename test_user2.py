class User:
    username = ""
    password = ""
    users = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username
        elif isinstance(other, str):
            return self.username == other

    @staticmethod
    def is_username_exists(username):
        if username in User.users:
            print("found")
        else:
            print('not found')


User.users.append(User("ali", "1234"))
User.users.append(User("reza", "1234"))
User.users.append(User("ahmad", "1234"))

u1 = User("ali", "1234")
u2 = User("reza", "1234")
u3 = User("ali", "12345")
print(u1 == u2)
print(u1 == u3)
print(u2 == u3)
un = input()
if User(un, "") in User.users:
    print("found")
else:
    print('not found')
if un in User.users:
    print("found")
else:
    print('not found')