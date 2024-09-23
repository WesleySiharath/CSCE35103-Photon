import tkinter as tk
from PIL import Image, ImageTk

def show_image():
    try:
        # Load the image
        img = Image.open("image.jpeg")  # Replace with your image file name
        img = img.resize((300, 300), Image.LANCZOS)  # Resize if needed
        photo = ImageTk.PhotoImage(img)

        # Create a label to display the image
        label = tk.Label(splash_root, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack()

        # Set a timer to close the splash window and show the team registration page
        splash_root.after(3000, show_team_registration)  # 3000 milliseconds = 3 seconds
    except Exception as e:
        print(f"Error loading image: {e}")

def show_team_registration():
    print("Transitioning to team registration...")  # Debug print
    splash_root.destroy()  # Close the splash screen

    registration_root = tk.Tk()  # Create the registration window
    registration_root.title("Team Registration")
    registration_root.attributes('-fullscreen', True)  # Set full screen

    # Set grey background
    registration_root.configure(bg="#d3d3d3")  # Light grey background

    # Red Team Table
    red_frame = tk.Frame(registration_root, borderwidth=2, relief="solid", bg="#d3d3d3")
    red_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    tk.Label(red_frame, text="Red Team", font=("Times New Roman", 24), bg="#d3d3d3", fg="black").pack(pady=10)

    for _ in range(10):  # 10 rows
        row_frame = tk.Frame(red_frame, bg="#d3d3d3")
        row_frame.pack(pady=5)

        player_id_entry = tk.Entry(row_frame, width=10)
        player_id_entry.pack(side=tk.LEFT, padx=5)

        player_name_entry = tk.Entry(row_frame, width=20)
        player_name_entry.pack(side=tk.LEFT, padx=5)

    submit_red_button = tk.Button(red_frame, text="Submit Red Team", command=lambda: print("Red Team submitted"), bg="black", fg="white")
    submit_red_button.pack(pady=10)

    # Blue Team Table
    blue_frame = tk.Frame(registration_root, borderwidth=2, relief="solid", bg="#d3d3d3")
    blue_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    tk.Label(blue_frame, text="Blue Team", font=("Times New Roman", 24), bg="#d3d3d3", fg="black").pack(pady=10)

    for _ in range(10):  # 10 rows
        row_frame = tk.Frame(blue_frame, bg="#d3d3d3")
        row_frame.pack(pady=5)

        player_id_entry = tk.Entry(row_frame, width=10)
        player_id_entry.pack(side=tk.LEFT, padx=5)

        player_name_entry = tk.Entry(row_frame, width=20)
        player_name_entry.pack(side=tk.LEFT, padx=5)

    submit_blue_button = tk.Button(blue_frame, text="Submit Blue Team", command=lambda: print("Blue Team submitted"), bg="black", fg="white")
    submit_blue_button.pack(pady=10)

    registration_root.bind("<Escape>", lambda event: registration_root.destroy())  # Exit fullscreen with Esc
    registration_root.mainloop()  # Start the registration window event loop

# Create the splash window
splash_root = tk.Tk()
splash_root.title("Splash Screen")
splash_root.attributes('-fullscreen', True)  # Set full screen for splash
splash_root.configure(bg="#d3d3d3")  # Light grey background for the splash

# Call the function to show the image
show_image()

# Start the splash window event loop
splash_root.mainloop()
