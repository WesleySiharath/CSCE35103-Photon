import psycopg2
import python_udpclient

# Always try to connect to database
try:
    # Connect to local database
    conn = psycopg2.connect(
            host='localhost',
            database="photon-db",
            user='postgres',
            password='')
except psycopg2.Error as err:
        print(f"Error: {err}")


# Add new players into db
def add_player(player_id, codename):
    # Open a cursor to perform database operations  
    cur = conn.cursor()

    # Get players data from table 
    select_query = "SELECT * FROM players"
    cur.execute(select_query)
    players = cur.fetchall()

    # Check for duplicate players
    for player in players:
        if player_id == player[0]:
            print(f"Error: womp womp, same id:{player[0]} for player: {player[1]}")
            return None
    
    # Insert new player into player db
    cur.execute('INSERT INTO players (id, codename)'
                'VALUES (%s, %s)',
                (player_id, codename))
    
    conn.commit()

    print(f"Player {codename} added successfully!")

    cur.close()

    python_udpclient.send_equipment_code(str(player_id))


# List all players from table 
def list_players():
        # Open a cursor to perform database operations  
        cur = conn.cursor()

        # Get players data from table 
        select_query = "SELECT * FROM players"
        cur.execute(select_query)
        players = cur.fetchall()

        for player in players:
            print(player)
            
#delete a player from the table
def delete_player(player_id):
    #open a cursor to perform database operations
    try:
        cursor = conn.cursor()
    
        #check if player exists
        cursor.execute('SELECT * FROM players WHERE id = %s', (player_id))
        player = cursor.fetchone()
        
        if player is None:
            print(f"Player {player_id} doesn't exist")
            cursor.close()
            return None
        else: 
            #delete the player if they exist
            cursor.execute('DELETE FROM players WHERE id = %s', (player_id))
            conn.commit()
            
            print(f"Player {player_id} has been deleted. rip")
            
        cursor.close()
            
    except psycopg2.Error as err:
        print(f"Error: {err}")

def start_game():
    #  run Splash Screen
    #  run Player Entry Screen
    add_player(2, 'John')
    add_player(3, 'West')
    add_player(69, 'Diddy')
    list_players()
    delete_player(69)
    list_players()
    conn.close()



start_game()