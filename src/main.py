import server
import tkinter as tk
from PIL import Image, ImageTk

def Splash():
    try:
    
        img = Image.open("../assets/logo.jpg")  
        img = img.resize((1000, 1000), Image.LANCZOS)  
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
        
    submitRed = tk.Button(redFrame, text="Submit Red Team", command=lambda: print("Red Team submitted"), bg="black", fg="white")
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

    submitBlueButton = tk.Button(blueFrame, text="Submit Blue Team", command=lambda: print("Blue Team submitted"), bg="black", fg="white")
    submitBlueButton.pack(pady=10)
    
    #create start game button
    startFrame = tk.Frame(registration, borderwidth=2, relief="solid", bg="#981A2B")
    startFrame.pack(pady=20)
    startGame = tk.Button(startFrame, text="Start", command=lambda: end_registration(registration), bg="black", fg="white")
    startGame.pack(pady=10)

    registration.bind("<Escape>", lambda event: registration.destroy())  
    registration.mainloop() 
    
def end_registration(registration):
	print("Game Start")
	registration.destroy()
	startCountdown()
	
	
def countdown(count):
    label['text'] = count

    if count > 0:
        root.after(1000, countdown, count - 1)
    else:
        label['text'] = "To be continued"
        
def startCountdown():
    global label, root
    root = tk.Tk()
    root.title("Countdown Timer")
    
    # Set the window to full screen
    root.attributes('-fullscreen', True)
    root.configure(bg="black")  # Set background color to black

    label = tk.Label(root, font=('Helvetica', 48), fg="white", bg="black")  # Set text color to white
    label.pack(pady=20)

    countdown_time = 10
    countdown(countdown_time)
    
    root.mainloop()       

splash = tk.Tk()
splash.title("Splash Screen")
splash.attributes('-fullscreen', True)  
splash.configure(bg="#d3d3d3")  

Splash()
splash.mainloop()
