import requests
from pprint import pprint as print


def OxfordDefinition(word_id):
    app_id = "0f510216"
    app_key = "10a88b232d76d8f0025a33765a842e32"
    language = "en-gb"

    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

    res = r.json()

    if 'error' in res:
        return False

    output = {}
    resp = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audioFile'] = resp

    definitions = []

    n = len(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'])

    for i in range(n):
        definitions.append(f"👉 {res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][i]['definitions'][0]}")
    output['definition'] = "\n".join(definitions)

    return output
