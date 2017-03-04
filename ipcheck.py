import requests
import json
import os

if __name__ == '__main__':
    resp = requests.get('https://api.ipify.org?format=json')
    ipinfo = json.loads(resp.text)
    
    if os.path.isfile('ip.json'):
        with open('ip.json', 'r') as file:
            try:
                f = json.loads(file.readline())
                if ipinfo['ip'] != f['ip']:
                    with open('ip.json', 'w+') as file:
                        file.write(json.dumps(ipinfo))
                        print("\nPublic IP: {ip}\n".format(ip=ipinfo['ip']))
                else: 
                    print("\nPublic IP: {ip}\n".format(ip=ipinfo['ip']))
            except(json.decoder.JSONDecodeError):
                with open('ip.json', 'w+') as file:
                    file.write(json.dumps(ipinfo))
                    print("\nPublic IP: {ip}\n".format(ip=ipinfo['ip']))
            
    else:
        with open('ip.json', 'w+') as file:
            file.write(json.dumps(ipinfo))
            print("\nPublic IP: {ip}\n".format(ip=ipinfo['ip']))
