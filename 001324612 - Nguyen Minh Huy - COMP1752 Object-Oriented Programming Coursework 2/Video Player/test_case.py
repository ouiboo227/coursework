import csv
import pytest
from library_item import LibraryItem

# Assuming the CSV file is named 'data.csv'
CSV_FILE = 'data.csv'


def read_library_data():
    library_data = []
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:  # Iterating through each row in the CSV file
            # Creating LibraryItem objects and storing them in the 'library_data' list
            library_data.append(LibraryItem(
                row["ID"],
                row["Name"],
                row["Director"],
                int(row["Rating"])
            ))
    return library_data


# Fixture to provide the library data to test functions
@pytest.fixture
def library_data():
    return read_library_data()


# Test functions using the library_data fixture
def test_library_item_image(library_data):
    item = library_data[0]  # Assuming the first item in the CSV file
    assert item.image == "0"


def test_library_item_name(library_data):
    item = library_data[2]  # Assuming the third item in the CSV file
    assert item.name == "Marriage Story"


def test_library_item_director(library_data):
    item = library_data[4]  # Assuming the fifth item in the CSV file
    assert item.director == "Robert Zemeckis"


def test_library_item_rating(library_data):
    item = library_data[6]  # Assuming the seventh item in the CSV file
    assert item.rating == 0


# Test functions using the library_data fixture
def test_library_item_info(library_data):
    item = library_data[0]  # Assuming the first item in the CSV file
    assert item.info() == "El Camino - Vince Gilligan ******"


def test_library_item_default_rating(library_data):
    item = library_data[2]  # Assuming the third item in the CSV file
    # Adjust the expected value to include stars based on the item's rating
    assert item.info() == "Marriage Story - Noah Baumbach *"


def test_library_item_stars(library_data):
    item = library_data[4]  # Assuming the fifth item in the CSV file
    assert item.stars() == "********"


def test_library_item_zero_stars(library_data):
    item = library_data[6]  # Assuming the seventh item in the CSV file
    assert item.stars() == ""


def test_library_item_play_count(library_data):
    item = library_data[8]  # Assuming the ninth item in the CSV file
    item.play_count += 1
    assert item.play_count == 1
