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

@app.route('/add', methods=['POST'])
def add_game():
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        name = request.form['name']
        # Include additional fields for your "Games" table
        # For example, you may have fields like date, location, score, etc.

        cursor.execute('INSERT INTO Games (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()

    return redirect(url_for('display_games'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_game(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        # Include additional fields for your "Games" table
        # For example, you may have fields like date, location, score, etc.

        cursor.execute('UPDATE Games SET name = ? WHERE id = ?', (name, id))
        conn.commit()
        conn.close()
        return redirect(url_for('display_games'))

    cursor.execute('SELECT * FROM Games WHERE id = ?', (id,))
    game = cursor.fetchone()
    conn.close()

    return render_template('edit_game.html', game=game)

@app.route('/delete/<int:id>')
def delete_game(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Games WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return redirect(url_for('display_games'))
if __name__ == '__main__':
    app.run(debug=True)