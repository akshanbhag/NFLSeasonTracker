from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def display_data():
    conn = sqlite3.connect('NFLSeasonTracker.db')
    cursor = conn.cursor()

    # Fetch data from the database
    cursor.execute('SELECT * FROM Teams')
    data = cursor.fetchall()

    conn.close()

    return render_template('index.html', data=data)

def display_games():
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Games')
    games = cursor.fetchall()

    conn.close()

    return render_template('display_games.html', games=games, teams=get_teams())

@app.route('/add_game', methods=['POST'])
def add_game():
    if request.method == 'POST':
        home_team_id = request.form['home_team']
        away_team_id = request.form['away_team']
        winner_id = request.form['winner']
        date = request.form['date']
        week_number = request.form['week_number']

        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO Games (home_team_id, away_team_id, winner_id, date, week_number) VALUES (?, ?, ?, ?, ?)',
                       (home_team_id, away_team_id, winner_id, date, week_number))

        conn.commit()
        conn.close()

    return redirect(url_for('display_games'))

@app.route('/edit_game/<int:id>', methods=['GET', 'POST'])
def edit_game(id):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        home_team_id = request.form['home_team']
        away_team_id = request.form['away_team']
        winner_id = request.form['winner']
        date = request.form['date']
        week_number = request.form['week_number']

        cursor.execute('UPDATE Games SET home_team_id=?, away_team_id=?, winner_id=?, date=?, week_number=? WHERE id=?',
                       (home_team_id, away_team_id, winner_id, date, week_number, id))

        conn.commit()
        conn.close()

        return redirect(url_for('display_games'))

    cursor.execute('SELECT * FROM Games WHERE id = ?', (id,))
    game = cursor.fetchone()

    conn.close()

    return render_template('edit_game.html', game=game, teams=get_teams())

@app.route('/delete_game/<int:id>')
def delete_game(id):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Games WHERE id = ?', (id,))

    conn.commit()
    conn.close()

    return redirect(url_for('display_games'))

if __name__ == '__main__':
    app.run(debug=True)