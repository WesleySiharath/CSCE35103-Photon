import server
import tkinter as tk
import pygame
import os
import random
import threading
from queue import Queue
from heapq import heapify, heappush, heappop
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import python_udpserver

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

def playGameMusic():
    try:
        folder = "../assets/photon_tracks"
        tracks = [os.path.join(folder, track) for track in os.listdir(folder)]
        
        if not tracks:
            print("in terms of music there is no music :(")
            return
        
        pygame.mixer.init()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        
        def playNextTrack():
            track = random.choice(tracks)
            pygame.mixer.music.load(track)
            pygame.mixer.music.play()
            
        playNextTrack()
        
        def musicEndevent():
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    playNextTrack()
            splash.after(100, musicEndevent)
            
        musicEndevent()
        
    except Exception as e:
        print(f"Error playing background music: {e}")
        
def stopMusic():
    if pygame.mixer.get_init():
        pygame.mixer.music.stop()

def playSound(path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error playing sound: {e}")

def teamRegistration(redTeam = [{} for i in range(15)], blueTeam = [{} for i in range(15)]):
    #initialize lists
    redEntries = []
    blueEntries = []
    
    print("Transitioning to team registration...")
    # move splash destroy 
    try:
        splash.destroy()
    except Exception:
        pass

    registration = tk.Toplevel(root) 
    registration.title("Team Registration")

    registration.geometry("%dx%d" % (screen_width, screen_height))
    # registration.state('zoomed')
    registration.configure(bg="#d3d3d3")

    # Red Team Table
    redFrame = tk.Frame(registration, borderwidth=2, relief="solid", bg="#981A2B")
    redFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Title
    tk.Label(redFrame, text="Red Team", font=("Courier New", 24), bg="#d3d3d3", fg="black").pack(pady=10)

    # Input Fields
    for i in range(15): 
        rowFrame = tk.Frame(redFrame, bg="#BA1F33")
        rowFrame.pack(pady=5)

        tk.Label(rowFrame, text="ID:", bg="White", fg="Black").pack(side=tk.LEFT, padx=5)
        idInput = tk.Entry(rowFrame, width=10)
        idInput.pack(side=tk.LEFT, padx=5)
        
        tk.Label(rowFrame, text="Name", bg="White", fg="Black").pack(side=tk.LEFT, padx=5)
        nameInput = tk.Entry(rowFrame, width=20)
        nameInput.pack(side=tk.LEFT, padx=5)

        tk.Label(rowFrame, text="Equipment ID:", bg="White", fg="Black").pack(side=tk.LEFT, padx=5)
        equipmentIdInput = tk.Entry(rowFrame, width=10)
        equipmentIdInput.pack(side=tk.LEFT, padx=5)
        try:
            if redTeam[i]:
                idInput.insert(tk.END, redTeam[i]['id'])
                nameInput.insert(tk.END, redTeam[i]['name'])
                equipmentIdInput.insert(tk.END, redTeam[i]['equipment_id'])
        except:
            pass

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
    for i in range(15):  
        rowFrame = tk.Frame(blueFrame, bg="#4120BA")
        rowFrame.pack(pady=5)

        tk.Label(rowFrame, text="ID:", bg="White", fg="Black").pack(side=tk.LEFT, padx=5)
        idInput = tk.Entry(rowFrame, width=10)
        idInput.pack(side=tk.LEFT, padx=5)

        tk.Label(rowFrame, text="Name:", bg="White", fg="Black").pack(side=tk.LEFT, padx=5)
        nameInput = tk.Entry(rowFrame, width=20)
        nameInput.pack(side=tk.LEFT, padx=5)

        tk.Label(rowFrame, text="Equipment ID:", bg="White", fg="Black").pack(side=tk.LEFT, padx=5)
        equipmentIdInput = tk.Entry(rowFrame, width=10)
        equipmentIdInput.pack(side=tk.LEFT, padx=5)
        try:
            if blueTeam[i]:
                idInput.insert(tk.END, blueTeam[i]['id'])
                nameInput.insert(tk.END, blueTeam[i]['name'])
                equipmentIdInput.insert(tk.END, blueTeam[i]['equipment_id'])
        except:
            pass

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

    def endProgram():
        playSound("../assets/sounds/fortniteknocked.mp3")
        registration.destroy()
        root.destroy
        exit()

    #keyboard inputs to start game/countdown, clear player entries, and close window
    registration.bind("<F12>", lambda event: clearEntries(redEntries, blueEntries))
    registration.bind("<F5>", lambda event: end_registration(registration))  
    registration.bind("<Escape>", lambda event: endProgram())  

    # bind method to registration
    registration.getAllPlayers = getAllPlayers.__get__(registration)

    # bind entries to registration
    registration.redEntries = redEntries
    registration.blueEntries = blueEntries

    #start main event loop
    registration.mainloop() 

# if entry is filled with info
def validEntry(entry):
    if entry['name'].get() and entry['id'].get() and entry['equipment_id'].get() and entry['state'] == "locked":
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
        errorMessage(f"Please Input an Integer for player ID or add code name on {team}")
        
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
                server.send_code(equipment_code)
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

def countdown(count, redTeam, blueTeam, images):
    label.config(image='')
    try: 
        photo = ImageTk.PhotoImage(images[count])
        label.config(image=photo)
        label.image = photo 
        
        if count > 0:
            if count == 15:
                playGameMusic()
            Counter.after(930, countdown, count - 1, redTeam, blueTeam, images)
        elif count == 0:
            # send start code
            server.send_code(202)
            GameAction(redTeam, blueTeam)
    except Exception as e:
        print(f"Error loading image for countdown: {e}")
        label.config(text="Error loading image")

def startCountdown(redTeam, blueTeam):
   global label, Counter
   Counter = tk.Toplevel(root)
   Counter.title("Countdown Timer")
   Counter.geometry("%dx%d" % (screen_width, screen_height))
   Counter.configure(bg="black")
    
   label = tk.Label(Counter, bg="black")  
   label.pack(pady=20)

   #sound
   playSound("../assets/sounds/rumble.mp3")
   countdown(countdown_time, redTeam, blueTeam, images)
   
   Counter.mainloop() 

def update_timer(button, label, remaining_time, redTeam, blueTeam, GameAction):
	
    if remaining_time > 0:
        mins, secs = divmod(remaining_time, 60)
        time_format = f"{mins:02}:{secs:02}"
        label.config(text=f"Time Remaining: {time_format}")
        label.after(1000, update_timer, button, label, remaining_time - 1, redTeam, blueTeam, GameAction)
            
    else:
        button.configure(command=lambda: (GameAction.destroy(), teamRegistration(redTeam, blueTeam)))
        GameAction.bind("<F1>", lambda event: (GameAction.destroy(), teamRegistration(redTeam, blueTeam)))
        label.config(text="Time Remaining: 00:00")
        stopMusic()
        playSound("../assets/sounds/ThatsTheGame.mp3")
        # send stop code 3 times
        server.send_code(221)
        server.send_code(221)
        server.send_code(221)

def update_team_score_labels(redTeam_score, blueTeam_score, redScoreLabel, blueScoreLabel):
    redScoreLabel.config(text=f"Red Team Score: {redTeam_score}")
    blueScoreLabel.config(text=f"Blue Team Score: {blueTeam_score}")

    if redTeam_score >= blueTeam_score:
        current_bg = redScoreLabel.cget("bg")
        new_bg = "#981A2B" if current_bg == "white" else "white"
        redScoreLabel.config(bg=new_bg)

    elif blueTeam_score > redTeam_score:
        current_bg = blueScoreLabel.cget("bg")
        new_bg = "#1A2B98" if current_bg == "white" else "white"
        blueScoreLabel.config(bg=new_bg)

def update_playaction(eventLogText, redTeam, blueTeam, redTeam_score, blueTeam_score, redScoreLabel, blueScoreLabel, blueFrame, redFrame):
    try:
        if not udp_queue.empty():
            data = str(udp_queue.get())
            data = data.strip("[]")
            data_list = data.split(",")  
            hitter = data_list[0].strip().strip("'")
            hit = data_list[1].strip().strip("'")

            hitter_player = None
            hit_player = None
            hit_base = None
            base_hit = False

            for player in redTeam + blueTeam:
                if int(player['equipment_id']) == int(hitter):
                    hitter_player = player
                if int(player['equipment_id']) == int(hit):
                    hit_player = player
       
                if hit == '43':
                   hit_base = '43'
                elif hit == '53':
                   hit_base = '53'
			

            eventLogText.config(state=tk.NORMAL) 
            if hitter_player and hit_player:
                eventLogText.insert(tk.END, "Shooter: ", "default")
                if hitter_player in redTeam:
                    eventLogText.insert(tk.END, f"{hitter_player['name']} ", "red")
                else:
                    eventLogText.insert(tk.END, f"{hitter_player['name']} ", "blue")

                eventLogText.insert(tk.END, "- Hit: ", "default")
                if hit_player in redTeam:
                    eventLogText.insert(tk.END, f"{hit_player['name']}\n", "red")
                else:
                    eventLogText.insert(tk.END, f"{hit_player['name']}\n", "blue")
                
                # scores
                if hit_player in redTeam and hitter_player in blueTeam:
                    blueTeam_score += 10
                    hitter_player['score'] += 10
                elif hit_player in blueTeam and hitter_player in redTeam:
                    redTeam_score += 10
                    hitter_player['score'] += 10
                elif hit_player in redTeam and hitter_player in redTeam:
                    redTeam_score -= 10
                    hitter_player['score'] -= 10
                    server.send_code(hitter_player['equipment_id'])
                elif hit_player in blueTeam and hitter_player in blueTeam:
                    blueTeam_score -= 10
                    hitter_player['score'] -= 10
                    server.send_code(hitter_player['equipment_id'])
                    
            elif hit_base == '43':
                base_hit = True
                redTeam_score += 100
                hitter_player['score'] += 100
            elif hit_base == '53':
                base_hit = True
                blueTeam_score += 100
                hitter_player['score'] += 100
            else:
                eventLogText.insert(tk.END, "Error: Player not found\n", "error")
                
            if base_hit == True:
               eventLogText.insert(tk.END, "Shooter: ", "default")
               if hitter_player in redTeam:
                   eventLogText.insert(tk.END, f"{hitter_player['name']} ", "red")
                   eventLogText.insert(tk.END, "- Hit: ", "default")
                   eventLogText.insert(tk.END, f"BLUE BASE \n", "blue")
               else:
                   eventLogText.insert(tk.END, f"{hitter_player['name']} ", "blue")
                   eventLogText.insert(tk.END, "- Hit: ", "default")
                   eventLogText.insert(tk.END, f"RED BASE \n", "red")

            eventLogText.config(state=tk.DISABLED) 

            # sort teams by score
            sortedRed = []
            sortedBlue = []

            for player in redTeam:
                if int(player['equipment_id']) == int(hitter):
                    player['score'] = hitter_player['score']

                heappush(sortedRed, (-1 * player['score'], player['name'], player['label']))

            for player in blueTeam:
                if int(player['equipment_id']) == int(hitter):
                    player['score'] = hitter_player['score']

                heappush(sortedBlue, (-1 * player['score'], player['name'], player['label']))

            # Blue Team Players
            for index, widget in enumerate(blueFrame.winfo_children()):
                if index == 0 or index == 1:
                    continue
                score, player, label = heappop(sortedBlue)
                widget.winfo_children()[0].config(text = f"{player}: {-1 * score}")

                hitter_player['label'] = widget.winfo_children()[0]

            # Red Team Players 
            for index, widget in enumerate(redFrame.winfo_children()):
                if index == 0 or index == 1:
                    continue
                score, player, label = heappop(sortedRed)
                widget.winfo_children()[0].config(text = f"{player}: {-1 * score}")

                hitter_player['label'] = widget.winfo_children()[0]

            eventLogText.yview(tk.END)

    except Exception as e:
        print(f"Error updating play action: {e}")

    update_team_score_labels(redTeam_score, blueTeam_score, redScoreLabel, blueScoreLabel)
    eventLogText.after(250, update_playaction, eventLogText, redTeam, blueTeam, redTeam_score, blueTeam_score, redScoreLabel, blueScoreLabel, blueFrame, redFrame)

def GameAction(redTeam, blueTeam):
    for player in redTeam + blueTeam:
        player["score"] = 0

    Counter.destroy()
    GameAction = tk.Toplevel(root)
    GameAction.title("Game Action")
    GameAction.geometry("%dx%d" % (screen_width, screen_height))
    GameAction.configure(bg="black")
    remaining_time = 6 * 60
    redTeam_score = 0
    blueTeam_score = 0
    # Title
    timer_label = tk.Label(GameAction, text="Time Remaining: 06:00", font=("Courier New", 24), bg="white", fg="black")
    timer_label.pack(pady=10)
	
    # Create a frame to contain the team frames, aligned horizontally
    teamFrame = tk.Frame(GameAction, bg="white")
    teamFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Red Team Frame
    redFrame = tk.Frame(teamFrame, borderwidth=1, relief="solid", bg="#981A2B")
    redFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Red Team Header
    redHeaderFrame = tk.Frame(redFrame, bg="#981A2B")
    redHeaderFrame.pack(side=tk.TOP, pady=5, fill=tk.X)
    redScoreLabel = tk.Label(redFrame, text=f"Red Team Score: {redTeam_score}", font=("Courier New", 24), bg="white", fg="black")
    redScoreLabel.pack(side=tk.TOP, padx=10, anchor="w")

    # Red Team Players
    for player in redTeam:
        rowFrame = tk.Frame(redFrame, bg="#981A2B")
        rowFrame.pack(side=tk.TOP, fill=tk.X, pady=5)
        score = tk.Label(rowFrame, text=f"{player['name']}: {player['score']}", bg="#981A2B", fg="white")
        score.pack(anchor="w")
        player['label'] = score
    
    # Blue Team Frame
    blueFrame = tk.Frame(teamFrame, borderwidth=1, relief="solid", bg="#1A2B98")
    blueFrame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Blue Team Header
    blueHeaderFrame = tk.Frame(blueFrame, bg="#1A2B98")
    blueHeaderFrame.pack(side=tk.TOP, pady=5, fill=tk.X)
    blueScoreLabel = tk.Label(blueFrame, text=f"Blue Team Score: {blueTeam_score}", font=("Courier New", 24), bg="white", fg="black")
    blueScoreLabel.pack(side=tk.TOP, padx=10, anchor="w")

    # Blue Team Players
    for player in blueTeam:
        rowFrame = tk.Frame(blueFrame, bg="#1A2B98")
        rowFrame.pack(side=tk.TOP, fill=tk.X, pady=5)
        score = tk.Label(rowFrame, text=f"{player['name']}: {player['score']}", bg="#1A2B98", fg="white")
        score.pack(anchor="w")
        player['label'] = score
    
    # event log and scrollbar
    eventLog = tk.Frame(GameAction, bg="white")
    eventLog.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(eventLog)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    eventLogText = tk.Text(
    eventLog,
    height=10,
    width=80,
    yscrollcommand=scrollbar.set,
    bg="black",
    fg="white",
    font=("Courier New", 14),
    wrap=tk.WORD,
    state=tk.DISABLED
    )
    scrollbar.config(command=eventLogText.yview)
    eventLogText.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    eventLogText.tag_configure("red", foreground="red")
    eventLogText.tag_configure("blue", foreground="blue")
    eventLogText.tag_configure("default", foreground="white")
    eventLogText.tag_configure("error", foreground="yellow")

    # Play frame at the bottom
    playFrame = tk.Frame(GameAction, borderwidth=1, relief="solid", bg="white")
    playFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)
    tk.Label(playFrame, text="Game Action", font=("Courier New", 24), bg="white", fg="black").pack(pady=10)
    
    
    # create button to return to player entry screen
    buttonFrame = tk.Frame(GameAction, borderwidth=2, relief="solid", bg="black",  highlightbackground="white", highlightthickness=2)
    buttonFrame.place(relx=1.0, rely=1.0, anchor='se', x=-20, y=-20)
    buttonFrame = tk.Button(buttonFrame, text="F1\nReturn to Player Entry Screen", bg="black", fg="white") 
    buttonFrame.pack(pady=10)
    
    update_timer(buttonFrame, timer_label, remaining_time, redTeam, blueTeam, GameAction)
    update_playaction(eventLogText, redTeam, blueTeam, redTeam_score, blueTeam_score, redScoreLabel, blueScoreLabel, blueFrame, redFrame)

    GameAction.mainloop()
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")
    root.withdraw()

    splash = tk.Toplevel(root)
    splash.title("Splash Screen")
    screen_width = splash.winfo_screenwidth() 
    screen_height = splash.winfo_screenheight() 
    splash.geometry("%dx%d" % (screen_width, screen_height))

    splash.configure(bg="#d3d3d3") 

    udp_queue = Queue() 

    udp_thread = threading.Thread(target=python_udpserver.udp_server, args=(udp_queue,), daemon=True)
    udp_thread.start()
    
    images = []  
    
    countdown_time = 30
    if not images:
        for i in range(countdown_time + 1):
            img_path = f"../assets/countdown_images/{i}.tif"

            img = Image.open(img_path)
            img = img.resize((screen_width, screen_height), Image.LANCZOS)
            images.append(img) 

    Splash()
    root.mainloop()

