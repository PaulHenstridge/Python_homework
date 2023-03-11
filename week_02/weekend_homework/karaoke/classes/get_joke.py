import requests
import json


class MakeApiCall:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        response = requests.get(f"{self.url}", headers={"Accept": "application/json"})
        if response.status_code == 200:
            print("data fetched sucessfully")
            my_json = response.json()
            print(my_json["joke"])
            return my_json["joke"]
        else:
            print(f"Error occured: Status code {response.status_code}")
