# AsteroidWatch

<<<<<<< HEAD
AsteroidWatch/
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── api.nasa.py 
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── scripts.js
│   ├── components/
│   │   └── alert.js
│   │   └── orbitVisualization.js

database.py

tables 

1. near_earth_objects

Stores general information about each near-Earth object.

id (Primary Key, Integer): Unique identifier for the NEO.
name (String): Name of the NEO.
diameter_km (Float, Nullable): Diameter of the NEO in kilometers.
is_potentially_hazardous (Boolean): Whether the NEO is considered potentially hazardous.


2. close_approach_data

Stores data about each close approach of NEOs to Earth.

id (Primary Key, Integer): Unique identifier for the close approach event.
neo_id (Foreign Key, Integer): References id in the near_earth_objects table.
close_approach_date (Date): Date of the close approach.
relative_velocity_kph (Float): Relative velocity of the NEO during the close approach, in kilometers per hour.
miss_distance_km (Float): Distance by which the NEO will miss Earth, in kilometers.

3. users
Purpose: Stores user information for alerting and personalization features.
Columns:
id (Primary Key, Integer): Unique identifier for each user.
username (String, Unique): Username chosen by the user.
email (String, Unique): User's email address.
password_hash (String): Hashed password for authentication.
created_at (Timestamp): Timestamp when the user account was created.

4. alerts
Purpose: Stores user-specific alerts for close approaches.
Columns:
id (Primary Key, Integer): Unique identifier for each alert.
user_id (Foreign Key, Integer): References id in the users table.
neo_id (Foreign Key, Integer): References id in the near_earth_objects table.
alert_date (Timestamp): Timestamp when the alert was created.
sent (Boolean): Whether the alert has been sent to the user.

=======
Asteroid Watch is a web application that tracks Near-Earth Objects (NEOs) and provides close approach data of asteroids that might pose a potential threat to Earth. This project uses NASA's Near-Earth Object (NEO) API to fetch real-time asteroid data and stores it in a PostgreSQL database.

Features : 
Track Near-Earth Objects (NEOs): Fetch and store general information about NEOs, including their name, size, and potential hazard level.
Close Approach Data: Allow users to track close approach events for NEOs, including the approach date, relative velocity, and miss distance from Earth.
User Alerts: Send alerts to users for specific NEOs based on their close approach data.
User Management: Allow users to sign up, log in, and receive personalized asteroid alerts.

Tech Stack :
Frontend - HTML,CSS,Javascript,Three.js for 3d visualization of asteroids
Backend - Python,Flask, NASA'S neo API
Database- PostgreSQL, psycop2g
>>>>>>> b0530dc1630bd1bf68709d1a2376183dd9310916
