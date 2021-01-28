import os
import requests

AIRTABLE_BASE_ID=os.environ.get('AIRTABLE_BASE_ID')
AIRTABLE_API_KEY=os.environ.get('AIRTABLE_API_KEY')
AIRTABLE_TABLE_NAME=os.environ.get('AIRTABLE_TABLE_NAME')

def push_to_airtable(email=None):
    if email is None:
        return False
    endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"

    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "records": [
            {
            "fields": {
                "email is awesome": email,
            }
            }
        ]
    }

    r = requests.post(endpoint,json=data, headers=headers)
    print(r.json())
    return r.status_code == 200

def get_from_airtable():

    endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"

    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }

    params = {
        "maxRecords":"100",
        "view":"Grid view"
    }

    r = requests.get(endpoint, headers = headers, params = params )
    print(endpoint)
    print(r.status_code, ' ', r.json())
    print(len(r.json()['records']))

    response = []
    for item in r.json()['records']:
        response.append(item['fields']['email is awesome'])
        print(item['fields']['email is awesome'])
    return response
