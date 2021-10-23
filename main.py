import requests
from bs4 import BeautifulSoup


data = {
    'mth_frm_mth': '01',
    'mth_frm_yr': '2019',
    'mth_to_mth': '01',
    'mth_to_yr': '2020',
    'hdn': 'monthly'
}

url = 'https://www.moneycontrol.com/stocks/marketstats/nse-gainer/all-companies_-2/'
soup = BeautifulSoup(requests.get(url).content, 'html.parser')


print(soup.div, class_="bsr_table hist_tbl_hm")
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
