import psycopg2
import socket

msgFromClient       = ""
serverAddressPort   = ("127.0.0.1", 7501)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


def send_code(code):
    msgFromClient = str(code)
    bytesToSend = str.encode(msgFromClient)
    
    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    
    if code != 221:
        msgFromServer = (UDPClientSocket.recvfrom(bufferSize)[0]).decode("utf-8")
        msg = f"Message from Server: \"{msgFromServer}\""
        print(msg)
    

# Always try to connect to database
try:
    # Connect to local database
    conn = psycopg2.connect(
            host='localhost',
            # update user, password, database for virtual machine (student, student, photon) user for Mac is postgres
            database='photon-db',
            user='postgres',
            password='')
except psycopg2.Error as err:
        print(f"Error: {err}")


# Add new players into db
def add_player(player_id, codename):
    # if player id  doesn't exists
    if not player_id:
        return False
    
    #make sure player id and equipment code is an int
    try:
        player_id = int(player_id)
    except ValueError:
        # print(f"Nuh uh: {player_id} is not a valid integer")
        return False
    
    codename = str(codename)

    # Open a cursor to perform database operations  
    cur = conn.cursor()

    # Get players data from table 
    select_query = "SELECT * FROM players"
    cur.execute(select_query)
    players = cur.fetchall()

    # Check for duplicate players
    for player in players:
        if player_id == player[0]:
            # print(f"Error: womp womp, same id:{player[0]} for player: {player[1]}")
            return player[1]
        
    # exit if codename doesn't exists
    if not codename:
        return False
    
    # Insert new player into player db
    cur.execute('INSERT INTO players (id, codename)'
                'VALUES (%s, %s)',
                (player_id, codename))
    
    conn.commit()

    print(f"Player {codename} added successfully!")

    cur.close()
    
    return True

# Clear server table
def clearEntries():
    try:
        #open connection
        cur = conn.cursor()

        #delete all
        cur.execute("DELETE FROM players")
        conn.commit()

        print("Rest in piece; all player deleted")
        
        cur.close()
        
    except psycopg2.Error as err:
        print(f"womp womp: {err}")

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
        cursor.execute(f'SELECT * FROM players WHERE id = {player_id}')
        player = cursor.fetchone()
        
        if player is None:
            print(f"Player {player_id} doesn't exist")
            cursor.close()
            return None
        else: 
            #delete the player if they exist
            cursor.execute(f'DELETE FROM players WHERE id = {player_id}')
            conn.commit()
            
            print(f"Player {player_id} has been deleted. rip")
            
        cursor.close()
            
    except psycopg2.Error as err:
        print(f"Error: {err}")

def start_game():
    list_players()



start_game()