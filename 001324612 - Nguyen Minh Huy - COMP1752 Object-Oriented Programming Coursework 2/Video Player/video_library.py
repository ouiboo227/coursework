# Importing the 'csv' module to work with CSV files and importing the 'LibraryItem' class from another file
import csv
from library_item import LibraryItem

# Initializing an empty dictionary to hold library items and defining the path to the CSV file
library = {}
csv_file_path = 'data.csv'


# Function to read data from a CSV file and populate the 'library' dictionary
def read_csv_data(file_path):
    with open(file_path, newline='') as csvfile:  # Opening the CSV file in read mode
        reader = csv.DictReader(csvfile)  # Creating a CSV reader object
        for row in reader:  # Iterating through each row in the CSV file
            # Creating LibraryItem objects and storing them in the 'library' dictionary using 'ID' as the key
            library[row["ID"]] = LibraryItem(
                row["ID"],
                row["Name"],
                row["Director"],
                int(row["Rating"])
            )


# Function to write data from the 'library' dictionary back to the CSV file
def write_csv_data(file_path):
    with open(file_path, 'w', newline='') as csvfile:  # Opening the CSV file in write mode
        fieldnames = ["ID", "Name", "Director", "Rating"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # Creating a CSV writer object
        writer.writeheader()  # Writing header row in the CSV file
        for item in library.values():  # Iterating through values in the 'library' dictionary
            # Writing each LibraryItem's data as a row in the CSV file
            writer.writerow({
                "ID": item.image,
                "Name": item.name,
                "Director": item.director,
                "Rating": item.rating
            })


# Reading data from the CSV file and populating the 'library' dictionary
read_csv_data(csv_file_path)


# Function to set the rating of a video in the library
def set_rating(key, rating):
    try:
        item = library[key]  # Accessing the LibraryItem object using the key
        item.rating = rating  # Updating the rating of the item
        write_csv_data(csv_file_path)  # Update the CSV file with the new rating
    except KeyError:
        return  # Handling if the provided key is not found in the library


# Function to set the director of a video in the library
def set_director(key, director):
    try:
        item = library[key]  # Accessing the LibraryItem object using the key
        item.director = director  # Updating the director of the item
        write_csv_data(csv_file_path)  # Update the CSV file with the new director
    except KeyError:
        return  # Handling if the provided key is not found in the library


# Function to set the name of a video in the library
def set_name(key, name):
    try:
        item = library[key]  # Accessing the LibraryItem object using the key
        item.name = name  # Updating the name of the item
        write_csv_data(csv_file_path)  # Update the CSV file with the new name
    except KeyError:
        return  # Handling if the provided key is not found in the library


# Search for videos based on name, director, or rating
def search_all(search_input):
    results = {}
    for key, item in library.items():
        # Check if search_input is in video name or director
        if (
                search_input.lower() in item.name.lower() or
                search_input.lower() in item.director.lower()
        ):
            if key in results:
                results[key].append(item)
            else:
                results[key] = [item]
        # Check if search_input is a digit and matches video rating
        elif search_input.isdigit() and int(search_input) == item.rating:
            if key in results:
                results[key].append(item)
            else:
                results[key] = [item]

    return results


# Search for a specific video based on name, director, or rating
def search_library(search_input, search_type):
    results = []
    for key, item in library.items():
        if search_type == "name" and search_input.lower() in item.name.lower():
            results.append(key)
        elif search_type == "director" and search_input.lower() in item.director.lower():
            results.append(key)
        elif search_type == "rating" and str(item.rating) == search_input:
            results.append(key)

    return results


# List all videos in the library
def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


# Get the name of a video
def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


# Get the director of a video
def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


# Get the rating of a video
def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


# Get the image number of a video
def get_image(key):
    try:
        item = library[key]
        return item.image
    except KeyError:
        return -1


# Get the play count of a video
def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


playlist = {}


# Add a video to the playlist, avoiding duplicates
def add_to_playlist(key):
    try:
        item = library[key]
        if key not in playlist:
            playlist[key] = item
    except KeyError:
        return


# List videos in the playlist
def list_the_playlist():
    # Assuming playlist is a dictionary with keys as strings and values as objects with 'info' method
    output = {}
    for key in playlist:
        item = playlist[key]
        output[key] = item.info()
    return output


# Increment the play count of all videos in the playlist
def increase_play_count():
    for key in playlist:
        item = playlist[key]
        item.play_count += 1


# Reset the play count of all videos and clear the playlist
def reset_play_count():
    global playlist  # Use the global playlist variable
    playlist = {}  # Clear the playlist
    for key in library:
        item = library[key]
        item.play_count = 0
