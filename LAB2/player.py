from datetime import datetime


class Player:
    def __init__(self, nickname, email, date_of_birth, xp, cls):
        self.nickname = nickname
        self.email = email
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        self.xp = xp
        self.cls = cls

    def __repr__(self):
        return f"<Player[nickname = {self.nickname}]>"