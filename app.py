from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# SQLite Database Configuration
DATABASE = 'NFLSeasonTracker.db'

def get_db():
    db = getattr(app, '_database', None)
    if db is None:
        db = app._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(app, '_database', None)
    if db is not None:
        db.close()

# Routes
@app.route('/')
def index():
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM Game")
    games = cur.fetchall()
    con.close()
    game_to_edit = None  # Add this line to initialize game_to_edit
    game_to_delete = None  # Add this line to initialize game_to_delete
    return render_template('index.html', games=games, game_to_edit=game_to_edit, game_to_delete=game_to_delete)

@app.route('/add_game', methods=['POST'])
def add_game():
    if request.method == 'POST':
        home_team = request.form['home_team']
        away_team = request.form['away_team']
        winner = request.form['winner']
        date_played = request.form['date_played']
        week_number = request.form['week_number']
        
        con = get_db()
        cur = con.cursor()
        cur.execute("INSERT INTO Game (home_team, away_team, winner, date_played, week_number) VALUES (?, ?, ?, ?, ?)",
                    (home_team, away_team, winner, date_played, week_number))
        con.commit()
        con.close()
        flash('Game added successfully', 'success')
        return redirect(url_for('index'))

def edit_game(game_id):
    if request.method == 'POST':
        # Extract form data and update the selected game
        con = get_db()
        cur = con.cursor()
        # Update the game using SQL UPDATE statement
        # Handle the form submission for updating the game
        home_team = request.form['home_team']
        away_team = request.form['away_team']
        winner = request.form['winner']
        date_played = request.form['date_played']
        week_number = request.form['week_number']

        # Update the game using SQL UPDATE statement
        cur.execute("UPDATE Games SET home_team=?, away_team=?, winner=?, date_played=?, week_number=? WHERE game_id=?",
                    (home_team, away_team, winner, date_played, week_number, game_id))
        con.commit()
        con.close()
        flash('Game updated successfully', 'success')
        return redirect(url_for('index'))
    
@app.route('/delete_game/<int:game_id>', methods=['POST'])
def delete_game(game_id):
    if request.method == 'POST':
        con = get_db()
        cur = con.cursor()
        cur.execute("DELETE FROM Game WHERE game_id=?", (game_id,))
        con.commit()
        con.close()
        flash('Game deleted successfully', 'success')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)