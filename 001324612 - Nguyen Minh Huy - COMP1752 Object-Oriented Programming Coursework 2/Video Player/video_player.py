# Import the Tkinter library
import tkinter as tk
# Import the custom modules
import font_manager as fonts
from check_videos import CheckVideos
from create_video_list import CreateVideoList
from update_videos import UpdateVideos


# Function to handle "Check Videos" button click
def check_videos_clicked():
    status_lbl.configure(text="Check Videos button was clicked!")
    # Open a new CheckVideos window
    CheckVideos(tk.Toplevel(frame))


# Function to handle "Create Video List" button click
def create_video_list_clicked():
    status_lbl.configure(text="Create Video List button was clicked!")
    # Open a new CreateVideoList window
    CreateVideoList(tk.Toplevel(frame))


# Function to handle "Update Videos" button click
def update_videos_clicked():
    status_lbl.configure(text="Update Videos button was clicked!")
    # Open a new UpdateVideos window
    UpdateVideos(tk.Toplevel(frame))


# Create the main application window
window = tk.Tk()
window.geometry("520x180")
window.title("Video Player")
window.iconbitmap(r"./picture/logo.ico")

# Create a Tkinter frame
frame = tk.Frame(window, relief=tk.RAISED)
frame.pack()

# Configure fonts
fonts.configure()

# Label for header text
header_lbl = tk.Label(frame, text="Select an option by clicking one of the buttons below:")
header_lbl.grid(row=0, column=0, sticky="NW", columnspan=3, padx=10, pady=10)

# Button to check videos
check_videos_btn = tk.Button(frame, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, stick="NW", padx=10, pady=10)

# Button to create video list
create_video_list_btn = tk.Button(frame, text="Create Video List", command=create_video_list_clicked)
create_video_list_btn.grid(row=1, column=1, stick="NW", padx=10, pady=10)

# Button to update videos
update_videos_btn = tk.Button(frame, text="Update Videos", width=12, command=update_videos_clicked)
update_videos_btn.grid(row=1, column=2, stick="NW", padx=10, pady=10)

# Label for status messages
status_lbl = tk.Label(frame, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, stick="NW", columnspan=3, padx=10, pady=10)

# Button to exit the system
exit_button = tk.Button(frame, text="Exit System", width=12, command=window.destroy)
exit_button.grid(row=2, column=2, stick="NW", padx=10, pady=10)


# Start the Tkinter event loop
frame.mainloop()
