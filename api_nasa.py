import requests
from datetime import datetime,timedelta

#1. NEO Feed- obtaining data of asteroid close to earth

start_date=(datetime.now()-timedelta(1)).strftime('%Y-%m-%d')
end_date= (datetime.now()+timedelta(7)).strftime('%Y-%m-%d')
api_key='YUM3KrFjewBOn44QzOdjUBdT1KOHbBx7H1ToFIYc'

feed_response=requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY')
if feed_response.status_code==200:
	data=feed_response.json() #in a dictionary format
	#velocity, distance from earth, name ,diameter
	for date in data['near_earth_objects']: 
		for neo in data['near_earth_objects'][date]:
			print("Name : ",neo["name"],"Velocity : ",neo["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"],
            "Date : ", neo["close_approach_data"][0]["close_approach_date"],
			"Diameter : ", neo["estimated_diameter"]["kilometers"]["estimated_diameter_max"])


#2.Neo - Lookup  looking up specific Asteroid based on its NASA JPL small body (SPK-ID) ID

# Asteroid SPK-ID
asteroid_id = '3542519'
api_key='YUM3KrFjewBOn44QzOdjUBdT1KOHbBx7H1ToFIYc'

lookup_response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=DEMO_KEY')
asteroid_data = lookup_response.json()

print("Name: ", asteroid_data['name'], "NASA JPL URL:", asteroid_data['nasa_jpl_url'], 
      "Diameter : " , asteroid_data['estimated_diameter']['kilometers']['estimated_diameter_max'])


#3. Neo - browsing overall asteroid data set



# Fetch data
browse_response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=DEMO_KEY')
browse_data = browse_response.json()

# Process and print data
for neo in browse_data['near_earth_objects']:
    print(f"Name: {neo['name']}, NASA JPL URL: {neo['nasa_jpl_url']}, "
          f"Absolute Magnitude: {neo['absolute_magnitude_h']}")




