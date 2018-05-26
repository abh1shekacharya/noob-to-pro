import requests
import operator

apiId = 'b2f3c3b9ce4f2d2e9ba3c23e91e8e4e8'
header = {"user_key": apiId, "Accept": "application/json"}

cityName = str(input('Enter the City Name: '))
cityUrl = 'https://developers.zomato.com/api/v2.1/cities?q=' + cityName
cityReq = requests.get(cityUrl, headers = header)
cityData = cityReq.json()
cityId = str(cityData['location_suggestions'][0]['id'])

resUrl = 'https://developers.zomato.com/api/v2.1/search?entity_id=' + cityId + '&entity_type=city'
resReq = requests.get(resUrl, headers = header)
resData = resReq.json()
resRat = []
resInfo = {}
for i in resData['restaurants']:
    if (float(i['restaurant']['user_rating']['aggregate_rating'])) > 3:
        resInfo[i['restaurant']['id']] = (float(i['restaurant']['user_rating']['aggregate_rating']))

resInfo = sorted(resInfo.items(), key=operator.itemgetter(1), reverse=True)

print('The Top 5 Restaurant in ' + cityName + ' based on user rating are:- ')

for i in range(5):
    topUrl = 'https://developers.zomato.com/api/v2.1/restaurant?res_id=' + resInfo[i][0]
    topReq = requests.get(topUrl, headers = header)
    topData = topReq.json()
    print(topData['name'])




