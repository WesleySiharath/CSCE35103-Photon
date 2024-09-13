import mysql.connector
#Installed MYSQL Created a server using base not sure if the local host will be carried over in vm.
def add_player(player_id, codename):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='Main',
            password='coolkid69',
            database='photon_db'
        )

        cursor = connection.cursor()

        #check if playerid already in db
        sql_select_Query = "select * from players;"
        cursor.execute(sql_select_Query)
        players_temp = cursor.fetchall()
        for row in players_temp:
            if player_id == row[0]:
                print(f"Error: womp womp, same id", row[0])    

        insert_query = "INSERT INTO players (id, codename) VALUES (%s, %s)"
        values = (player_id, codename)
        cursor.execute(insert_query, values)
        connection.commit()
        print(f"Player {codename} added successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def list_players():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='Main',
            password='coolkid69',
            database='photon_db'
        )
        cursor = connection.cursor()
        select_query = "SELECT * FROM players"
        cursor.execute(select_query)
        results = cursor.fetchall()
        for player in results:
            print(player)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

add_player(2, 'John')
add_player(3, 'West')
list_players()
