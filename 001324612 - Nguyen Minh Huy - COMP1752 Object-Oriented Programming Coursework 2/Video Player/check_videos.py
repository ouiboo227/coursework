# Import libraries with clear aliases
import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import font_manager as fonts
import video_library as lib


# Define a function using clear and descriptive names
def set_text(text_area, content):
    # Clear the content of the text_area
    text_area.delete("1.0", tk.END)
    # Insert new content into the text_area
    text_area.insert(1.0, content)


class CheckVideos:  # class CheckVideos
    def __init__(self, window):
        # Set up the main window properties using Tkinter
        self.name = None
        window.geometry("900x400")
        window.title("Video Player: Check Videos")
        window.iconbitmap(r"./picture/logo.ico")

        # Create a frame within the window
        frame = tk.Frame(window, relief=tk.RAISED)
        frame.pack()

        # Check Video Section
        # Label for entering video number
        enter_lbl = tk.Label(frame, text="Enter Video Number:")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Entry widget for inputting the video number
        self.input_txt = tk.Entry(frame, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Button to check the video details, linked to the check_video_clicked method
        check_video_btn = tk.Button(frame, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, sticky="W", padx=10, pady=10)

        # Result Section
        # ScrolledText widget for displaying video details
        self.video_txt = tkst.ScrolledText(frame, width=48, height=14, wrap="none")
        self.video_txt.grid(row=1, column=0, columnspan=3, sticky="NW", padx=10, pady=10)

        # Exit Section
        # Button to exit the system
        exit_button = tk.Button(frame, text="Exit System", command=window.destroy)
        exit_button.grid(row=0, column=4, sticky="E", padx=10, pady=10)

        # Search Section
        # Button to search for videos, linked to the search_clicked method
        search_button = tk.Button(frame, text="Search Video", command=self.search_clicked)
        search_button.grid(row=0, column=4, sticky="W", padx=10, pady=10)

        # ComboBox for selecting search criteria
        self.combo = ttk.Combobox(frame, width=12, state="readonly")
        self.combo.grid(row=1, column=3, sticky="NW", padx=10, pady=10)
        self.combo["values"] = ["all", "name", "director", "rating"]
        self.combo.current(0)

        # Label for search entry
        search_lbl = tk.Label(frame, text="Search Here:")
        search_lbl.grid(row=1, column=3, padx=10, pady=10)

        # Entry widget for search input
        self.search_txt = tk.Entry(frame, width=14)
        self.search_txt.grid(row=1, column=3, sticky="SW", padx=10, pady=10)

        # Status Section
        # Label for displaying system status
        self.status_lbl = tk.Label(frame, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=1, column=0, columnspan=4, sticky="SW", padx=10, pady=10)

        # Image Section
        # Canvas for displaying images
        self.image = tk.Canvas(frame, width=255, height=305)
        self.image.grid(row=1, column=4, sticky="N", padx=10, pady=10)

        # Call the welcome_image method to display an initial image
        self.welcome_image()

        # List All Videos Section
        # Button to list all videos, linked to the list_videos_clicked method
        list_videos_btn = tk.Button(frame, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        # Call the list_videos_clicked method to initially list all videos
        self.list_videos_clicked()

    def check_video_clicked(self):
        # Get the input key from a text widget
        key = self.input_txt.get()
        # Check if key is not empty and is a valid string
        if key and isinstance(key, str):
            try:
                key = str(int(key))
                # Get the name of the video using a function from the 'lib' module
                name = lib.get_name(key)
                # Check if the video name is not None (i.e., video found)
                if name is not None:
                    # Get director, rating, play count, and image number using respective functions
                    director = lib.get_director(key)
                    rating = lib.get_rating(key)
                    play_count = lib.get_play_count(key)
                    num_image = lib.get_image(key)
                    # Open and resize the image based on the image number
                    image_original = Image.open(f"./picture/{num_image}.jpg").resize((255, 305))
                    # Convert the image to a Tkinter PhotoImage
                    image = ImageTk.PhotoImage(image_original)
                    # Create an image widget in the Tkinter canvas
                    self.image.create_image(0, 0, anchor=tk.NW, image=image)
                    # Associate the image with the image attribute of the Tkinter canvas
                    self.image.image = image
                    # Create a formatted string with video details
                    video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
                    # Set the text of a Tkinter text widget with the video details
                    set_text(self.video_txt, video_details)
                else:
                    # If video is not found, set a message indicating it
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
        # Update the text of a Tkinter label to indicate the button click
        self.status_lbl.configure(text="Check Video button was clicked!")
        self.input_txt.delete(0, tk.END)

    def search_clicked(self):
        self.video_txt.delete(1.0, tk.END)
        # Get search input from the entry widget
        search_input = self.search_txt.get()
        # Check if search input is empty
        if search_input is None or search_input == "":
            set_text(self.video_txt, f"Video not found")
        else:
            # Get the selected search type from the combo box
            combo_value = self.combo.get()
            # Check if all videos are to be searched
            if combo_value == "all":
                # Perform a general search and display results
                search_result = lib.search_all(search_input)
                if not search_result:
                    set_text(self.video_txt, f"Video {search_input} not found")
                    self.welcome_image()
                for key in search_result:
                    search_name = lib.get_name(key)
                    if search_name is not None:
                        # If video is found, display its details and image
                        director = lib.get_director(key)
                        rating = lib.get_rating(key)
                        play_count = lib.get_play_count(key)
                        num_image = lib.get_image(key)
                        image_original = Image.open(f"./picture/{num_image}.jpg").resize((255, 305))
                        image = ImageTk.PhotoImage(image_original)
                        self.image.create_image(0, 0, anchor=tk.NW, image=image)
                        self.image.image = image
                        video_details = (f"{search_name}\n{director}\nRating: {rating}\nPlays: {play_count}\n "
                                         f"_____________________\n")
                        self.video_txt.insert(1.0, video_details)
                    else:
                        # If video is not found, display a message
                        set_text(self.video_txt, f"Video {key} not found")
                        self.welcome_image()
            else:
                # Perform a specific search based on the selected type
                search_type = combo_value
                search_result = lib.search_library(search_input, search_type)
                for key in search_result:
                    search_name = lib.get_name(key)
                    if search_name is not None:
                        # If video is found, display its details and image
                        director = lib.get_director(key)
                        rating = lib.get_rating(key)
                        play_count = lib.get_play_count(key)
                        num_image = lib.get_image(key)
                        image_original = Image.open(f"./picture/{num_image}.jpg").resize((255, 305))
                        image = ImageTk.PhotoImage(image_original)
                        self.image.create_image(0, 0, anchor=tk.NW, image=image)
                        self.image.image = image
                        video_details = (f"{search_name}\n{director}\nRating: {rating}\nPlays: {play_count}\n "
                                         f"_____________________\n")
                        self.video_txt.insert(1.0, video_details)
                    else:
                        # If video is not found, display a message
                        set_text(self.video_txt, f"Video {key} not found")
                        self.welcome_image()
        # Update the status label
        self.status_lbl.configure(text="Search Video button was clicked!")
        self.search_txt.delete(0, tk.END)

    def list_videos_clicked(self):
        # Get a list of all videos and display them
        video_list = lib.list_all()
        set_text(self.video_txt, video_list)
        # Update the status label
        self.status_lbl.configure(text="List Videos button was clicked!")

    def welcome_image(self):
        # Display a welcome image
        image_original = Image.open("./picture/welcome.png").resize((255, 255))
        image = ImageTk.PhotoImage(image_original)
        self.image.create_image(0, 0, anchor=tk.NW, image=image)
        self.image.image = image


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    CheckVideos(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc
