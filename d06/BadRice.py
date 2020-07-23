import requests
import json
path = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'

date = requests.get(path).text#取得網路原始字串資料

list = json.loads(date) # 將 json 字串轉成 python 可用的物件

for rice in list:
    name = str(rice.get('品名'))
    if name.__contains__('池上'):
        print(rice.get('品名'),rice.get('不合格原因'))