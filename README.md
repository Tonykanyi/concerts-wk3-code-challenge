# Concerts-code-challenge

The Concert Management System is a Python-based application designed to manage bands, venues, and concerts. It uses SQLite as the database backend and allows users to perform various operations such as creating, updating, deleting, and querying records related to concerts and their participants.

Features
Bands:

Create, update, delete, and retrieve band information such as the name and hometown of the band.
Retrieve all concerts performed by a specific band.
Find out which venues a band has performed at.
Identify the band with the most performances.
Venues:

Manage venue information, including name and city.
Retrieve a list of concerts held at a particular venue.
Query the most frequent band that has performed at a specific venue.
Concerts:

Schedule concerts by associating bands and venues with specific dates.
Query information such as:
All concerts performed by a specific band.
The venues where a band has performed.
Concert introductions and hometown shows.
Setup Instructions
Prerequisites
Python 3.x: Make sure you have Python installed on your machine.
SQLite: SQLite is bundled with Python, but you can install the CLI if needed for manual database management.
Installing Dependencies
Clone the repository:

bash
Copy code
git clone https://github.com/Tonykanyi/Concerts-code-challenge.git
Navigate to the project directory:

bash

cd concert-management-system
Install dependencies using Pipenv (or use pip to install directly from the Pipfile):

bash

pipenv install
Activate the virtual environment:

bash

pipenv shell
Database Setup
The project uses SQLite to store band, venue, and concert data. The database schema will be automatically created if it does not exist.

To create the database and tables, run the application:

bash

python debug.py
This will create a database.db file in the root directory and set up the required tables.

How to Use
After setting up the database, you can interact with the Concert Management System using the available methods in the Band, Venue, and Concert classes. Below are a few examples of how to use the system:

Example Usage
python
Copy code
from band import Band
from venue import Venue
from concert import Concert

# Create a band
sautiSol = Band.create("Sauti Sol", "Nairobi")
manchesterReds = Band.create("Manchester Reds", "Manchester")

# Create a venue
kasaraniStadium = Venue.create("Kasarani Stadium", "Nairobi")
nyayoStadium = Venue.create("Nyayo Stadium", "Nairobi")

# Create a concert
concert1 = Concert.create("2023-12-23", sautiSol, kasaraniStadium)
concert2 = Concert.create("2023-12-24", manchesterReds, nyayoStadium)

# Query information
print(sautiSol.concerts())            # List of concerts by Sauti Sol
print(sautiSol.venues())              # Venues where Sauti Sol has performed
print(Band.most_performances())       # Find the band with the most performances
print(kasaraniStadium.most_frequent_band()) # Find the most frequent band at Kasarani Stadium
Database Schema
The system uses three primary tables: bands, venues, and concerts. Here’s an overview of the database schema:

Bands Table
Column	Type	Description
id	INTEGER	Primary key (auto-increment)
name	TEXT	Name of the band
hometown	TEXT	Hometown of the band
Venues Table
Column	Type	Description
id	INTEGER	Primary key (auto-increment)
title	TEXT	Name of the venue
city	TEXT	City where the venue is located
Concerts Table
Column	Type	Description
id	INTEGER	Primary key (auto-increment)
date	TEXT	Date of the concert
band_id	INTEGER	Foreign key referencing bands
venue_id	INTEGER	Foreign key referencing venues
Query Functions
Band Class
create(name, hometown): Creates a new band and saves it to the database.
concerts(): Returns all concerts associated with the band.
venues(): Returns all venues where the band has performed.
most_performances(): Returns the band with the most performances.
Venue Class
create(title, city): Creates a new venue and saves it to the database.
concerts(): Returns all concerts held at the venue.
most_frequent_band(): Returns the band that has performed the most at this venue.
Concert Class
create(date, band, venue): Creates a new concert and saves it to the database.
introduction(): Returns a string introducing the concert with the band and venue.
hometown_show(): Returns True if the concert is happening in the band's hometown.
Contributing
If you'd like to contribute to this project, please feel free to submit a pull request or open an issue with your suggestions.

License
This project is licensed under the MIT License. See the LICENSE file for more details.