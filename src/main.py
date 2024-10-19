import server
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk

def Splash():
    try:
        screen_width = splash.winfo_screenwidth()
        screen_height = splash.winfo_screenheight()
        img = Image.open("../assets/logo.jpg")  
        img = img.resize((screen_width, screen_height), Image.LANCZOS)  
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(splash, image=photo)
        label.image = photo 
        label.pack()
        splash.after(3000, teamRegistration) 
    except Exception as e:
        print(f"Error loading image: {e}")

def teamRegistration():
    #initialize lists
    redEntries = []
    blueEntries = []
    
    print("Transitioning to team registration...")
    splash.destroy() 

    registration = tk.Tk() 
    registration.title("Team Registration")
    registration.attributes('-fullscreen', True)  
    registration.configure(bg="#d3d3d3")

    # Red Team Table
    redFrame = tk.Frame(registration, borderwidth=2, relief="solid", bg="#981A2B")
    redFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Title
    tk.Label(redFrame, text="Red Team", font=("Courier New", 24), bg="#d3d3d3", fg="black").pack(pady=10)

    # Input Fields
    for _ in range(15): 
        rowFrame = tk.Frame(redFrame, bg="#BA1F33")
        rowFrame.pack(pady=5)

        tk.Label(rowFrame, text="ID:", bg="White").pack(side=tk.LEFT, padx=5)
        idInput = tk.Entry(rowFrame, width=10)
        idInput.pack(side=tk.LEFT, padx=5)
        
        tk.Label(rowFrame, text="Name", bg="White").pack(side=tk.LEFT, padx=5)
        nameInput = tk.Entry(rowFrame, width=20)
        nameInput.pack(side=tk.LEFT, padx=5)

        tk.Label(rowFrame, text="Equipment ID:", bg="White").pack(side=tk.LEFT, padx=5)
        equipmentIdInput = tk.Entry(rowFrame, width=10)
        equipmentIdInput.pack(side=tk.LEFT, padx=5)

        redEntries.append({'id': idInput, 'name': nameInput, 'equipment_id': equipmentIdInput, 'state': "normal"})  # Save references to the entry widgets

    # Submit Button  
    submitRed = tk.Button(redFrame, text="Submit Red Team", command=lambda: submitPlayers(redEntries, "Red Team"), bg="black", fg="white")
    submitRed.pack(pady=10)

    # Blue Team Table
    blueFrame = tk.Frame(registration, borderwidth=2, relief="solid", bg="#1A2498")
    blueFrame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Title
    tk.Label(blueFrame, text="Blue Team", font=("Courier New", 24), bg="#d3d3d3", fg="black").pack(pady=10)

    # Input Fields
    for _ in range(15):  
        rowFrame = tk.Frame(blueFrame, bg="#4120BA")
        rowFrame.pack(pady=5)

        tk.Label(rowFrame, text="ID:", bg="White").pack(side=tk.LEFT, padx=5)
        idInput = tk.Entry(rowFrame, width=10)
        idInput.pack(side=tk.LEFT, padx=5)

        tk.Label(rowFrame, text="Name:", bg="White").pack(side=tk.LEFT, padx=5)
        nameInput = tk.Entry(rowFrame, width=20)
        nameInput.pack(side=tk.LEFT, padx=5)

        tk.Label(rowFrame, text="Equipment ID:", bg="White").pack(side=tk.LEFT, padx=5)
        equipmentIdInput = tk.Entry(rowFrame, width=10)
        equipmentIdInput.pack(side=tk.LEFT, padx=5)

        blueEntries.append({'id': idInput, 'name': nameInput, 'equipment_id': equipmentIdInput, 'state': "normal"})

    # Submit Button  
    submitBlueButton = tk.Button(blueFrame, text="Submit Blue Team", command=lambda: submitPlayers(blueEntries, "Blue Team"), bg="black", fg="white")
    submitBlueButton.pack(pady=10)
    
    #create start game button
    startFrame = tk.Frame(registration, borderwidth=2, relief="solid", bg="black",  highlightbackground="white", highlightthickness=2)
    startFrame.place(relx=0.0, rely=1.0, anchor='sw', x=20, y=-20)
    startGame = tk.Button(startFrame, text="F5 \n Start Game", command=lambda: end_registration(registration), bg="black", fg="white") 
    startGame.pack(pady=10)
    
    #create f12 button
    clearFrame = tk.Frame(registration, borderwidth=2, relief="solid", bg="black",  highlightbackground="white", highlightthickness=2)
    clearFrame.place(relx=0.0, rely=1.0, anchor='sw', x=180, y=-20)
    clearFrame = tk.Button(clearFrame, text="F12 \n Clear Entries", command=lambda: clearEntries(redEntries, blueEntries), bg="black", fg="white") 
    clearFrame.pack(pady=10)

    #keyboard inputs to start game/countdown, clear player entries, and close window
    registration.bind("<F12>", lambda event: clearEntries(redEntries, blueEntries))
    registration.bind("<F5>", lambda event: end_registration(registration))  
    registration.bind("<Escape>", lambda event: registration.destroy())  

    # TEST: return button adds entries from each team 
    # registration.bind("<Return>", lambda event: (submitPlayers(redEntries, "Red Team"), submitPlayers(blueEntries, "Blue Team")))

    # bind method to registration
    registration.getAllPlayers = getAllPlayers.__get__(registration)

    # bind entries to registration
    registration.redEntries = redEntries
    registration.blueEntries = blueEntries

    #start main event loop
    registration.mainloop() 

# if entry is filled with info
def validEntry(entry):
    if entry['name'].get() and entry['id'].get() and entry['equipment_id'].get():
        return True
    return False

# registration object method to put players into red and blue team
def getAllPlayers(self):   
    redTeam = []
    blueTeam = []

    for entry in self.redEntries:
        if validEntry(entry):
            redTeam.append({'id': entry['id'].get(), 'name': entry['name'].get(), 'equipment_id': entry['equipment_id'].get(), 'state': entry['state']})

    for entry in self.blueEntries:
        if validEntry(entry):
            blueTeam.append({'id': entry['id'].get(), 'name': entry['name'].get(), 'equipment_id': entry['equipment_id'].get(), 'state': entry['state']})

    return (redTeam, blueTeam)


# Show an error message
def errorMessage(message):
   tk.messagebox.showerror("Error", message)

def submitPlayers(entries, team):
    # flag to prevent multiple errors
    player_id_error = False
    equipment_id_error = False

    readable_entries = []

    for entry in entries:
        if (entry['state'] == "normal"):
            readable_entries.append(entry)

    for entry in readable_entries:
        success, error_message = addPlayer(entry)
        if (success):
            # lock input box for successful entry
            entry['name'].config(state='readonly')
            entry['id'].config(state='readonly')
            entry['equipment_id'].config(state='readonly')

            # lock entry
            entry['state'] = "locked"

            # exit loop on first succesful entry
            return None
        
        if (error_message == "Player_ID_error"):
            player_id_error = True
        elif (error_message == "Equipment_ID_error"):
            equipment_id_error = True
    
    # show one error message if error has happened once
    if player_id_error:
        errorMessage(f"Please Input an Integer for player ID on {team}")
        
    if equipment_id_error:
        errorMessage(f"Please Input an Integer for Equipment ID on {team}")


def addPlayer(entry):
        player_id = (entry['id'].get()) # Extract ID from entry widget
        player_name = (entry['name'].get())  # Extract name from entry widget
        player_equipment_id = (entry['equipment_id'].get()) # Extract equipment id fron entry widget

        if (server.add_player(player_id, player_name)):
            # successful entry
            entry['name'].delete(0, tk.END)
            entry['name'].insert(tk.END, server.add_player(player_id, player_name))
        else:
            # unsuccessful entry, existence of player id
            if (player_id):
                print(f"Player ID {player_id} was invalid. Clearing entry.")
                entry['id'].delete(0, tk.END)
                return (False, "Player_ID_error")
            else:
                # player id doesn't exist check next entry
                return (False, "")
         
        # send equipment id when added player to player entry screen
        if player_equipment_id:
            try:
                # check equipment code is integer
                equipment_code = int(player_equipment_id)

                # sends equipment code to udp server
                server.send_equipment_id(equipment_code)
                return (True, "")
            except ValueError:
                entry['equipment_id'].delete(0, tk.END)
                return (False, "Equipment_ID_error")
        else:
            # no equipment id, make operator submit one
            return (False, "Equipment_ID_error")
        

def end_registration(registration):
    print("Game Start")

    # grab players from registration screen
    redTeam, blueTeam = registration.getAllPlayers()

    # check if there are players on both sides
    if (redTeam and blueTeam):
        registration.destroy()
    else:
        # show error message to add players
        errorMessage("Add at least 1 player to both sides before starting")
        return None

    startCountdown(redTeam, blueTeam)
	
def clearEntries(redEntries, blueEntries):
    #go thru red
    for entry in redEntries:
        entry['name'].config(state='normal')
        entry['id'].config(state='normal')
        entry['equipment_id'].config(state='normal')
        entry['state'] = "normal"
        
        entry['id'].delete(0, tk.END)
        entry['name'].delete(0, tk.END)
        entry['equipment_id'].delete(0, tk.END)
        
    #go thru blue
    for entry in blueEntries:
        entry['name'].config(state='normal')
        entry['id'].config(state='normal')
        entry['equipment_id'].config(state='normal')
        entry['state'] = "normal"

        entry['id'].delete(0, tk.END)
        entry['name'].delete(0, tk.END)
        entry['equipment_id'].delete(0, tk.END)
        
    # #clear in server
    # server.clearEntries()

def countdown(count, redTeam, blueTeam):
    try: 
        screen_width = Counter.winfo_screenwidth() 
        screen_height = Counter.winfo_screenheight() 
        img_path = f"../assets/countdown_images/{count}.tif"
        
        img = Image.open(img_path)
        img = img.resize((screen_width, screen_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo 
        
        if count > 0:
            Counter.after(1000, countdown, count - 1, redTeam, blueTeam)
        elif count == 0:
            GameAction(redTeam, blueTeam)
    except Exception as e:
        print(f"Error loading image for countdown: {e}")
        label.config(text="Error loading image")

        
def startCountdown(redTeam, blueTeam):
   global label, Counter
   Counter = tk.Tk()
   Counter.title("Countdown Timer")
   Counter.attributes('-fullscreen', True)
   Counter.configure(bg="black")
    
   label = tk.Label(Counter, bg="black")  
   label.pack(pady=20)
   
   countdown_time = 30
   countdown(countdown_time, redTeam, blueTeam)
   
   Counter.mainloop() 
 
def GameAction(redTeam, blueTeam):
    print("Transitioning to GameAction...")

    # print red and blue team's players info
    print(redTeam, blueTeam)
    Counter.destroy()
    
    GameAction = tk.Tk() 
    GameAction.title("Game Action")
    GameAction.attributes('-fullscreen', True)  
    GameAction.configure(bg="#d3d3d3")  
    
	

splash = tk.Tk()
splash.title("Splash Screen")
splash.attributes('-fullscreen', True)  
splash.configure(bg="#d3d3d3")  

Splash()
splash.mainloop()
