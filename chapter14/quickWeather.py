import json, requests, sys
apiFile = open('apikey.txt')
APIKEY = apiFile.read().rstrip('\n')
if len(sys.argv) < 2:
    print('Location needed: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&APPID={APIKEY}' % (location)
response = requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'],'\n')
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'],'\n')
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
