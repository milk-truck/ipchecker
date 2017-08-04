""" Gets your public IP address and stores it
Will add notifications when IP changes """

import json
import requests

def retrieve_ip(uri):
    """ get da ip """
    resp = requests.get(uri)
    return resp.json()['ip']

def main():
    """ Main func lol """
    theip = retrieve_ip('https://api.ipify.org?format=json')

    try:
        oldip = json.load(open('ip.json'))['ip']
    except FileNotFoundError:
        oldip = '0.0.0.0'

    if theip == oldip:
        print('No change -> {}'.format(theip))
    else:
        json.dump({'ip': theip}, open('ip.json', 'w'))
        print('IP is now {}'.format(theip))

if __name__ == '__main__':
    main()
