'''
Name: Noah Draper, Drew Sexton
email: drapernm@mail.uc.edu, sextondw@mail.uc.edu
Assignment: Assignment 07
Course: IS 4010
Semester/Year: Fall 2022
Brief Description:This projects demonstrates that we can make and API call with a URL
'''

import json
import requests
import webbrowser

#Show NASA Astronomy pic of the day
def APOD():

    #data request
    params = {"api_key": "6mg0rSabfpZ3xx3RujevZPu8wqlxgGa1AcWjxbno", "hd": True, "count" : 1}    
    API = r"https://api.nasa.gov/planetary/apod?"
    data = requests.get(API, params = params)
    
    parsed_json = json.loads(data.text) #python dictionary

    
    print("Title:", parsed_json[0]["title"]) #title of photo
    print("Explanation:", parsed_json[0]["explanation"]) #Explanation of photo
    print("Date:", parsed_json[0]["date"]) #Date Taken
    
    if "copyright" in parsed_json[0]:
        print("Copyright:", parsed_json[0]["copyright"]) #Copyright owner
    else:
        print("Image is public domain") #pulic domain image
    
    webbrowser.open(parsed_json[0]["url"]) #shows image in browser window
APOD()

