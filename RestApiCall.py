from urllib2 import Request, urlopen, URLError

request = Request('http://api.openhazards.com/GetEarthquakeProbability?q=San+Francisco,+CA&m=6.8&r=100')
request1=Request("http://api.aerisapi.com/earthquakes/closest?p=74640")

try:
	response = urlopen(request)
	Result = response.read()
	print Result
	#print kittens[559:1000]
except URLError, e:
    print 'No kittez. Got an error code:', e


    """
    You can find more info about the request parameter here | The response is in xml format
http://www.openhazards.com/data/GetEarthquakeProbability

We can try this rest api as well, here we get the response in Json format : 
http://www.aerisweather.com/support/docs/api/reference/endpoints/earthquakes/

    """