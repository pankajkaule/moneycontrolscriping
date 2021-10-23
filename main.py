import requests
from bs4 import BeautifulSoup


# url = 'https://www.moneycontrol.com/stocks/marketstats/nse-gainer/all-companies_-2/'
# soup = BeautifulSoup(requests.get(url).content, 'html.parser').text


# allCompanies = soup.findall('div', class_='bsr_table hist_tbl_hm')
# all_data = []
# for tr in soup.select('.bsr_table hist_tbl_hm'):
#     print(tr)
#     tds = [td.get_text(strip=True) for td in tr.select('td')]
#     all_data.append(tds)

# # print on screen
# print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(
#     'Date', 'Open', 'High', 'Low', 'Close'))
# for row in all_data:
#     print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(*row))


# import requests
# from bs4 import BeautifulSoup
# url = "https://www.moneycontrol.com/stocks/marketstats/nse-gainer/all-companies_-2/"

# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html.parser')
# datatable = soup.find_all(class_="bsr_table hist_tbl_hm")


# print(datatable)  # to print html in tree structure


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
    companyNames.append(link)

# print(companyNames)

tablerow = soup.find_all('tr')

companyHigh = []
companyLow = []
companyClose = []
companyChange = []
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
    for i in low:
        i = i.text.replace(',', '')
        print(i)
        companyLow.append(float(i))

#         # close price

    close = tr.find_all('td', attrs={'width': 85, 'align': 'right'})

    # print(close)
    for i in close:
        i = i.text.replace(',', '')
        companyClose.append(i)

    change = tr.find_all('td', attrs={'width': 80, 'align': 'right'})
    # print(change)

    for i in change:
        if i.has_attr('class'):
            companyChange.append(float(i.text))

companyData = []
# print(companyChange)
# print(len(companyClose))
# print(len(companyHigh))
print(len(companyLow))
# print(len(companyClose))
# print(len(companyChange))


# for i in range(len(companyNames)):
#     companyData.append({
#         'company': companyNames[i],
#         'high': companyHigh[i],
#         'low': companyLow[i],
#         'change_in_per': companyChange[i],
#         'close': companyClose[i]
#     })

# print(companyData)
# new_dict = sorted(

#     companyData, key=lambda i: i['change_in_per'], reverse=True
# )
# print(new_dict)
