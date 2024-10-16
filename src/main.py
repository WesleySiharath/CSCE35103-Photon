import server
import tkinter as tk
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
    for _ in range(10): 
        rowFrame = tk.Frame(redFrame, bg="#BA1F33")
        rowFrame.pack(pady=5)

        tk.Label(rowFrame, text="ID:", bg="White").pack(side=tk.LEFT, padx=5)
        idInput = tk.Entry(rowFrame, width=10)
        idInput.pack(side=tk.LEFT, padx=5)
        
        tk.Label(rowFrame, text="Name", bg="White").pack(side=tk.LEFT, padx=5)
        nameInput = tk.Entry(rowFrame, width=20)
        nameInput.pack(side=tk.LEFT, padx=5)

        tk.Label(rowFrame, text="Equipment ID:", bg="White").pack(side=tk.LEFT, padx=5)
        equipmentIdInput = tk.Entry(rowFrame, width=20)
        equipmentIdInput.pack(side=tk.LEFT, padx=5)

        redEntries.append({'id': idInput, 'name': nameInput, 'equipment_id': equipmentIdInput})  # Save references to the entry widgets

    # Submit Button  
    submitRed = tk.Button(redFrame, text="Submit Red Team", command=lambda: addPlayers(redEntries), bg="black", fg="white")
    submitRed.pack(pady=10)

    # Blue Team Table
    blueFrame = tk.Frame(registration, borderwidth=2, relief="solid", bg="#1A2498")
    blueFrame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Title
    tk.Label(blueFrame, text="Blue Team", font=("Courier New", 24), bg="#d3d3d3", fg="black").pack(pady=10)

    # Input Fields
    for _ in range(10):  
        rowFrame = tk.Frame(blueFrame, bg="#4120BA")
        rowFrame.pack(pady=5)

        tk.Label(rowFrame, text="ID:", bg="White").pack(side=tk.LEFT, padx=5)
        idInput = tk.Entry(rowFrame, width=10)
        idInput.pack(side=tk.LEFT, padx=5)

        tk.Label(rowFrame, text="Name:", bg="White").pack(side=tk.LEFT, padx=5)
        nameInput = tk.Entry(rowFrame, width=20)
        nameInput.pack(side=tk.LEFT, padx=5)

        tk.Label(rowFrame, text="Equipment ID:", bg="White").pack(side=tk.LEFT, padx=5)
        equipmentIdInput = tk.Entry(rowFrame, width=20)
        equipmentIdInput.pack(side=tk.LEFT, padx=5)

        blueEntries.append({'id': idInput, 'name': nameInput, 'equipment_id': equipmentIdInput})

    # Submit Button  
    submitBlueButton = tk.Button(blueFrame, text="Submit Blue Team", command=lambda: addPlayers(blueEntries), bg="black", fg="white")
    submitBlueButton.pack(pady=10)
    
    #create start game button
    startFrame = tk.Frame(registration, borderwidth=2, relief="solid", bg="black",  highlightbackground="white", highlightthickness=2)
    startFrame.place(relx=0.0, rely=1.0, anchor='sw', x=20, y=-20)
    startGame = tk.Button(startFrame, text="F5 \n Start Game", command=lambda: end_registration(registration), bg="black", fg="white") 
    startGame.pack(pady=10)

    #keyboard inputs to start game/countdown, clear player entries, and close window
    registration.bind("<F12>", lambda event: clearEntries(redEntries, blueEntries))
    registration.bind("<F5>", lambda event: end_registration(registration))  
    registration.bind("<Escape>", lambda event: registration.destroy())  
    
    #start main event loop
    registration.mainloop() 

def addPlayers(entries):
    for entry in entries:

        player_id = (entry['id'].get()) # Extract ID from entry widget
        player_name = (entry['name'].get())  # Extract name from entry widget
        player_equipment_id = (entry['equipment_id'].get()) # Extract equipment id fron entry widget

        # all three entries have to be filled 
        if player_id and player_name and player_equipment_id:
            poggers = server.add_player(player_id, player_name, player_equipment_id)

            if poggers == 1:
                print(f"Player ID {player_id} was invalid. Clearing entry.")
                entry['id'].delete(0, tk.END)
            elif poggers == 2:
                print(f"Equipment ID {player_equipment_id} was invalid. Clearing entry.")
                entry['equipment_id'].delete(0, tk.END)
            elif poggers == 3:
                print(f"Duplicate Player ID. Clearing entry.")
                entry['id'].delete(0, tk.END)
            else:
                print(f"Nice, player added successfully")
        

def end_registration(registration):
	print("Game Start")
	registration.destroy()
	startCountdown()
	
def clearEntries(redEntries, blueEntries):
    #go thru red
    for entry in redEntries:
        entry['id'].delete(0, tk.END)
        entry['name'].delete(0, tk.END)
        entry['equipment_id'].delete(0, tk.END)
        
    #go thru blue
    for entry in blueEntries:
        entry['id'].delete(0, tk.END)
        entry['name'].delete(0, tk.END)
        entry['equipment_id'].delete(0, tk.END)
        
    #clear in server
    server.clearEntries()

def countdown(count):
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
            Counter.after(1000, countdown, count - 1)
        elif count == 0:
            GameAction()
    except Exception as e:
        print(f"Error loading image for countdown: {e}")
        label.config(text="Error loading image")

        
def startCountdown():
   global label, Counter
   Counter = tk.Tk()
   Counter.title("Countdown Timer")
   Counter.attributes('-fullscreen', True)
   Counter.configure(bg="black")
    
   label = tk.Label(Counter, bg="black")  
   label.pack(pady=20)
   
   countdown_time = 30
   countdown(countdown_time)
   
   Counter.mainloop() 
 
def GameAction():
    print("Transitioning to GameAction...")
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
