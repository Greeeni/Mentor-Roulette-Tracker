import os
import requests
import urllib.parse
import json
import pandas as pd
from os.path import exists
from dotenv import load_dotenv
load_dotenv()
tomestone_key = os.getenv("tomestone_key")
tomestone_csrf = os.getenv("tomestone_csrf")

'''
To get the CSRF TOKEN for tomestone.gg, go to :
https://tomestone.gg/api/documentation#/ClassJob/afcba82837e017446763caf52146933f

On the top of the website, you have to authorize your API key you receive from the website:
https://tomestone.gg/

The format in which the key needs to be authorized is by inserting "Bearer <your_api_key_here>"

Then, to gather the curl headers, I ran one of the examples on the Swagger site, copy and pasted the Curl
into a site such as:
https://curlconverter.com/

'''
headers = {
    'accept': 'application/json',
    'Authorization': tomestone_key, # Has to follow the format "Bearer <your_api_key_here>"
    'X-CSRF-TOKEN': tomestone_csrf,
}

# url = 'https://tomestone.gg/api/'

def class_job(page, limit):
    params = {
        'page': str(page),
        'limit': str(limit),
    }
    response = requests.get('https://tomestone.gg/api/classjob', params=params, headers=headers)
    print(response.status_code)
    print(response.json())

# class_job(1, 100)

def dungeons():
    params = {
        'page': '1',
        'limit': '99',
    }
    response = requests.get('https://tomestone.gg/api/instance', params=params, headers=headers)
    print(response.status_code)
    print(response.json())
    if exists("dungeons.json"):
        print("json Exists, continuing")
    else:
        params = {
            'page': '1',
            'limit': '99',
        }
        response = requests.get('https://tomestone.gg/api/instance', params=params, headers=headers)
        print(response.status_code)
        # print(response.json())
        print("Generating json:")
        with open("dungeons.json", "xt") as file:
            json.dump(response.json(), file, indent=4)

keys_to_delete = ['bannerHd', 'banner', 'nameDe', 'nameFr', 'nameJp', 'descriptionDe', 'descriptionFr', 'descriptionJp']
def delete_values(json_data, keys):
    for result in json_data["results"]:
        for key in keys:
            if key in result:
                result[key] = ""
                result.pop(key, None)

            

def clean_dungeons():
    # data = json.loads()
    print('Cleaning dungeons.json')
    with open("dungeons.json", 'r') as f:
        data = json.load(f)
    
    delete_values(data, keys_to_delete)
    with open('dungeons.json', 'w') as file:
        json.dump(data, file, indent = 4)



if __name__ == "__main__":
    # dungeons()
    # clean_dungeons()
    df = pd.read_json('dungeons.json')

    # print(df.to_string()) 

    # TODO 
    # Check if hasNextPage == true/false to gather all information
    # Find a way to collect all the data, and then from there separate it into different corresponding files
    # Decide on using CSV or JSON (Probably json for ease of readability)