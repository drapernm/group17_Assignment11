'''
Created on Nov 3, 2022

@author: noahdraper
'''

import json
import requests
import webbrowser

def nasapic():

    #data request
    params = {"api_key": "6mg0rSabfpZ3xx3RujevZPu8wqlxgGa1AcWjxbno", "hd": True, "count" : 1}    
    API = r"https://api.nasa.gov/planetary/apod?"
    data = requests.get(API, params = params)
    
    title = json.loads(data.text) #parsed json - title of the image
    
    print(title[0]["title"])
    webbrowser.open(title[0]["url"]) #shows image in browser window
nasapic()

