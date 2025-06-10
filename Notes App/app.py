from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    with sqlite3.connect('notes.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
        ''')

@app.route('/')
def index():
    with sqlite3.connect('notes.db') as conn:
        notes = conn.execute('SELECT * FROM notes').fetchall()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        with sqlite3.connect('notes.db') as conn:
            conn.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
        return redirect('/')
    return render_template('add_note.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
