class Team:

    PLAYERS_LIST = [
        "M4TH's",
        "O Lendario Menino Brazo",
        "Edumundo2566",
        "UchihaL2",
        "JPSena12",
        "Tales",
        "Pedro"
    ]

    def __init__(self, name="Equipe", members=None):
        self.name = name
        self.score = 0
        self.members = members if members else self.PLAYERS_LIST[:3]
        self.photos = [self.get_photo(m) for m in self.members]

    def add_points(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

    def update_members(self, members):
        self.members = members
        self.photos = [self.get_photo(m) for m in self.members]

    @staticmethod
    def get_photo(player_name):
        return f"{player_name.lower().replace(' ', '').replace('\'', '')}.jpg"