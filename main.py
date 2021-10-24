import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

data = requests.get(
    'https://www.moneycontrol.com/stocks/marketstats/bsemact1/index.php').text


data1 = requests.get(
    'https://www.moneycontrol.com/stocks/marketstats/nse-gainer/all-companies_-2/').text

soup = BeautifulSoup(data1, 'lxml')


# print(soup)
allCompanies = soup.find_all('span', class_='gld13 disin')

# print(allCompanies)

companyNames = []
for row in allCompanies:
    link = row.find('a').text
    companyNames.append(str(link))

# print(companyNames)

tablerow = soup.find_all('tr')

companyHigh = []
companyLow = []
companyClose = []
companyChange = []
companyGain = []
for tr in tablerow:

    # high price
    high = tr.find_all('td', attrs={'width': 75, 'align': 'right'})
    if len(high) == 0:
        continue
    for i in high:
        i = i.text.replace(',', '')
        companyHigh.append(float(i))
        break
# print(companyHigh)
#         # low price
    low = tr.find_all('td', attrs={'width': 80, 'align': 'right'})
    flag = True
    for i in low:
        i = i.text.replace(',', '')
        if flag == True:
            companyLow.append(float(i))
            flag = False
        else:

            companyClose.append(float(i))
            flag = True

    change = tr.find_all('td', attrs={'width': 45, 'align': 'right'})
    percentchangeandgainflag = True
    for i in change:
        if i.has_attr('class'):
            if percentchangeandgainflag == True:
                companyChange.append(float(i.text))
                percentchangeandgainflag = False
            else:
                companyGain.append(float(i.text))
                percentchangeandgainflag = True


companyData = []


# print(companyNames)
# print(companyHigh)
# print(companyLow)
# print(companyChange)
# print(companyGain)


for i in range(len(companyNames)):
    companyData.append({
        'company': companyNames[i],
        'high': companyHigh[i],
        'low': companyLow[i],
        'change_in_per': companyChange[i],
        'gain': companyGain[i]
    })

today = date.today()

filename = today.strftime("%b-%d-%Y")

fields = ['company', 'high', 'low', 'change_in_per', 'gain']
filename = filename+".csv"
with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(companyData)
