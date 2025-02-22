from app.models.game import Game
from app.models.team import Team

team1 = Team("Equipe 1", ["M4TH's", "O Lendario Menino Brazo", "JPSena12"])
team2 = Team("Equipe 2", ["Edumundo2566", "UchihaL2", "Tales"])

game = Game(team1, team2)

def add_points(team, points):
    game.add_points(team, points)
    return game.check_winner()

def reset_game():
    game.reset_game()

def update_members(team, members):
    if team == 1:
        game.team1.update_members(members)
    else:
        game.team2.update_members(members)