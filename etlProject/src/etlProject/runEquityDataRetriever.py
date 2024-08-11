import equityDataRetriever
import json

with open('config.json') as config_file:
    data = json.load(config_file)['stockprediction']['properties']['dataload']
    path = data['path']
    url  = data['url']

if __name__ == "__main__":
    equityDataRetriever.main_daily(url,path)