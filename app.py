from flask import Flask, render_template, request, redirect, url_for
from app.controllers.game_controller import add_points, reset_game, update_members, game

app = Flask(__name__, template_folder='app/views/templates', static_folder='app/static')

@app.route('/')
def index():
    return render_template('index.html', team1=game.team1, team2=game.team2)

@app.route('/add_points', methods=['POST'])
def add():
    team = int(request.form['team'])
    points = int(request.form['points'])
    winner = add_points(team, points)

    if winner:
        return render_template('index.html', team1=game.team1, team2=game.team2, winner=winner)
    
    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    reset_game()
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    team = int(request.form['team'])
    members = [request.form['member1'], request.form['member2'], request.form['member3']]

    update_members(team, members)
    return redirect(url_for('index'))

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)