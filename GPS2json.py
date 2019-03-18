import requests
import xmltodict

API_KEY = '77059e7025a5bd97'
COUNT = 20

def GPS2json(longitude, latitude, start, keyword):
    url = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
    payload = {'key':API_KEY, 'lng':longitude, 'lat':latitude, 'start':start, 'count':COUNT, 'keyword':keyword}

    r = requests.get(url, params=payload)

    xml = r.text

    datas = xmltodict.parse(xml)

    results = []
    for data in datas['results']['shop']:
        name = data['name']
        lng = data['lng']
        lat = data['lat']
        budget = data['budget']['name']
        catch = data['catch']
        image = data['photo']['pc']['l']

        result = {'name':name, 'lng':lng, 'lat':lat, 'budget':budget, 'catch':catch, 'image':image}
        results.append(result)

    return results

longitude = '139.761457'
latitude = '35.669220'
results = GPS2json(longitude, latitude, 1, 'たこ焼き')

print(results)