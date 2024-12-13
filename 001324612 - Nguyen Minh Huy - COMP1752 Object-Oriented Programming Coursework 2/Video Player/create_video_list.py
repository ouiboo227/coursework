# Import the Tkinter library with alias 'tk'
import tkinter as tk
# Import a specific module 'scrolledtext' from the Tkinter library
import tkinter.scrolledtext as tkst

# Import the 'Image' and 'ImageTk' modules from the 'PIL' library for image handling
from PIL import Image, ImageTk

# Import the 'font_manager' module for font management
import font_manager as fonts
# Import the 'video_library' module for video-related functionality
import video_library as lib


# Define a function 'set_text' to update the content of a Tkinter text area
def set_text(text_area, content):
    # Clear the existing content in the text_area
    text_area.delete("1.0", tk.END)
    # Insert the new content into the text_area
    text_area.insert(1.0, content)


# Define a class for creating a video list GUI
class CreateVideoList:
    # Constructor to initialize the GUI window
    def __init__(self, window):
        # Initialize attributes to None
        self.play_count = None
        self.rating = None
        self.director = None
        self.name = None

        window.geometry("1000x400")
        window.title("Video Player: Create Video List")
        # You can set the window icon if you have the appropriate .ico file
        window.iconbitmap(r"./picture/logo.ico")

        # Create a Tkinter frame
        frame = tk.Frame(window, relief=tk.RAISED)
        frame.pack()

        # Button to list all videos
        list_videos_btn = tk.Button(frame, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, sticky="W", padx=10, pady=10)

        # Button to reset play count of videos
        play_videos_btn = tk.Button(frame, text="Reset", command=self.reset_play_count)
        play_videos_btn.grid(row=0, column=4, sticky="E", padx=10, pady=10)

        # Button to play videos (no command provided)
        exit_button = tk.Button(frame, text="Play Videos", command=self.play_video)
        exit_button.grid(row=0, column=4, sticky="W", padx=10, pady=10)

        # Button to add a video to the playlist
        check_video_btn = tk.Button(frame, text="Add Playlist", command=self.check_digit)
        check_video_btn.grid(row=0, column=3, sticky="W", padx=10, pady=10)

        # Button to exit the system
        exit_button = tk.Button(frame, text="Exit System", command=window.destroy)
        exit_button.grid(row=0, column=4, sticky="E", padx=10, pady=10)

        # Label for entering video number
        enter_lbl = tk.Label(frame, text="Add Video Number:")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Entry widget for inputting video number
        self.input_txt = tk.Entry(frame, width=3)
        self.input_txt.grid(row=0, column=2, sticky="E", padx=10, pady=10)

        # ScrolledText widget for displaying video details
        self.video_txt = tkst.ScrolledText(frame, width=50, height=14, wrap="none")
        self.video_txt.grid(row=1, column=0, columnspan=3, sticky="NW", padx=10, pady=10)

        # Text widget for displaying playlist
        self.playlist_txt = tkst.ScrolledText(frame, width=20, height=14, wrap="none")
        self.playlist_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Label for displaying status messages
        self.status_lbl = tk.Label(frame, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=1, column=0, columnspan=4, sticky="SW", padx=10, pady=10)

        # Canvas for displaying images
        self.image = tk.Canvas(frame, width=255, height=305)
        self.image.grid(row=1, column=4, padx=10, pady=10)

        # Call the welcome_image function to display a welcome image
        self.welcome_image()

    # Reset the play count of a video based on user input
    def reset_play_count(self):
        lib.reset_play_count()
        # Clear the video_txt and playlist_txt widgets
        self.input_txt.delete(0, tk.END)
        self.video_txt.delete(1.0, tk.END)
        self.playlist_txt.delete(1.0, tk.END)
        self.status_lbl.configure(text="Reset Videos button was clicked!")
        self.welcome_image()

    # List all videos in the library and display in video_txt widget
    def list_videos_clicked(self):
        video_list = lib.list_all()
        self.video_txt.insert(1.0, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

    # Check if the input is a digit; if yes, call check_video_clicked, otherwise display a message
    def check_digit(self):
        input_text = self.input_txt.get()
        if input_text.isdigit():
            input_text = str(int(input_text))
            playlist = lib.list_the_playlist()
            if input_text not in playlist:
                self.check_video_clicked()
            else:
                self.input_txt.delete(0, tk.END)
        else:
            set_text(self.playlist_txt, "Please Input Number")
            self.welcome_image()
        self.status_lbl.configure(text="Add Videos button was clicked!")

    # Check details of a video based on user input1 and display in video_txt widget
    def check_video_clicked(self):
        key = self.input_txt.get()
        key = str(int(key))
        self.name = lib.get_name(key)
        if self.name is not None:
            self.director = lib.get_director(key)
            self.rating = lib.get_rating(key)
            self.play_count = lib.get_play_count(key)
            num_image = lib.get_image(key)
            image_original = Image.open(f"./picture/{num_image}.jpg").resize((255, 305))
            image = ImageTk.PhotoImage(image_original)
            self.image.create_image(0, 0, anchor=tk.NW, image=image)
            self.image.image = image
            # Display video details and increment play count
            video_details = f"Name: {self.name} _ Director: {self.director} _ Rating: {self.rating}\n"
            self.video_txt.insert(1.0, video_details)
            # Add video to the playlist
            self.add_video_to_playlist()
        else:
            set_text(self.playlist_txt, f"Video {key} not found")
            self.input_txt.delete(0, tk.END)
            self.welcome_image()

    # Add the current video to the playlist and update play count
    def add_video_to_playlist(self):
        video_key = self.input_txt.get()  # Get the video key from input text widget
        video_key = str(int(video_key))
        playlist = lib.list_the_playlist()
        if int(video_key) in playlist:
            set_text(self.playlist_txt, f"Video {video_key} already exists in the playlist")
        else:
            lib.add_to_playlist(video_key)
            set_text(self.playlist_txt, f"Video {video_key} added to playlist")
        # Clear the input text widget
        self.input_txt.delete(0, tk.END)

    def play_video(self):
        set_text(self.playlist_txt, tk.END)
        lib.increase_play_count()
        playlist = lib.list_the_playlist()
        for key in playlist:
            name = lib.get_name(key)
            if name is not None:
                director = lib.get_director(key)
                rating = lib.get_rating(key)
                play_count = lib.get_play_count(key)
                # Display video details and increment play count
                video_details = (f"Name: {name}\n Director: {director}\n Rating: {rating}\n Play: {play_count}\n "
                                 f"____________________\n")
                self.playlist_txt.insert(1.0, video_details)
        self.welcome_image()

    # Display a welcome image in the image canvas
    def welcome_image(self):
        image_original = Image.open("./picture/welcome.png").resize((255, 255))
        image = ImageTk.PhotoImage(image_original)
        self.image.create_image(0, 0, anchor=tk.NW, image=image)
        self.image.image = image


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    CreateVideoList(window)  # open the CreateVideoListVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc
