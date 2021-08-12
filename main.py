import requests
from collections import OrderedDict

response = requests.get("https://www.binance.com/bapi/asset/v1/public/asset-service/product/get-exchange-info")
collection = response.json()['data']

pairs = OrderedDict()

for i in collection:
    if i['quoteAsset'] not in pairs:
        pairs[i['quoteAsset']] = []

    pairs[i['quoteAsset']].append(i['baseAsset'] + '\n')

for p in pairs:
    file = open('out/' + p + '.txt', 'w')
    lines = []

    for a in pairs.get(p):
        lines.append(p + '\\' + a)

    file.writelines(lines)
    file.close()
