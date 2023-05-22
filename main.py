import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StockX-Data-Contest-2019-3 2.csv')
dateList = df['Order Date'].tolist()
salePriceList = df['Sale Price'].tolist()
dateCountDict = {}
dateCount2017, dateCount2018, dateCount2019 = [], [], []
salePrice2017, salePrice2018, salePrice2019 = {}, {}, {}

for i in dateList:
  dateIndex = dateList.index(i)
  i = i.split('/')
  if int(i[0]) < 10 and int(i[1]) < 10:
    dateList[dateIndex] = int('20' + i[2] + '0' + i[0] + '0' + i[1])
  elif int(i[0]) < 10 and int(i[1]) >= 10:
    dateList[dateIndex] = int('20' + i[2] + '0' + i[0] + i[1])
  elif int(i[0]) >= 10 and int(i[1]) < 10:
    dateList[dateIndex] = int('20' + i[2] + i[0] + '0' + i[1])
  else:
    dateList[dateIndex] = int('20' + i[2] + i[0] + i[1])
df['Order Date'] = dateList

for i in dateList:
    if i not in dateCountDict:
      dateCountDict[i] = 1
    elif i in dateCountDict:
      dateCountDict[i] += 1

for i in list(dateCountDict):
  if int(i) >= 20170000 and int(i) < 20180000:
    dateCount2017.append(dateCountDict[i])
  elif int(i) >= 20180000 and int(i)< 20190000:
    dateCount2018.append(dateCountDict[i])
  else:
    dateCount2019.append(dateCountDict[i])

for i in range(len(dateList)):
  if int(dateList[i]) >= 20170000 and int(dateList[i]) < 20180000:
    salePrice2017[dateList[i]] = int(salePriceList[i].replace('$', '').replace(',', ''))
  elif int(dateList[i]) >= 20180000 and int(dateList[i]) < 20190000:
    salePrice2018[dateList[i]] = int(salePriceList[i].replace('$', '').replace(',', ''))
  else:
    salePrice2019[dateList[i]] = int(salePriceList[i].replace('$', '').replace(',', ''))

avg2017 = sum(dateCount2017) / len(dateCount2017)
avg2018 = sum(dateCount2018) / len(dateCount2018)
avg2019 = sum(dateCount2019) / len(dateCount2019)

avgPrice2017 = sum(salePrice2017.keys()) / len(salePrice2017)
avgPrice2018 = sum(salePrice2018.keys()) / len(salePrice2018)
avgPrice2019 = sum(salePrice2019.keys()) / len(salePrice2019)

plt.plot(['2017', '2018', '2019'], [avg2017, avg2018, avg2019])
plt.show()

plt.plot(['2017', '2018', '2019'], [avgPrice2017, avgPrice2018, avgPrice2019])
plt.show()