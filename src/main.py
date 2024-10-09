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
    print("Transitioning to team registration...")
    splash.destroy() 

    registration = tk.Tk() 
    registration.title("Team Registration")
    registration.attributes('-fullscreen', True)  
    registration.configure(bg="#d3d3d3")  
 
    redFrame = tk.Frame(registration, borderwidth=2, relief="solid", bg="#981A2B")
    redFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    tk.Label(redFrame, text="Red Team", font=("Courier New", 24), bg="#d3d3d3", fg="black").pack(pady=10)

    for _ in range(10): 
        rowFrame = tk.Frame(redFrame, bg="#BA1F33")
        rowFrame.pack(pady=5)
        tk.Label(rowFrame, text="ID:", bg="White").pack(side=tk.LEFT, padx=5)
        idInput = tk.Entry(rowFrame, width=10)
        idInput.pack(side=tk.LEFT, padx=5)
        
        tk.Label(rowFrame, text="Name", bg="White").pack(side=tk.LEFT, padx=5)
        nameInput = tk.Entry(rowFrame, width=20)
        nameInput.pack(side=tk.LEFT, padx=5)
        redEntries.append({'id': int(idInput), 'name': str(nameInput)})
        
    submitRed = tk.Button(redFrame, text="Submit Red Team", command=lambda: addPlayers(redEntries), bg="black", fg="white")
    submitRed.pack(pady=10)

    # Blue Team Table
    blueFrame = tk.Frame(registration, borderwidth=2, relief="solid", bg="#1A2498")
    blueFrame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    tk.Label(blueFrame, text="Blue Team", font=("Courier New", 24), bg="#d3d3d3", fg="black").pack(pady=10)

    for _ in range(10):  
        rowFrame = tk.Frame(blueFrame, bg="#4120BA")
        rowFrame.pack(pady=5)
        tk.Label(rowFrame, text="ID:", bg="White").pack(side=tk.LEFT, padx=5)
        idInput = tk.Entry(rowFrame, width=10)
        idInput.pack(side=tk.LEFT, padx=5)
        tk.Label(rowFrame, text="Name:", bg="White").pack(side=tk.LEFT, padx=5)
        nameInput = tk.Entry(rowFrame, width=20)
        nameInput.pack(side=tk.LEFT, padx=5)
        blueEntries.append({'id': int(idInput), 'name': str(nameInput)})

    submitBlueButton = tk.Button(blueFrame, text="Submit Blue Team", command=lambda: addPlayers(blueEntries), bg="black", fg="white")
    submitBlueButton.pack(pady=10)
    
    #create start game button
    startFrame = tk.Frame(registration, borderwidth=2, relief="solid", bg="black",  highlightbackground="white", highlightthickness=2)
    startFrame.place(relx=0.0, rely=1.0, anchor='sw', x=20, y=-20)
    startGame = tk.Button(startFrame, text="F3", command=lambda: end_registration(registration), bg="black", fg="white") 
    startGame.pack(pady=10)

    registration.bind("<F3>", lambda event: end_registration(registration))  
    registration.bind("<Escape>", lambda event: registration.destroy())  
    registration.mainloop() 
    
def end_registration(registration):
	print("Game Start")
	registration.destroy()
	startCountdown()
	

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
