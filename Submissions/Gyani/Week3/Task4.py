import requests
import re

city=input('Enter the city you want to get information :   ')

city=city.replace(' ','%20')

url = "https://developers.zomato.com/api/v2.1/locations?query={}".format(city)

header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "136b37c8c4bdd2d25c81bbb090daa37e"}

r=requests.get(url, headers=header)

city=city.replace('%20',' ')




if r.json()['location_suggestions'][0]['city_name'].find(city)==-1:
	print("City Not found.")
	exit()

Entity_Type=r.json()['location_suggestions'][0]['entity_type']
Entity_Id=r.json()['location_suggestions'][0]['entity_id']


url1 = "https://developers.zomato.com/api/v2.1/search?entity_id={}&entity_type={}&sort=rating&order=desc".format(Entity_Id,Entity_Type)
r1=requests.get(url1, headers=header)

if (r1.json()['results_found']==0):
	print("Sorry :-( \nNo restaurants are found for this city.")
	exit()
restro_list=r1.json()['restaurants']
number=r1.json()['results_shown']
count=1
print("The top 5 restaurants are :-\n")
for i in range(number):
	s=restro_list[i]
	if s['restaurant']['user_rating']['aggregate_rating']>'3':
		print(count,") Name of resturant:    ",s['restaurant']['name'])
		print()
		print("    Address:              ",s['restaurant']['location']['address'])
		print()
		print("    Aggregate User Rating:",s['restaurant']['user_rating']['aggregate_rating'])
		count=count+1
		print()
	if count==6:
		break	 

