import sqlite3

def create_connection():
    conn = sqlite3.connect('football_team.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS players
                      (id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      position TEXT NOT NULL,
                      number INTEGER NOT NULL,
                      age INTEGER NOT NULL,
                      status TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS fixtures
                      (id INTEGER PRIMARY KEY,
                      date TEXT NOT NULL,
                      opponent TEXT NOT NULL,
                      venue TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS team_selection
                      (fixture_id INTEGER,
                      player_id INTEGER,
                      is_substitute BOOLEAN,
                      FOREIGN KEY(fixture_id) REFERENCES fixtures(id),
                      FOREIGN KEY(player_id) REFERENCES players(id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS captains
                      (priority INTEGER NOT NULL,
                      player_id INTEGER NOT NULL,
                      FOREIGN KEY(player_id) REFERENCES players(id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS roles
                      (role TEXT NOT NULL,
                      player_id INTEGER NOT NULL,
                      FOREIGN KEY(player_id) REFERENCES players(id))''')
    conn.commit()
    conn.close()

def add_player(name, position, number, age, status):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO players (name, position, number, age, status) VALUES (?, ?, ?, ?, ?)',
                   (name, position, number, age, status))
    conn.commit()
    conn.close()

def get_all_players():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM players')
    players = cursor.fetchall()
    conn.close()
    return players

def update_player(id, name, position, number, age, status):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE players SET name = ?, position = ?, number = ?, age = ?, status = ? WHERE id = ?',
                   (name, position, number, age, status, id))
    conn.commit()
    conn.close()

def delete_player(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM players WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def add_fixture(date, opponent, venue):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO fixtures (date, opponent, venue) VALUES (?, ?, ?)',
                   (date, opponent, venue))
    conn.commit()
    conn.close()

def get_all_fixtures():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM fixtures')
    fixtures = cursor.fetchall()
    conn.close()
    return fixtures

def add_team_selection(fixture_id, player_id, is_substitute):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO team_selection (fixture_id, player_id, is_substitute) VALUES (?, ?, ?)',
                   (fixture_id, player_id, is_substitute))
    conn.commit()
    conn.close()

def get_team_selection(fixture_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM team_selection WHERE fixture_id = ?', (fixture_id,))
    team_selection = cursor.fetchall()
    conn.close()
    return team_selection

def add_captain(priority, player_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO captains (priority, player_id) VALUES (?, ?)',
                   (priority, player_id))
    conn.commit()
    conn.close()

def get_captains():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM captains')
    captains = cursor.fetchall()
    conn.close()
    return captains

def add_role(role, player_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO roles (role, player_id) VALUES (?, ?)',
                   (role, player_id))
    conn.commit()
    conn.close()

def get_roles():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM roles')
    roles = cursor.fetchall()
    conn.close()
    return roles
