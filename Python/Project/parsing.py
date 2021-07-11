# import requests
# import bs4 as bs
# from bs4 import BeautifulSoup
# import pandas as pd

# class Writer:
#     def __init__(self, parlament):
#         self.depDf = pd.DataFrame(
#             {'id': parlament.ids,
#             'name': parlament.names,
#             'fractions': parlament.fractions,
#             'link': parlament.links,
#             'fraction_link': parlament.fraction_links
#             }
#         )
#     def write_to_xlsx(self):
#         writer = pd.ExcelWriter('deputies.xlsx', engine='xlsxwriter')
#         self.depDf.to_excel(writer, sheet_name='deps', index = False)
#         writer.save()

#     def write_to_csv(self):
#         csvFileContents = self.depDF.to_csv(index=False)
#         with open("deputies.csv", "w", encoding='utf-8') as f:
#             f.write(csvFileContents)


# class Parlament:
#     def __init__(self, deputies):
#         self.deputies = deputies

#         self.ids = []
#         self.names = []
#         self.fractions = []
#         self.links = []
#         self.fractions_link = []

#         for deputy in deputies:
#             self.ids.append(deputy.id)
#             self.names.append(deputy.name)
#             self.fractions.append(deputy.fraction)
#             self.links.append(deputy.link)
#             self.fractions_link.append(deputy.fraction_link)

# class Deputy:
#     def __init__(self, id, name, fraction, link, fraction_link):
#         self.id = id
#         self.name = name
#         self.fraction = fraction
#         self.link = link
#         self.fraction_link = fraction_link

# def find_deputy():
#     url ='http://kenesh.kg/ru/deputy/list/35'

#     source = requests.get(url)
#     main_text = source.text
#     soup = BeautifulSoup(main_text, 'html.parser')
#     deputyTable = soup.find_all('table', attrs={'class':'table'})
#     deputyTableRows = deputyTable.tbody.find_all('tr')
#     deputies = []
#     for tr in deputyTableRows:
#         deputyProps = []
#         trContents = tr.find_all('td')

#         for td in trContents:
#             deputyProps.append(td.text.replace('\n', ' '))

#         deputyProps.append('http://kenesh.kg' + trContents[1].a['href'])
#         deputyProps.append('http://kenesh.kg' + trContents[2].a['href'])
#         deputyProps.append('http://kenesh.kg' + trContents[3].a['href'])
#         deputies.append(Deputy(deputyProps[0], deputyProps[1], deputyProps[2], deputyProps[3], deputyProps[4], deputyProps[5]))
#     return deputies

# p = Parlament(find_deputy())
# w = Writer(p)
# w.write_to_xlsx()
# w.write_to_csv()




# for div1 in divs:
#     print(div1.find('em', {'class': 'searched-item'}).get_text())
# for div2 in divs:
#     print(div2.find('a', {'class': 'post__title_link'}).get_text())

      
    
    
# import telebot
# import urllib.request
# import bs4 as bs
# import pandas as pd
# import aioschedule as schedule

# class Writer:
#     def __init__(self, parlament):
#         self.depDF = pd.DataFrame({
#             'id': parlament.ids,
#             'name': parlament.names,
#             'frac': parlament.frac
#         })

#     def write_to_xlsx(self):
#         writer = pd.ExcelWriter('deputies.xlsx', engine='xlsxwriter')
#         self.depDF.to_excel(writer, sheet_name='deps', index=False)
#         writer.save()
#     



#     def write_to_csv(self):
#         csvFileContents = self.depDF.to_csv(index=False)
#         with open("deputies.csv", "w", encoding='utf-8') as f:
#             f.write(csvFileContents)


# class Parlament:
#     def __init__(self, deputies):
#         self.deputies = deputies
#         self.ids = []
#         self.names = []
#         self.fractions = []
#         self.dep_links = []
#         self.frac_links = []

#         for deputy in deputies:
#             self.ids.append(deputy.id)
#             self.names.append(deputy.name)
#             self.fractions.append(deputy.fraction)
#             self.dep_links.append(deputy.dep_link)
#             self.frac_links.append(deputy.frac_link)


# class Deputy:
#     def __init__(self, id, name, fraction, dep_link, frac_link):
#         self.id = id
#         self.name = name
#         self.fraction = fraction
#         self.dep_link = dep_link
#         self.frac_link = frac_link
    
# def find_deps():
#         print("Deputies fetching...")
#         url = "http://kenesh.kg/ru/deputy/list/35"
#         source = urllib.request.urlopen(url)
#         soup = bs.BeautifulSoup(source, 'html.parser')
#         deputyTable = soup.find('table', attrs={'class': 'table'})
#         deputyTableRows = deputyTable.tbody.find_all("tr")
       
#         for tr in deputyTableRows:
#             deputies = []
#             deputyProps = []
#             trContents = tr.find_all("td")
#             for td in trContents:
#                     deputyProps.append(td.text.replace('/n', ' '))
#                     deputyProps.append('http://kenesh.kg' + trContents[1].a['href'])
#                     deputyProps.append('http://kenesh.kg' + trContents[2].a['href'])
#                     deputies.append(Deputy(deputyProps[0], deputyProps[1], deputyProps[2], deputyProps[3], deputyProps[4], ))
#             return deputies


          

# par = Parlament(find_deps())
# w = Writer(par)
# w.write_to_xlsx()
    


# ******************pagination

import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def writer(data):
    with open('~/Python/Project/kivano.csv', 'a') as file:
        write = csv.writer(file)
        return write.writerow((
            data['title'],
            data['description'],
            data['price'],
            data['status'],
            data['img']
        ))


def count_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find('div', class_='pager-wrap').find_all('a')[-1].get('href')
    total_pages = pages.split('=')[-1]
    return int(total_pages)

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    ads = soup.find('div', class_ = 'list_view').find_all('div', class_ = 'item')
    # url = 'https://www.kivano.kg'
    for ad in ads:
        try:
            title = ad.find('div', class_ = 'listbox_title').text
            description = ad.find('div', class_ = 'product_text pull-left').text
            price = ad.find('div', class_ = 'listbox_price').text
            status = ad.find('div', class_ = 'listbox_motive').text
            img = ad.find('div', class_ = 'listbox_img').find('img').get('src')
        except:
            title = 'No title'
            description = 'No description'
            price = 'No price'
            status = 'Out of stock'
            img = 'No image'

        data = {
            'title': title,
            'description': description,
            'price': price,
            'status': status,
            'img': img
        }

# writer(file)

# def main(): 
#     url = 'https://www.kivano.kg/prigotovlenie-pischi'
#     page_part = '?page='
#     tottal_pages = count_pages(get_html(url))
#     for i in range(1, tottal_pages + 1):
#         url_gen = url + page_part + str(i)
#         html = get_html(url_gen)
#         get_data(html)

# main()