import json
from pprint import pprint

class JsonParser:

    def read(self, fileName='./resources/data.json'):
        with open(fileName) as data_file:    
            data = json.load(data_file)
            maps = data["users"]
            project = data["name"]
            company = data["company"]["name"]
            client = data["client"]["name"]
            pprint(project)
            pprint(company)
            pprint(client)

        return maps

if __name__ == '__main__':

    parser = JsonParser()
    maps = parser.read()
    pprint(maps)
