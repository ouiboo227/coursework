# Import the necessary libraries
import tkinter as tk
import tkinter.ttk as ttk
import video_library as lib
import font_manager as fonts
from PIL import Image, ImageTk


# Define a function to set text in a Tkinter text area
def set_text(text_area, content):
    # Clear the content of the text_area
    text_area.delete("1.0", tk.END)
    # Insert new content into the text_area
    text_area.insert(1.0, content)


class UpdateVideos:
    def __init__(self, window):
        window.geometry("800x400")  # Set window size
        window.title("Video Player: Update Videos")  # Set window title
        window.iconbitmap(r"./picture/logo.ico")  # Set window icon

        self.rating = None
        self.director = None
        self.name = None
        self.video_details = None  # Initialize variables to None
        self.values = []  # Initialize values as an empty list

        frame = tk.Frame(window, relief=tk.RAISED)  # Create a frame within the window
        frame.pack()  # Place the frame within the window

        enter_lbl = tk.Label(frame, text="Enter Video Number:")  # Create a label
        enter_lbl.grid(row=0, column=0, sticky="W", padx=10, pady=10)  # Place label in the frame

        self.input_txt = tk.Entry(frame, width=3)  # Create an entry widget for input
        self.input_txt.grid(row=0, column=0, sticky="E", padx=10, pady=10)  # Place entry widget in the frame

        check_video_btn = tk.Button(frame, width=10, text="Check Video", command=self.status_check_video_clicked)
        check_video_btn.grid(row=0, column=2, sticky="W", padx=10, pady=10)  # Button to check video status

        self.combo = ttk.Combobox(frame, width=23, values=self.values, state="readonly")
        self.combo.grid(row=1, column=1, sticky="NW", padx=10, pady=10)  # Place Combobox widget in the frame
        self.values = ["Stay Original", "Name", "Director", "Rating"]  # Update values with the desired items
        self.combo["values"] = self.values
        self.combo.current(0)  # Set the default selection to "Stay Original"

        exit_button = tk.Button(frame, width=10, text="Exit system", command=window.destroy)
        exit_button.grid(row=0, column=2, sticky="E", padx=10, pady=10)  # Button to exit the system

        update_button = tk.Button(frame, width=20, text="Update Video", command=self.check_combobox)
        update_button.grid(row=1, column=1, sticky="SW", padx=10, pady=10)  # Button to update video

        self.video_txt = tk.Text(frame, width=28, height=14, wrap="none")  # Create a text widget
        self.video_txt.grid(row=1, column=0, sticky="NW", padx=10, pady=10)  # Place text widget in the frame

        self.update_input = tk.Entry(frame, width=25)  # Create an entry widget for input
        self.update_input.grid(row=1, column=1, padx=10, pady=10)  # Place entry widget in the frame

        self.image = tk.Canvas(frame, width=255, height=305)  # Create a canvas for an image
        self.image.grid(row=1, column=2, sticky="NW", padx=10, pady=10)  # Place canvas in the frame

        self.status_lbl = tk.Label(frame, text="", font=("Helvetica", 10))  # Create a label
        self.status_lbl.grid(row=1, column=0, columnspan=4, sticky="SW", padx=10, pady=10)  # Place label in the frame

        self.output = tk.StringVar(frame)  # Create a StringVar
        output = tk.Entry(frame, width=25, textvariable=self.output, state="readonly")  # Create an output entry widget
        output.grid(row=0, column=1, padx=10, pady=10)  # Place output entry widget in the frame

        self.welcome_image()  # Call a method to display a welcome image
        self.output.set("None of update yet")  # Set the output entry widget text

    def status_check_video_clicked(self):
        self.check_video_clicked()
        # Update a variable associated with the GUI to display the current video being played
        self.output.set(f"Now playing {self.name}")
        # Update the status label to indicate the button click
        self.status_lbl.configure(text="Check Video button was clicked!")

    def check_video_clicked(self):
        # Get the video key from the input text widget
        key = self.input_txt.get()
        # Check if key is not empty and is a valid string
        if key and isinstance(key, str):
            try:
                key = str(int(key))
                # Get video details using the video_library module
                self.name = lib.get_name(key)
                # Check if the video is found
                if self.name is not None:
                    # Retrieve video details
                    self.director = lib.get_director(key)
                    self.rating = lib.get_rating(key)
                    play_count = lib.get_play_count(key)
                    num_image = lib.get_image(key)
                    # Open and resize the video image
                    image_original = Image.open(f"./picture/{num_image}.jpg").resize((255, 305))
                    image = ImageTk.PhotoImage(image_original)
                    # Update the image in the Tkinter canvas
                    self.image.create_image(0, 0, anchor=tk.NW, image=image)
                    self.image.image = image
                    # Update self.values with video information
                    self.values = ["Stay Original", self.name, self.director, self.rating]
                    self.combo["values"] = self.values
                    self.combo.current(0)
                    # Create a formatted string with video details
                    video_details = f"{self.name}\n{self.director}\nrating: {self.rating}\nplays: {play_count}"
                    # Set the text of the Tkinter text widget with video details
                    set_text(self.video_txt, video_details)
                else:
                    # If video is not found, display a message
                    set_text(self.video_txt, f"Video {key} not found")
                    self.welcome_image()
            except ValueError:
                # Handle the case where key could not be converted to an integer
                set_text(self.video_txt, "Invalid input. Please enter a valid video number.")
                self.welcome_image()
        else:
            # Handle the case where key is empty or not a string
            set_text(self.video_txt, "Invalid input. Please enter a valid video number.")
            self.welcome_image()

    def check_combobox(self):
        selected_index = self.combo.current()  # Get the index of the selected item
        if selected_index == 3:
            # Display a message indicating the previous rating
            self.output.set(f"{self.combo.get()} is the previous rating")
            # Update the rating and refresh the video details
            self.update_rating()
        elif selected_index == 1:
            # Display a message indicating the previous name
            self.output.set(f"{self.combo.get()} is the previous name")
            # Update the name and refresh the video details
            self.update_name()
            self.check_video_clicked()
        elif selected_index == 2:
            # Display a message indicating the previous director
            self.output.set(f"{self.combo.get()} is the previous director")
            # Update the director and refresh the video details
            self.update_director()
        elif selected_index == 0:
            # If no updates, display a message
            self.output.set("No updates made")
            self.update_input.delete(0, tk.END)
        # Update the status label to indicate the button click
        self.status_lbl.configure(text="Update button was clicked!")

    # Update the name of a video based on user input
    def update_name(self):
        key_update = self.input_txt.get()
        key_update = str(int(key_update))
        name = self.update_input.get()
        lib.set_name(key_update, name)
        self.update_input.delete(0, tk.END)

    # Update the rating of a video based on user input
    def update_rating(self):
        key_update = self.input_txt.get()
        key_update = str(int(key_update))
        rating = self.update_input.get()
        if rating.isdigit():
            if 0 <= int(rating) <= 10:
                lib.set_rating(key_update, rating)
                self.check_video_clicked()
            else:
                self.output.set("The number is out of range 0-10")
        else:
            self.output.set("Please input number")
        self.update_input.delete(0, tk.END)

    # Update the director of a video based on user input
    def update_director(self):
        key_update = self.input_txt.get()
        key_update = str(int(key_update))
        director = self.update_input.get()
        if director.isdigit():
            self.output.set("Please input director")
        else:
            lib.set_director(key_update, director)
            self.check_video_clicked()
        self.update_input.delete(0, tk.END)

    # Display a welcome image in the Tkinter canvas
    def welcome_image(self):
        image_original = Image.open("./picture/welcome.png").resize((250, 250))
        image = ImageTk.PhotoImage(image_original)
        self.image.create_image(0, 0, anchor=tk.NW, image=image)
        self.image.image = image


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    UpdateVideos(window)  # open the UpdateVideos GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc
