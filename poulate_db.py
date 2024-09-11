from api_nasa import data, asteroid_data, browse_data
import psycopg2
from psycopg2.extras import execute_values

# Database connection details
conn = psycopg2.connect(
    dbname="asteroidwatch",
    user="postgres",
    password="anika1234",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Insert data into near_earth_objects
neo_insert_query = """
    INSERT INTO near_earth_objects (id, name, diameter_km, is_potentially_hazardous) VALUES %s
    ON CONFLICT (id) DO NOTHING
"""

neo_data_to_insert = []

# Process feed data
for neo in browse_data['near_earth_objects']:
    id = neo['id']
    name = neo['name']
    diameter_km = neo['estimated_diameter']['kilometers']['estimated_diameter_max']
    is_potentially_hazardous = neo['is_potentially_hazardous_asteroid']
    neo_data_to_insert.append((id, name, diameter_km, is_potentially_hazardous))

# Insert data into near_earth_objects table
execute_values(cursor, neo_insert_query, neo_data_to_insert)

# Commit the transaction to ensure data is inserted before proceeding
conn.commit()

# Fetch all inserted NEO IDs
cursor.execute("SELECT id FROM near_earth_objects")
inserted_neos = {row[0] for row in cursor.fetchall()}

# Insert data into close_approach_data
close_approach_insert_query = """
    INSERT INTO close_approach_data (neo_id, close_approach_date, relative_velocity_kph, miss_distance_km) VALUES %s
    ON CONFLICT (id) DO NOTHING
"""
cursor1=conn.cursor()
close_approach_data_to_insert = []

# Process feed data
for date in data['near_earth_objects']:
    for neo in data['near_earth_objects'][date]:
        neo_id = neo['id']
        if neo_id in inserted_neos:  # Validate neo_id exists in near_earth_objects
            for approach in neo['close_approach_data']:
                close_approach_date = approach['close_approach_date']
                relative_velocity_kph = float(approach['relative_velocity']['kilometers_per_hour'])
                miss_distance_km = float(approach['miss_distance']['kilometers'])
                close_approach_data_to_insert.append((neo_id, close_approach_date, relative_velocity_kph, miss_distance_km))

# Insert data into close_approach_data table
execute_values(cursor1, close_approach_insert_query, close_approach_data_to_insert)

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
cursor1.close()
conn.close()
