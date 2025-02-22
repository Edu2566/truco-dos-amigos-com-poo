class Game:
    def __init__(self, team1, team2, points_to_win=12):
        self.team1 = team1
        self.team2 = team2
        self.points_to_win = points_to_win

    def add_points(self, team, points):
        if team == 1:
            self.team1.add_points(points)
        else:
            self.team2.add_points(points)

    def reset_game(self):
        self.team1.reset_score()
        self.team2.reset_score()

    def check_winner(self):
        if self.team1.score >= self.points_to_win:
            return f"{self.team1.name} venceu!"
        elif self.team2.score >= self.points_to_win:
            return f"{self.team2.name} venceu!"
        else:
            return None