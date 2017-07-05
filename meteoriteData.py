import requests
import json

class LandingsData:
   def __init__(self, landings_data):
       self.landings_data = landings_data

   def get_data(self):
   	landings_data = requests.get('https://data.nasa.gov/resource/y77d-th95.json')
   	print(repr(landings_data))

   	with open(self.landings_data) as landings_data:
   		landings_data = json.load(landings_data)
   		landings_list = landings_data['data']
   		for landings_data in landings_list:
   			the_id = landings_data [0]
   			mass = landings_data[1]
   			name = landings_data[2]
   			year = landings_data[7]
   		print ("ID: {} Mass: {} Name: {} Year: {}".format(the_id, mass, name, year))

total_records = LandingsData(len(landings_data)
	print ("Total records: {}".format(total_records))

#get total records
#total_records = json.loads(landings_data)
#print ("Total records: " len(total_records))

#get total mass > 2kg
 # for landings_data in landings_list:
#landings_data.mass > 2kg


#get how many meteorites fell in the year 2008
 # for landings_data in landings_list:
#landings_data.mass > 2kg
#landings_data.year = 2008

#get name of the 9,992nd record in the dataset
#landings_data.id = 2008


#the difference in mass between the 9,992nd record and the record with an id of 9992
#landings_data.id = 9992 AND ???