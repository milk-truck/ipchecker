import requests, json, os

r = requests.get('https://api.ipify.org?format=json')
j = json.loads(r.text)

if os.path.isfile('ip.json'):
    with open('ip.json', 'r') as file:
        f = json.loads(file.read())
        if (j['ip'] != f['ip']):
            with open('ip.json', 'w+') as file:
                file.write(json.dumps(j))
else:
    with open('ip.json', 'w+') as file:
        file.write(json.dumps(j))
