import requests # this library will help you make your requests
import json # this library will help parse api data in json format 

# below we will define components of the URL to simplify the request 
lat = str(42)
long = str(71)
apiKey = "EnterYourApiKeyHere"

completeRequest = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+long+"&appid="+apiKey

# when making an API call, we can add parameters to the endpoint. An endpoint is just the exact data we are requesting from the server, and the more parameters, the more specific the data that is returned will be
# for example, the api we're using to make this request, we can filter for 'mode' - which is the data structure returned (json is default), and even 'units' - such as metric vs imperial

# below we will strucuture the requests
weatherEndpoint = requests.get(completeRequest)
weatherEndpointData = weatherEndpoint.text
parseEndpoint = json.loads(weatherEndpointData)
print(parseEndpoint) # hopefully, this will print some data about the location we inserted for latitude and longitude
