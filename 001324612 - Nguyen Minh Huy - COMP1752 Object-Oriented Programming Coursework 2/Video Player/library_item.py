# Class representing an item in the library
class LibraryItem:
    # Constructor to initialize the attributes of the item
    def __init__(self, image, name, director, rating=0):
        self.image = image  # Image associated with the item
        self.name = name  # Name of the item
        self.director = director  # Director of the item
        self.rating = rating  # Rating of the item, default is 0
        self.play_count = 0  # Number of times the item has been played, initialized to 0

    # Method to provide information about the item
    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"  # Returns item's name, director, and stars
        # representing rating

    # Method to generate star representation based on the item's rating
    def stars(self):
        stars = ""  # Initialize an empty string to hold stars
        for i in range(self.rating):  # Iterate over the rating value
            stars += "*"  # Add a star for each unit of rating
        return stars  # Return the stars as a string
