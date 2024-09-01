import testnew
import json

with open('config.json') as config_file:
    data = json.load(config_file)['stockprediction']['properties']['dataload']
    path = data['path']
    symbolList = data['symblist']
    fromdate = '20240829'
    todate   = '20240830'

if __name__ == "__main__":
    testnew.main_daily1(fromdate,todate,path,symbolList)