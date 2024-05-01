from abc import abstractmethod, ABC
import pprint
import re


class Chess():
    board = []

    def initialize(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        # Pawn
        self.board[6] = [Pawn("P", "w", x, 2) for x in range(1, 9)]
        self.board[1] = [Pawn("P", "b", x, 7) for x in range(1, 9)]
        # Rook

        pprint.pprint(self.board)

    def print(self):
        pass
        # create default board here


class Piece(ABC):
    name = ""
    color = ""
    x = 0
    y = 0

    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.x = x
        self.y = y

    def __repr__(self):
        return self.name + self.color

    # ???????
    @abstractmethod
    def move(self, x, y):
        pass
    # create your abstract methods here


# in these classes implement method that you abstracted in Piece  class
class Pawn(Piece):
    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)

    def move(self, x, y):
        pass


class Rook(Piece):
    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)

    def move(self, x, y):
        pass


class Knight(Piece):
    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)

    def move(self, x, y):
        pass


class Bishop(Piece):
    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)

    def move(self, x, y):
        pass


class Queen(Piece):
    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)

    def move(self, x, y):
        pass


class King(Piece):
    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)

    def move(self, x, y):
        pass


class User():
    username: str = ""
    password: str = ""
    users: list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username
        elif isinstance(other, str):
            return self.username == other

    @staticmethod
    # in static we dont use self
    def register(username, password):

        if not username.isascii():
            print("username format is invalid")
            return

        if not password.isascii():
            print("password format is invalid")
            return

        if re.findall(r"\W", username):
            print("username format is invalid")

        if re.findall(r"\W", password):
            print("password format is invalid")


        u1 = User(username, password)
        if u1 in User.users :
            print("exist")
            return
        User.users.append(u1)
        print("register successful")


Chess().initialize()
User.register("hesam", "124")
User.register("hesam", "124")
User.register("alireza12", "124alireza")
User.register("alireza12", "124alireza")
User.register("alireza12", "124alireza")
User.register("alireza12dشسیشس", "124alireza")
